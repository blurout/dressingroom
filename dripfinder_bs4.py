''' 
Dressing Room Web Scraper

Fall 2022

version 0.0.1

This script scrapes the web for desirable fashion items on sale.
Current version is testing requests from ssense.com
'''

import bs4 as bs
import urllib.request


file = open('links.txt', 'r')
links = file.readlines()
for link in links:
    #initialize our request to look legit
    req = urllib.request.Request (
        link,
        data = None,
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
        }
    )
    # set up source variable using our request to get the ugly soup
    source = urllib.request.urlopen(req).read()
    # make the soup beautiful
    soup = bs.BeautifulSoup(source, 'lxml')
    # print price of specific listing, ex: yeezy 450
    print(soup.find(class_="pdp-product-price__price s-text").string)
file.close()
