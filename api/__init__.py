from flask import Flask
from flask_restful import Api
from .endpoints.url_shortener import URLShortener

app = Flask(__name__)
api = Api(app)


api.add_resource(URLShortener, "/api/shorten")
