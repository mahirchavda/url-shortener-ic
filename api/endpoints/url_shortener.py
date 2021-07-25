import base64
import hashlib
from flask_restful import Resource, reqparse

SHORT_URL_LENGTH = 7


class URLShortener(Resource):
    def __init__(self, url_hash_mapping, shortener_web_server):
        self.url_hash_mapping = url_hash_mapping
        self.shortener_web_server = shortener_web_server
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("url", required=True, location="json")
        super().__init__()

    def get_url_hash(self, url):
        md5_hash = hashlib.md5(url.encode("utf-8")).digest()
        url_hash = base64.urlsafe_b64encode(md5_hash).decode("ascii")
        return url_hash[:SHORT_URL_LENGTH]

    def post(self):
        args = self.parser.parse_args()
        url = args["url"]
        if url in self.url_hash_mapping:
            url_hash = self.url_hash_mapping[url]
            short_url = "{}/{}".format(self.shortener_web_server, url_hash)
        else:

            url_hash = self.get_url_hash(url)
            self.url_hash_mapping[url] = url_hash
            short_url = "{}/{}".format(self.shortener_web_server, url_hash)

        response = {"short_url": short_url, "url": url}
        return response
