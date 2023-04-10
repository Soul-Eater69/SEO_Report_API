import base64
from PIL import Image
import re
from bs4 import BeautifulSoup
import io


class UsabilityUtil:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, soup_obj):
        self.url = soup_obj["url"]
        self.response = soup_obj["response"]
        self.soup = BeautifulSoup(self.response["text"], "html.parser")
        self.mobile_data = soup_obj["mobile_data"]
        self.desktop_data = soup_obj["desktop_data"]

    # mode represents mobile(0) or desktop(1).

    def get_opportunities(self, mode):
        data = self.mobile_data if mode == 0 else self.desktop_data

        audits = data["lighthouseResult"]["audits"]
        result = dict()
        for value in audits.values():
            try:
                if (value['details']['type'] == 'opportunity' and value["details"]["overallSavingsMs"] > 0):
                    result[value['title']
                           ] = value["details"]["overallSavingsMs"]/1000
            except:
                continue

        return result

    def get_vitals(self, mode):  # mode represents mobile(0) or desktop(1).

        data = self.mobile_data if mode == 0 else self.desktop_data
        fid = 0
        lcp = 0
        cls_ = 0
        try:
            fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"]
        except:
            fid = 0
        try:
            lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]/1000
        except:
            lcp = 0
        try:
            cls_ = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]/100
        except:
            cls_ = 0

        return {"fid": fid, "lcp": lcp, "cls": cls_}

    def get_lab_data(self, mode):  # mode represents mobile(0) or desktop(1).
        data = self.mobile_data if mode == 0 else self.desktop_data

        # into seconds (/1000)
        fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]/1000
        speed_index = data["lighthouseResult"]["audits"]["speed-index"]["displayValue"].replace(
            '\xa0', ' ').replace("s", "")
        lcp = data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"].replace(
            '\xa0', ' ').replace("s", "")
        time_interactive = data["lighthouseResult"]["audits"]["interactive"]["displayValue"].replace(
            '\xa0', ' ').replace("s", "")
        blocking_time = int(data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"].replace(
            '\xa0', ' ').replace("ms", "").replace(",", ""))/1000
        cls_ = data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"].replace(
            '\xa0', ' ')

        good_seo_time = True

        try:
            if float(fcp) > 2.0 or float(speed_index.strip()) > 3.0 or float(lcp.strip()) > 2.5 or float(time_interactive.strip()) > 5.0 or float(blocking_time) > 0.3 or float(cls_.strip()) > 0.1:
                good_seo_time = False
        except Exception as e:
            print(e)
            good_seo_time = True

        return [fcp, speed_index, lcp, time_interactive, blocking_time, cls_], good_seo_time

    def get_screenshot(self, mode):

        data = self.mobile_data if mode == 0 else self.desktop_data if mode == 1 else self.tablet_data

        # Assuming that the Lighthouse JSON response is stored in a variable called "data"
        screenshot_data = data["lighthouseResult"]["audits"]["final-screenshot"]["details"]["data"]
        screenshot_bytes = base64.b64decode(screenshot_data.split(",")[1])

        # Load the image using PIL
        screenshot_image = Image.open(io.BytesIO(screenshot_bytes))
        screenshot_image.save('screenshot.png', 'PNG')
        # Compress the image by reducing its quality
        image_buffer = io.BytesIO()
        screenshot_image.save(image_buffer, format='JPEG', quality=110)

        # Convert the compressed image to base64-encoded string
        image_bytes = image_buffer.getvalue()
        base64_image = base64.b64encode(image_bytes).decode('utf-8')

        # Return the base64-encoded image string as part of the API response
        return {"screenshot_image": base64_image}

    def get_mobile_viewport(self):
        viewport_tag = self.soup.find('meta', attrs={'name': 'viewport'})

        return True if viewport_tag else False

    def flash_used(self):
        flash_embeds = self.soup.find_all(
            "embed", attrs={"type": "application/x-shockwave-flash"})
        flash_objects = self.soup.find_all(
            "object", attrs={"type": "application/x-shockwave-flash"})

        return len(flash_embeds) > 0 or len(flash_objects) > 0

    def get_iframes(self):
        return len(self.soup.select("iframe")) > 0

    def get_fav_icon(self):
        return True if self.soup.find_all('link', attrs={'rel': re.compile("^(shortcut icon|icon)$", re.I)}) else False

    def get_emails(self):
        text = self.response["text"]
        # regular expression to match email addresses
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.search(email_regex, text):
            return True
        return False
