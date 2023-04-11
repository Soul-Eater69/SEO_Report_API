import re
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import json
import os
from deepawali_seo_report import app


class DataSetter:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, domain_name):
        try:
            self.url, self.response = self.get_url_content(domain_name)
            self.soup = BeautifulSoup(self.response.text, 'html.parser')

            pattern = re.compile(r"(https?)://([A-Za-z0-9\-\.]+).*")
            match = pattern.match(self.url)

            if match:
                protocol = match.group(1)
            else:

                raise Exception("Not a valid url")

            try:
                lighthouse_mobile_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + \
                    protocol + "://" + domain_name + \
                    "/&strategy=mobile&locale=en&key=" + \
                    app.config['LIGHTHOUSE_API_KEY']
                lighthouse_desktop_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + \
                    protocol + "://" + domain_name + \
                    "/&strategy=desktop&locale=en&key=" + \
                    app.config['LIGHTHOUSE_API_KEY']

                """ lighthouse_tablet_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="++ \
                    protocol + "://" + domain_name +"&emulatedFormFactor=tablet&screenEmulation.disabled=true&deviceScreenSize=768x1024&key=AIzaSyCGK9KUGoc66FjkFCiXlVY8ZTFwOJK3Fbg" """
                import json

                print(lighthouse_desktop_url)

                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = [executor.submit(requests.get, url) for url in [
                        lighthouse_mobile_url, lighthouse_desktop_url]]

                    for future in concurrent.futures.as_completed(futures):
                        response = future.result()

                        if "mobile" in response.url:
                            self.mobile_data = response.json()
                        elif "desktop" in response.url:
                            self.desktop_data = response.json()

                """ self.mobile_data = ""
                self.desktop_data = "" """
            except Exception as e:

                print("lighthous", e)

        except Exception as e:
            print("Exception\n\n")
            print(e)
            return e

    def get_url_content(self, domain):
        print("value", domain)
        urls_to_try = [
            f"https://www.{domain}",
            f"https://{domain}",
            f"http://www.{domain}",
            f"http://{domain}",
            f"{domain}"
        ]
        for url_to_try in urls_to_try:
            try:
                response = requests.get(url_to_try)
                return url_to_try, response
            except requests.exceptions.RequestException:
                pass
        raise ValueError("Invalid URL")

    def get_data_obj(self):
        data_dict = {
            "url": self.url,
            "response": {
                "status_code": self.response.status_code,
                "headers": dict(self.response.headers),
                "text": self.response.text
            },
            "mobile_data": self.mobile_data,
            "desktop_data": self.desktop_data,
        }
        return json.dumps(data_dict), str(self.url)
