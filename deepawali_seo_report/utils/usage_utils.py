import base64
from PIL import Image
import re
from bs4 import BeautifulSoup
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By





class UsabilityUtil:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, soup_obj):
        self.url = soup_obj["url"]
        self.response = soup_obj["response"]
        self.soup = BeautifulSoup(self.response["text"],"html.parser")
        self.mobile_data = soup_obj["mobile_data"]
        self.desktop_data = soup_obj["desktop_data"]

        '''options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        self.driver = webdriver.Chrome(options=options)'''
        


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

        # into seconds (/1000)
        fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"]
        lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]/1000
        cls_ = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]/100

        return {"fid": fid, "lcp": lcp, "cls": cls_}

    def get_lab_data(self, mode):  # mode represents mobile(0) or desktop(1).
        data = self.mobile_data if mode == 0 else self.desktop_data

        # into seconds (/1000)
        fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]/1000
        speed_index = data["lighthouseResult"]["audits"]["speed-index"]["displayValue"].replace(
            '\xa0', ' ').replace("s","")
        lcp = data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"].replace(
            '\xa0', ' ').replace("s","")
        time_interactive = data["lighthouseResult"]["audits"]["interactive"]["displayValue"].replace(
            '\xa0', ' ').replace("s","")
        blocking_time = int(data["lighthouseResult"]["audits"]["total-blocking-time"]["displayValue"].replace(
            '\xa0', ' ').replace("ms","").replace(",",""))/1000
        cls_ = data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["displayValue"].replace(
            '\xa0', ' ')

        return [fcp, speed_index, lcp, time_interactive, blocking_time, cls_]

    def get_screenshot(self, mode):
        data = self.mobile_data if mode == 0 else self.desktop_data if mode==1 else self.tablet_data

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
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' # regular expression to match email addresses

        if re.search(email_regex, text):
            return True
        return False

    '''def get_fonts(self):
        elements = self.driver.find_elements(By.XPATH, "//*[not(self::iframe) and not(self::frame) and not(self::frameset)]")
        for element in elements:
            font_size_str = element.value_of_css_property("font-size")
            if "px" in font_size_str:
                font_size = float(font_size_str.replace("px", ""))
                if font_size < 11:
                    self.driver.quit()
                    return True
        return False'''
