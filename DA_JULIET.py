import requests
# Set the target webpage
url = "http://172.18.58.238/headers.php"
r = requests.get(url)
# This will get the full page
print(r.text)
print("Status code:")
print("\t OK", )
# This will just get just the headers
h = requests.head(url)
print("Header:")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
import requests
h = {"User-Agent": "mobile"}
r = requests.get("http://172.18.58.238/headers.php", headers = h)
print (r.content)

import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ["http://172.18.58.238/multi/"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
                 newsel = '@src'
                 yield {
                     'Image Link': x.xpath(newsel).extract_first(),
                 }

        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),callback=self.parse)

import unittest
import os
class TestMyProgram(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\Lim kai jun\\Documents\\DA_JULIET\\PY_Project\\scrapy.py")
        os.system("C:\\Users\\Lim kai jun\\Documents\\DA_JULIET\\PY_Project\\requests.py")

    if __name__ == "_main_":
        unittest.main()
