#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import urllib.parse
import  sys
import  os

response = requests.get('http://www.freeimages.co.uk/galleries/transtech/informationtechnology/index.htm')
parse = BeautifulSoup(response.text,'lxml')

image_tags = parse.find_all('img')

images = [url.get('src') for url in image_tags]

if not images:
    sys.exit("No Images Man")

images = [urllib.parse.urljoin(response.url, url) for url in images]
print('Found %s images' % len(images))

file_path = "download_images"
directory = os.path.dirname(file_path)

if not os.path.exists(directory):
    try:
        os.makedirs(file_path)
        print("Creation of a directory %s OK" % file_path)
    except OSError:
        print("Creation of directory %s failed" % file_path)
else:
    print("The directory alreasy exists")

for url in images:
    response = requests.get(url)
    file = open('download_images/%s' % url.split('/')[-1], 'wb')
    file.write(response.content)
    file.close()
    print('Download %s' % url)







