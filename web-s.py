import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import json

def make_json(csvFilePath, jsonFilePath):
     
    data = []
     
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:

            key = rows['Index']
            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
 
r = requests.get('https://www.freethink.com/articles')
 
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
df.to_csv('scraped.csv', index=False, encoding='utf-8')

csvFilePath = r'scraped.csv'
jsonFilePath = r'scraped.json'
make_json(csvFilePath, jsonFilePath)


