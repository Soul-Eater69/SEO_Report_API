from . import app
import json
import jwt
import datetime
from urllib.parse import urlparse
from flask import request, jsonify, Response
from flask_httpauth import HTTPBasicAuth
from functools import wraps
from flask_restful import Resource
from .database.models import User
from .utils.dataSetter import DataSetter
from .utils.performance_util import PerformanceUtil
from .utils.usage_utils import UsabilityUtil
from .utils.on_page_seo_utils import OnPageSEOUtil
from .utils.social_utils import SocialUtil
from flask_caching import Cache
from .utils.organizers.on_page_seo_organizer import seoOrganizer
from .utils.organizers.usability_organizer import usabilityOrganizer
from .utils.organizers.performance_organizer import performanceOrganizer
from .utils.organizers.social_organizer import socialOrganizer

cache = Cache(config={'CACHE_TYPE': 'SimpleCache',
              'CACHE_DEFAULT_TIMEOUT': 3600})
cache.init_app(app)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]

        if not token:
            return {"message": "Token Missing"}

        try:
            data = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except Exception as e:
            print(e)
            return {"message": "Invalid Token"}

        return f(*args, **kwargs)

    return decorated


class Users(Resource):

    def put(self):
        data = request.get_json()

        user_name = data["userName"]
        password = data["password"]

        print(user_name, password)
        try:
            User(user_name=user_name, password=password).save()
        except Exception as e:
            return str(e)


class Login(Resource):
    def post(self):
        auth_header = None

        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"].split(" ")[1]

            username = auth_header.split("-")[0]
            password = auth_header.split("-")[1]

        print(username, password)
        user = User.objects.get(user_name=username)

        if user and user.password == password:
            token = jwt.encode(
                {'user': username, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config["SECRET_KEY"], algorithm="HS256")

            return {"token": token}

        else:
            return jsonify({"message": "Invalid Credentials"})


class Setup(Resource):

    @token_required
    def post(self):
        domain = request.get_json()["domainName"]
        print(domain)
        cached_domain = cache.get('domain')
        if cached_domain is None or cached_domain != domain:
            data_setter = DataSetter(domain)
            soup_obj, url = data_setter.get_data_obj()
            cache.set('soup_obj', soup_obj)
            cache.set('domain', domain)
            cache.set("url", url)
        return jsonify({"status": 'URL set', "url": cache.get("url")})


class OnPageSEO(Resource):

    @token_required
    def get(self):
        cached_soup = cache.get('soup_obj')

        if cached_soup is None:
            return jsonify({"status": 'URL not set'})

        soup_obj = json.loads(cache.get('soup_obj'))
        on_page_seo_obj = OnPageSEOUtil(soup_obj)
        organized_data = seoOrganizer(on_page_seo_obj)

        return organized_data


class Usability(Resource):

    @token_required
    def get(self):
        cached_soup = cache.get('soup_obj')

        if cached_soup is None:
            return jsonify({"status": 'URL not set'})

        soup_obj = json.loads(cache.get('soup_obj'))
        usability_obj = UsabilityUtil(soup_obj)
        organized_data = usabilityOrganizer(usability_obj)

        return organized_data


class Performance(Resource):

    @token_required
    def get(self):
        cached_soup = cache.get('soup_obj')

        if cached_soup is None:
            return jsonify({"status": 'URL not set'})

        soup_obj = json.loads(cache.get('soup_obj'))
        performance_obj = PerformanceUtil(soup_obj)
        organized_data = performanceOrganizer(performance_obj)

        return organized_data


class Social(Resource):

    @token_required
    def get(self):
        cached_soup = cache.get('soup_obj')

        if cached_soup is None:
            return jsonify({"status": 'URL not set'})

        soup_obj = json.loads(cache.get('soup_obj'))
        social_obj = SocialUtil(soup_obj)
        organized_data = socialOrganizer(social_obj)

        return organized_data
