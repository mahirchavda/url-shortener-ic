import base64
import hashlib
from flask_restful import Resource, reqparse

SHORT_URL_LENGTH = 7
SHORTENER_WEB_SERVER = "https://abc.com"


class URLShortener(Resource):
    def __init__(self):
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
        url_hash = self.get_url_hash(url)
        short_url = "{}/{}".format(SHORTENER_WEB_SERVER, url_hash)
        response = {"short_url": short_url, "url": url}
        return response
