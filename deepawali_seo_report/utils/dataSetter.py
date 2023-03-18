import re
import requests
from bs4 import BeautifulSoup
import concurrent.futures
import json



class DataSetter:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, url):
        try:
            self.response = requests.get(url)
            self.url = url
            self.soup = BeautifulSoup(self.response.text, 'html.parser')

            pattern = re.compile(r"(https?)://([A-Za-z0-9\-\.]+).*")
            match = pattern.match(self.url)

            if match:
                protocol = match.group(1)
                domain_name = match.group(2)
            else:
                raise Exception("Not a valid url")

            try:
                lighthouse_mobile_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + \
                    protocol + "://" + domain_name + "/&strategy=mobile&locale=en&key=AIzaSyCGK9KUGoc66FjkFCiXlVY8ZTFwOJK3Fbg"
                lighthouse_desktop_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=" + \
                    protocol + "://" + domain_name + "/&strategy=desktop&locale=en&key=AIzaSyCGK9KUGoc66FjkFCiXlVY8ZTFwOJK3Fbg"
                
                """ lighthouse_tablet_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="++ \
                    protocol + "://" + domain_name +"&emulatedFormFactor=tablet&screenEmulation.disabled=true&deviceScreenSize=768x1024&key=AIzaSyCGK9KUGoc66FjkFCiXlVY8ZTFwOJK3Fbg" """
                import json
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    futures = [executor.submit(requests.get, url) for url in [
                        lighthouse_mobile_url, lighthouse_desktop_url]]

                    for future in concurrent.futures.as_completed(futures):
                        response = future.result()
                        if response.url == lighthouse_mobile_url:
                            self.mobile_data = response.json()
                        elif response.url == lighthouse_desktop_url:
                            self.desktop_data = response.json()

                
                """ self.mobile_data = ""
                self.desktop_data = "" """
            except Exception as e:
                print("lighthous", e)

        except Exception as e:
            print(e)
            return e

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
        return json.dumps(data_dict)
