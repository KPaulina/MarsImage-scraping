import requests
from bs4 import BeautifulSoup
import os

url = 'https://marshemispheres.com/'

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
soup = soup.find(id='product-section')

link_endings = []
images = []

for link in soup.find_all('a'):
    link_endings.append(link.get('href'))


for ending in set(link_endings):
    r = requests.get(f"{url}{ending}", headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        href_links = link.get('href')
        if href_links.endswith('jpg'):
            images.append(href_links)


for image in images:

    with open(image.replace('/', '_'), 'wb') as f:
        im = requests.get(f"{url}{image}", headers=headers)
        f.write(im.content)
