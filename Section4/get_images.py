#!/usr/bin/env python3

import os
import requests
from lxml import html

class Scraping:

    def scrapingImages(self,url):
        print("\nGetting images from url:"+ url)
        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            images = parsed_body.xpath('//img/@src')
            print('Found images %s', len(images))

            os.system("mkdir images")


            for image in images:
                if image.startswith("http") == False:
                    download = url +"/" +image
                else:
                    download = image
                print(download)

                r = requests.get(download)
                f = open('images/%s' % download.split('/')[-1],'wb')
                f.write(r.content)
                f.close()

        except Exception as e:
            print("Connection error in" + url)
            pass

    def scrapingLinks(self, url):
        print("\nGetting links from url:" + url)

        try:
            response = requests.get(url)
            parsed_body = html.fromstring(response.text)

            links = parsed_body.xpath('//a/@href')

            print('Found links %s' % len(links))

            for link in links:
                print(link)

        except Exception as e:
            print("Connection error in  " + url)
            pass


if __name__ == '__main__':
    target = "https://youtube.com"
    scraping = Scraping()
    scraping.scrapingImages(target)
    scraping.scrapingLinks(target)











