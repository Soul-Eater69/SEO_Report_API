import re
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
import re
import os
from deepawali_seo_report import app


class SocialUtil:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, soup_obj):
        self.url = soup_obj["url"]
        self.response = soup_obj["response"]
        self.soup = BeautifulSoup(self.response["text"], "html.parser")
        self.data = soup_obj["desktop_data"]

    def has_facebook(self):
        soup = self.soup
        # define a regular expression pattern to match Facebook Page links
        fb_pattern = re.compile(
            r'(https?://)?(www\.)?(facebook\.com|fb\.com)/[a-zA-Z0-9.-]+/?')

        # find all links on the webpage
        links = soup.find_all('a')

        # loop through the links and check if any of them match the Facebook Page link pattern
        for link in links:
            try:
                if fb_pattern.match(link.get('href')):
                    return True
            except:
                continue
        else:
            return False

    def get_open_graphs(self):
        soup = self.soup
        res = []
        meta_tags = soup.find_all("meta")
        for tag in meta_tags:
            try:
                if tag.has_attr("property") and tag.attrs['property'].startswith('og:'):
                    res.append(
                        {"property": tag.attrs["property"], "content": tag.attrs["content"]})
            except:
                continue

        return res

    def get_facebook_pixel(self):
        script_tags = self.soup.find_all('script')

        # loop through the script tags and check if any of them contain the Facebook Pixel code
        for tag in script_tags:
            try:
                if 'fbq' in str(tag):
                    return True
            except:
                continue
        return False

    def has_twitter(self):
        twitter_profile = False
        links = self.soup.find_all("a")
        for link in links:
            try:
                if 'twitter.com/' in link.get('href'):
                    twitter_profile = True
                    break
            except:
                continue

        # print the result
        if twitter_profile:
            return True
        else:
            return False

    def get_twitter_cards(self):
        twitter_cards = self.soup.find_all(
            'meta', {'name': lambda name: name and name.startswith('twitter:')})
        # loop through the Twitter Cards metadata and print the tag and content attributes
        cards = []

        for tc in twitter_cards:
            try:
                tag = tc.get('name')
                content = tc.get('content')
                cards.append({"tag": tag, "content": content})
            except:
                continue

        return cards

    def has_instagram(self):
        links = self.soup("a")
        for link in links:
            try:
                if 'instagram.com' in link.get('href'):
                    return True
            except:
                continue

        return False

    def has_linkedin(self):
        links = self.soup("a")
        for link in links:
            try:
                if 'linkedin.com' in link.get('href'):
                    return True
            except:
                continue

        return False

    def get_youtube_data(self):

        links = self.soup.find_all('a')

        youtube_link = False

        # loop through the links and check if any of them are social media links
        for link in links:
            try:
                if 'youtube.com' in link.get('href'):
                    youtube_link = link.get('href')
            except:
                continue

        try:
            # check if a YouTube link was found
            if youtube_link:

                api_key = app.config["YOUTUBE_API_KEY"]

                # authenticate with the YouTube Data API using the API key above
                youtube = build('youtube', 'v3', developerKey=api_key)

                # replace with the URL of the YouTube channel you want to check
                channel_url = youtube_link

                # extract the channel's username or ID from the URL
                channel_username = re.search(
                    r'youtube\.com/(?:user|c|@)/([^/]+)', channel_url)
                channel_id = re.search(
                    r'youtube\.com/channel/([^/]+)', channel_url)

                if channel_username:
                    # if the URL contains the channel's username
                    channel_username = channel_username.group(1)

                    # use the YouTube Data API to search for channels with the given username
                    search_response = youtube.search().list(
                        type='channel',
                        q=channel_username,
                        part='id'
                    ).execute()

                    # get the channel ID from the search results
                    channel_id = search_response['items'][0]['id']['channelId']
                elif channel_id:
                    # if the URL contains the channel's ID
                    channel_id = channel_id.group(1)
                else:
                    raise ValueError('Invalid channel URL')

                # use the YouTube Data API to get the channel statistics
                channel_stats = youtube.channels().list(
                    part='statistics', id=channel_id).execute()

                # get the number of subscribers and views for the channel
                subscribers = channel_stats['items'][0]['statistics']['subscriberCount']
                views = channel_stats['items'][0]['statistics']['viewCount']

                return {'hasYoutube': youtube_link,
                        "hasData": True,
                        'subscribers': subscribers,
                        'views': views,
                        }
        except Exception as e:
            return {'hasYoutube': youtube_link,
                    "hasData": False,
                    'subscribers': 0,
                    'views': 0,
                    }

        return {'hasYoutube': "",
                "hasData": False,
                'subscribers': 0,
                'views': 0,
                }
