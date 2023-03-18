import requests
from bs4 import BeautifulSoup
from urllib import robotparser


class OnPageSEOUtil:

    def __init__(self, soup_obj):
        self.url = soup_obj["url"]
        self.response = soup_obj["response"]
        self.soup = BeautifulSoup(self.response["text"])
        

    def get_headings_data(self):
        try:
            headings_data = dict()
            tags = dict()
            total = 0
            for i in range(1, 7):
                tags_ = self.soup.find_all("h"+str(i))
                cleaned_tags = [ tag.text for tag in tags_]
                tags["H"+str(i)] = cleaned_tags
                cnt = len(tags_)
                headings_data["h"+str(i)] = cnt
                total+= cnt

            return {"headings_data":headings_data,"total_h_tags":total, "tags":tags}
        except Exception as e:
            print(e)
            return None

    def get_H1_tag(self):
        try:
            h1_tags = self.soup.find_all("h1")
            if h1_tags:
                return [i.text for i in h1_tags]
            return []
        except Exception as e:
            print(e)
            return []

    def get_lang(self):
        html_tag = self.soup.find(lambda tag: tag.has_attr("lang"))
        if html_tag:
            return html_tag.get("lang")
        return None

    def get_text_count(self):

        text = self.soup.get_text()
        return len(text.split())

    def get_title_data(self):
        title_text = self.soup.title.string
        title_length = len(title_text)
        return {"title_text": title_text, "title_length": title_length}

    def get_metaTag_data(self):
        meta = self.soup.find("meta", attrs={"name": "description"})
        if meta:
            return meta.get("content")
        else:
            return None

    def check_for_hrefLang(self):

        hreflang_elements = self.soup.find_all(
            lambda tag: tag.has_attr("hreflang"))
        return True if len(hreflang_elements) != 0 else False

    def get_image_attr_data(self):
        image_tags = self.soup.select("img")
        tags_without_alt = list(filter(lambda x: not x.has_attr(
            "alt") or x.get("alt") == "", image_tags))

        img_data = {
            "total_imgs": len(image_tags),
            "tags_without_alt_len": len(tags_without_alt),
            "tags_without_alt": tags_without_alt,
            "tags":[image_tag["src"] for image_tag in image_tags]
        }

        return img_data

    def get_canonical_tag(self):
        tag = self.soup.find_all(lambda x: 'canonical' in x.get(
            "rel") if x.has_attr("rel") else False)
        return len(tag) > 0

    def get_noindex_data(self):
        data = {"noindex_tag": False, "noindex_header": False}

        tag = self.soup.find_all(lambda x: 'noindex' in x.get(
            "content") if x.has_attr("content") else False)

        if 'X-Robots-Tag' in self.response["headers"] and 'noindex' in self.response["headers"]['X-Robots-Tag']:
            data["noindex_header"] = True

        if len(tag) > 0:
            data["noindex_tag"] = True
        return data

    def get_ssl_data(self):
        try:
            if self.url.startswith("https"):
                return {"ssl": True}

            https_url = "https://" + self.url.replace("http://", "")
            response = requests.get(https_url, timeout=5)
            response.raise_for_status()
            return {"ssl": True}

        except requests.exceptions.HTTPError as e:
            print(e)
            return {"ssl": False}
        except requests.exceptions.RequestException as e:
            print(e)
            return {"ssl": False}

    def get_robots_txt_data(self):
        robots_url = self.url + "/robots.txt"
        response = requests.get(robots_url)

        if response.status_code == 200:
            rp = robotparser.RobotFileParser(robots_url)
            rp.parse(response.text)

            if not rp.can_fetch("*", self.url):
                return {"robots": True, "blocked": True}
            else:
                return {"robots": True, "blocked": False}
        else:
            return {"robots": False, "blocked": None}

    def get_site_map(self):

        try:
            sitemap_index_url = "https://www.deepawaliseotips.com/sitemap_index.xml"
            sitemap_index = {}

            r = requests.get(sitemap_index_url)
            xml = r.text

            soup = BeautifulSoup(xml)
            sitemapTags = soup.find_all("sitemap")

            return True if len(sitemapTags) > 0 else False
        except Exception as e:
            print(e)
            return False

    def get_structured_data(self):

        # find all script tags that contain JSON-LD structured data
        json_ld_scripts = self.soup.find_all(
            'script', type='application/ld+json')

        # find all script tags that contain Microdata structured data
        microdata_scripts = self.soup.find_all(
            'script', type='application/ld+json')

        # find all tags that contain RDFa structured data
        rdfa_tags = self.soup.find_all(True, {'typeof': True})

        # find all tags that contain HTML+RDFa structured data
        html_rdfa_tags = self.soup.find_all(True, {'property': True})

        data = {}
        # check if structured data was found and print the result
        if json_ld_scripts or microdata_scripts:
            return {"schema_type": "json/ld"}
        elif rdfa_tags:
            return {"schema_type": "rdfa_tags"}
        elif html_rdfa_tags:
            return {"schema_type": "html_rdfa_tags"}
        else:
            return {"schema_type": None}
