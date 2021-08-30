import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import requests
import csv

req = urllib.request.Request("https://gasprices.aaa.com/state-gas-price-averages/", headers={'User-Agent': 'Murphy/4.23'})
html = urllib.request.urlopen(req, timeout = 10).read()
soup = BeautifulSoup(html, "html.parser")

data = soup.find_all("td", {"class": "regular"})

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut", "District of Columbia", "Delaware",
"Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
"Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey",
"New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
"South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

with open("average_prices_state.txt", "w") as file:
    csvwriter = csv.writer(file)
    for idx, price in enumerate(data):
        csvwriter.writerow([states[idx], str(price.text).strip()])