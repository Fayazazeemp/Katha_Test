from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import pandas as pd

app = Flask(__name__)
api = Api(app)
CORS(app)

class Articles(Resource):
    def get(self):
        data = pd.read_csv('scraped.csv')  # read CSV
        data = data.to_dict()
        return {'data': data},
    pass

api.add_resource(Articles, '/')  # '/' is our entry point

if __name__ == '__main__':
    app.run() 