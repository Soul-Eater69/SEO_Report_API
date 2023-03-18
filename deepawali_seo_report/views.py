from . import app
import json
from flask import request, jsonify
from flask_restful import Resource
from .utils.dataSetter import DataSetter
from .utils.performance_util import PerformanceUtil
from .utils.usage_utils import UsabilityUtil
from .utils.on_page_seo_utils import OnPageSEOUtil
from flask_caching import Cache
from .utils.organizers.on_page_seo_organizer import seoOrganizer
from .utils.organizers.usability_organizer import usabilityOrganizer
from .utils.organizers.performance_organizer import performanceOrganizer

cache = Cache(config={'CACHE_TYPE': 'SimpleCache',
              'CACHE_DEFAULT_TIMEOUT': 3600})
cache.init_app(app)


class Setup(Resource):
    def post(self):
        url = request.get_json()["url"]
        cached_url = cache.get('url')
        print(cache.get('url'),url)
        if cached_url is None or cache.get('url') != url:
            print("Not cached")
            data_setter = DataSetter(url)
            soup_obj = data_setter.get_data_obj()

            cache.set('soup_obj', soup_obj)
            cache.set('url', url)
        return jsonify({"status": 'URL set'})


class OnPageSEO(Resource):
    def get(self):
        cached_soup = cache.get('soup_obj')

        if cached_soup is None:
            return jsonify({"status": 'URL not set'})

        soup_obj = json.loads(cache.get('soup_obj'))
        on_page_seo_obj = OnPageSEOUtil(soup_obj)
        organized_data = seoOrganizer(on_page_seo_obj)

        return organized_data


class Usability(Resource):
    def get(self):
        cached_soup = cache.get('soup_obj')

        if cached_soup is None:
            return jsonify({"status": 'URL not set'})

        soup_obj = json.loads(cache.get('soup_obj'))
        usability_obj = UsabilityUtil(soup_obj)
        organized_data = usabilityOrganizer(usability_obj)

        return organized_data

class Performance(Resource):
    def get(self):
        cached_soup = cache.get('soup_obj')

        if cached_soup is None:
            return jsonify({"status": 'URL not set'})

        soup_obj = json.loads(cache.get('soup_obj'))
        performance_obj = PerformanceUtil(soup_obj)
        organized_data = performanceOrganizer(performance_obj)

        return organized_data