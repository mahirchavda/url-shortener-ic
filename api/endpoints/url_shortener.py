from flask_restful import Resource, reqparse


class URLShortener(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("url", required=True, location="json")
        super().__init__()

    def post(self):
        args = self.parser.parse_args()
        response = {"short_url": "", "url": args["url"]}
        return response
