
from urllib.parse import urlparse
import socket
import ssl
from bs4 import BeautifulSoup


class PerformanceUtil:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, soup_obj):
        self.url = soup_obj["url"]
        self.response = soup_obj["response"]
        self.soup = BeautifulSoup(self.response["text"], "html.parser")
        self.data = soup_obj["desktop_data"]

    def get_response_times(self):
        items = self.data["lighthouseResult"]["audits"]["network-requests"]["details"]["items"]
        # Initialize variables to store the load times
        server_response_time = self.data["lighthouseResult"]["audits"][
            "server-response-time"]["details"]["items"][0]["responseTime"]
        content_load_time = 0
        script_load_time = 0

        # Loop through each network request and calculate the load times
        for item in items:
            try:
                code = item["statusCode"]
                if code == 200:
                    mimeType = item["mimeType"]
                    requestDuration = item["networkEndTime"] - item["networkRequestTime"]
                    resourceType = item["resourceType"]
                
                    if ("javascript" in mimeType) or (resourceType=="Script"):
                        script_load_time += requestDuration
                    else:
                        content_load_time += requestDuration
            except Exception as e:
                print(item)
                print(e)
                continue

        return {"server_response_time": server_response_time/1000, 
                "content_load_time": content_load_time//1000, 
                "script_load_time": script_load_time//1000
                }

    def get_compression_data(self):
        resources = self.data["lighthouseResult"]["audits"]["network-requests"]["details"]["items"]

        obj_counts = {"total_objects": 0,
                      "html_obj": 0,
                      "css_obj": 0,
                      "javascript_obj": 0,
                      "image_obj": 0,
                      "other_obj": 0}

        # Define dictionary to store compressed size and original size for each resource type
        resource_sizes = {
            "html": {"original": 0, "compressed": 0, "rate": 0},
            "css": {"original": 0, "compressed": 0, "rate": 0},
            "js": {"original": 0, "compressed": 0, "rate": 0},
            "images": {"original": 0, "compressed": 0, "rate": 0},
            "other": {"original": 0, "compressed": 0, "rate": 0},
            "total_size": 0,
            "total_compressed_size": 0,
            "total_rate": 0,
        }

        # Loop through resources and add up sizes for each type
        for resource in resources:
            try:
                content_type = resource["mimeType"]
                size = resource["resourceSize"] / 1_000_000
                compressed_size = resource["transferSize"] / 1_000_000
                obj_counts["total_objects"] += 1

                if "text/html" in content_type:
                    resource_sizes["html"]["original"] += size
                    resource_sizes["html"]["compressed"] += compressed_size
                    obj_counts["html_obj"] += 1

                elif "text/css" in content_type:
                    resource_sizes["css"]["original"] += size
                    resource_sizes["css"]["compressed"] += compressed_size
                    obj_counts["css_obj"] += 1

                elif "javascript" in content_type:
                    resource_sizes["js"]["original"] += size
                    resource_sizes["js"]["compressed"] += compressed_size
                    obj_counts["javascript_obj"] += 1

                elif "image/" in content_type:
                    resource_sizes["images"]["original"] += size
                    resource_sizes["images"]["compressed"] += compressed_size
                    obj_counts["image_obj"] += 1

                else:
                    resource_sizes["other"]["original"] += size
                    resource_sizes["other"]["compressed"] += compressed_size
                    obj_counts["other_obj"] += 1
            except:
                continue

        for resource_type, sizes in resource_sizes.items():
            if isinstance(sizes, dict):
                original_size = sizes['original']
                compressed_size = sizes['compressed']

                resource_sizes["total_size"] += original_size
                resource_sizes["total_compressed_size"] += compressed_size

                if sizes["original"] > 0:
                    compression_ratio = (
                        1 - (sizes["compressed"] / sizes["original"])) * 100
                    sizes["rate"] = compression_ratio

        resource_sizes["total_rate"] = (
            resource_sizes["total_compressed_size"]/resource_sizes["total_size"])*100

        for i in resource_sizes:
            if isinstance(resource_sizes[i], dict) and resource_sizes[i]["rate"] < 0:
                resource_sizes[i]["rate"] = 0

        return {"counts": obj_counts, "sizes": resource_sizes}

    def get_amp_data(self):
        amp_data = {
            "amp_runtime": False,
            "doctype_declaration": False,
            "amp_css_boilerplate": False,
            "custom_css": False,
            "canonical_link": False,
            "amp_images": False,
        }

        # Check for the AMP runtime script
        amp_runtime = self.soup.find(
            'script', {'src': 'https://cdn.ampproject.org/v0.js'})
        if amp_runtime:
            amp_data['amp_runtime'] = True

        # Check for the AMP doctype declaration
        doctype_declaration = self.soup.find(
            text=lambda text: isinstance(text, str) and '<!doctype html>' in text)
        if doctype_declaration:
            amp_data['doctype_declaration'] = True

        # Check for the AMP CSS boilerplate
        amp_css_boilerplate = self.soup.find(
            'style', {'amp-boilerplate': True})
        if amp_css_boilerplate:
            amp_data['amp_css_boilerplate'] = True

        # Check for embedded inline custom CSS
        custom_css = self.soup.find('style', {'amp-custom': True})
        if custom_css:
            amp_data['custom_css'] = True

        # Check for AMP HTML canonical link
        canonical_link = self.soup.find('link', {'rel': 'canonical'})
        if canonical_link:
            amp_data['canonical_link'] = True

        # Check for AMP images
        amp_images = self.soup.find_all('amp-img')
        if amp_images:
            amp_data['amp_images'] = True

        return amp_data

    def get_js_errors(self):
        # Create a new Chrome browser instance
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(
            executable_path="D:\\driver\\chromedriver.exe", options=options)

        # Navigate to the website
        driver.get(self.url)

        error_strings = ["SyntaxError", "EvalError",
                         "ReferenceError", "RangeError", "TypeError", "URIError"]
        js_errors = driver.get_log("browser")
        js_errors = [error for error in js_errors if any(
            error_string in error["message"] for error_string in error_strings)]

        driver.quit()
        if js_errors:
            return True

        return False

    def check_http2(self):
        try:
            HOST = urlparse(self.url).netloc
            PORT = 443
            ctx = ssl.create_default_context()
            ctx.set_alpn_protocols(['h2', 'spdy/3', 'http/1.1'])

            conn = ctx.wrap_socket(
                socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_hostname=HOST)
            conn.connect((HOST, PORT))

            pp = conn.selected_alpn_protocol()

            if pp == "h2":
                return {"http2": True}
            else:
                return {"http2": False}
        except Exception as e:
            print(e)
            return {"http2": False}

    def check_optimized_images(self):
        audits = self.data['lighthouseResult']['audits']
        image_optimization_audit = audits['uses-optimized-images']

        if image_optimization_audit['score'] == 1:
            return True
        else:
            return False

    def check_minified_files(self):
        audits = self.data['lighthouseResult']['audits']
        css_minification_audit = audits['unminified-css']
        js_minification_audit = audits['unminified-javascript']

        print("\n\n",css_minification_audit,js_minification_audit,"\n\n")

        if css_minification_audit['score'] == 1 or js_minification_audit['score'] == 1:
            return True
        return False

    def check_depricated_html(self):
        obsolete_tags = self.soup.find_all(['center', 'font', 'marquee'])

        if len(obsolete_tags) == 0:
            return False
        else:
            return True

    def check_inline_styles(self):
        elements = self.soup.find_all(style=True)
        res = []
        for el in elements:
            styles = el['style'].strip()
            lineno = el.sourceline

            res.append({"styles": styles, "lineno": lineno})

        return {"inline_styles": res, "hasStyles":True if len(res)>0 else False}
