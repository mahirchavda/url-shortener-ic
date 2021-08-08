import base64
import uuid
import hashlib
from flask_restful import Resource, reqparse
from flask import request

SHORT_URL_LENGTH = 7


def non_empty_string(string):
    string = string.strip()
    if not string:
        raise ValueError("Must not be empty string")
    return string


class URLShortener(Resource):
    def __init__(self, url_hash_mapping, shortener_web_server):
        self.url_hash_mapping = url_hash_mapping
        self.shortener_web_server = shortener_web_server
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            "url", required=True, type=non_empty_string, location="json"
        )
        super().__init__()

    def get_random_hash(self):
        randon_hash = str(uuid.uuid4())
        return randon_hash

    def get(self):
        short_url_hash = request.args["short_url_hash"]
        if short_url_hash in self.url_hash_mapping:
            return {"url": self.url_hash_mapping[short_url_hash]}
        else:
            return {"message": "Not able to find url for given short url"}

    def post(self):
        args = self.parser.parse_args()
        url = args["url"]
        temp_url = url.lstrip(self.shortener_web_server + "/")
        if temp_url in self.url_hash_mapping:
            return {
                "short_url": url,
                "url": self.url_hash_mapping[temp_url],
            }
        else:
            url_hash = self.get_random_hash()
            short_url = "{}/{}".format(self.shortener_web_server, url_hash)
            self.url_hash_mapping[url_hash] = url
            return {"short_url": short_url, "url": url}
