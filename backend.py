from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import pandas as pd
import os
import json

app = Flask(__name__)
api = Api(app)
CORS(app)


class Articles(Resource):
    def get(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT,'scraped.json')
        data = json.load(open(json_url))
        return {'data': data},
    pass

api.add_resource(Articles, '/')  # '/' is our entry point

if __name__ == '__main__':
    app.run() 