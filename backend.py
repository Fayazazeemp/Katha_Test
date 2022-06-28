from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

app = Flask(__name__)
api = Api(app)
CORS(app)

def make_json(csvFilePath, jsonFilePath):
     
    data = []
     
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:

            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
 

def make_csv(url,csvFilePath):
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, 'html.parser')

    title_list = []

    for div in soup.findAll('div', attrs={'class':'flex-grow w-2/3 pl-8 loop-item__content'}):
        title_list.append(div.find('a').contents[0])

    link_list = []

    for link in soup.find_all('a'):
        links = link.get('href')
        link_list.append(links)

    refined_link = []

    for i in range(15,54,2):
        refined_link.append(link_list[i])

    images_list = []
    
    images = soup.select('img')
    for image in images:
        src = image.get('src')
        images_list.append(src)

    index = []
    for i in range(0,len(title_list)):
        index.append(i)

    df = pd.DataFrame({'Index':index,'Title':title_list,'Link':refined_link,'Image':images_list}) 
    df.to_csv(csvFilePath, index=False, encoding='utf-8')

class Articles(Resource):
    def get(self):
        SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
        json_url = os.path.join(SITE_ROOT,'scraped.json')
        data = json.load(open(json_url))
        return {'data': data},
    pass

api.add_resource(Articles, '/')  # '/' is our entry point

if __name__ == '__main__':
    csvFilePath = r'scraped.csv'
    jsonFilePath = r'scraped.json'
    url = 'https://www.freethink.com/articles'

    make_csv(url, csvFilePath)
    make_json(csvFilePath, jsonFilePath)
    
    app.run()
