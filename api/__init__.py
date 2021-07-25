import os
from flask import Flask
from flask_restful import Api
from .endpoints.url_shortener import URLShortener

app = Flask(__name__)
api = Api(app)

url_hash_mapping = {}
shortener_web_server = os.environ["SHORTENER_WEB_SERVER"].strip().strip("/")

api.add_resource(
    URLShortener,
    "/api/shorten",
    resource_class_args=(url_hash_mapping, shortener_web_server),
)
