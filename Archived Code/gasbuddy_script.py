### This script scrapes the gasbuddy website for gas stations, prices and distance from a certain geopoint
### this script was abandoned because the aaa website with data from OPISnet was found 
### this script was flawed because gasbuddy was highly protected from scraping by dynatrace and the data was imcomplete anyways

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
# import cloudscraper
import requests 
# scraper = cloudscraper.create_scraper()

# Randomly Generated Coordinates
# url = "https://www.gasbuddy.com/home?fuel=1&maxAge=0&method=&lat=42.3313&lng=-83.4656"
url = "https://www.gasbuddy.com/home?fuel=1&maxAge=0&method=&lat=42.021584&lng=-88.086376"
# "https://www.gasbuddy.com/home?fuel=1&maxAge=0&method=&lat=29.395318128257&lng=-98.838458275044"
# "https://www.gasbuddy.com/home?fuel=1&maxAge=0&method=&lat=38.384308307036&lng=-122.726771643204"
# "https://www.gasbuddy.com/home?fuel=1&maxAge=0&method=&lat=44.386328374335&lng=-69.777574640737"

req = urllib.request.Request(url, headers={'User-Agent': 'XYZ/3.0'})
html = urllib.request.urlopen(req, timeout = 10).read()
soup = BeautifulSoup(html, 'html.parser')

data = soup.find_all("div", {"class": "panel__panel___3Q2zW panel__white___19KTz colors__bgWhite___1stjL panel__bordered___1Xe-S panel__rounded___2etNE GenericStationListItem-module__station___1O4vF"})
with open("data.txt", "w") as file:
    for station in data:
        file.write(str(station.text))
        file.write("\n")

# data = soup.find_all('span', {'class': 'text__xl___2MXGo text__left___1iOw3 StationDisplayPrice-module__price___3rARL'})
# for a in data:
#     print(a.text)

# soup = BeautifulSoup(page.content, 'html.parser')

# # state = input("Input Your State ").strip() 
# title = soup.find(id="Michigan").get_text()

# price = soup.find("div", class_="col-sm-2 col-xs-3 text-right").get_text()
# print(price)
# print(title)