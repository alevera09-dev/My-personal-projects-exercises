# -*- coding: utf-8 -*-
"""
Created on Sun Oct  5 10:43:58 2025

@author: alesa
"""

"""
Touch Scraper
"""


import requests as req
from bs4 import BeautifulSoup as BS
import random as ran


def scrapeWikiArticle(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'}
    response = req.get(url=url, headers=headers) #(url, User-Agent)

    soup = BS(response.content, 'html.parser')
    title = soup.find(id='firstHeading')

    print(title.string)

    #obtener todos los tags
    allLinks = soup.find(id="bodyContent").find_all("a")
    ran.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # Solo estamos interesados en otros articulos wiki
        if link['href'].find("/wiki/") == -1: 
            continue

        # Usar este enlace para raspar/scrape
        linkToScrape = link
        break
    
    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

scrapeWikiArticle("https://en.wikipedia.org/wiki/Web_scraping")