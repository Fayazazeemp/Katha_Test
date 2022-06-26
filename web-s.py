import requests
from bs4 import BeautifulSoup
import pandas as pd
 
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

df = pd.DataFrame({'Title':title_list,'Link':refined_link,'Image':images_list}) 
df.to_csv('scraped.csv', index=False, encoding='utf-8')


