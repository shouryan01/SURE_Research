from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv
import itertools
from numpy import random
from time import sleep

url = "https://michigan.aaa.com/Safety/fuel-finder-redirect.aspx"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
# options.add_argument('user-agent=')
driver = webdriver.Chrome('./chromedriver', chrome_options = options)
driver.get(url)
time.sleep(2)

def get_data(zip):
    text_input = driver.find_element(By.NAME, "ctl00$ContentPlaceHolder1$aaaSearch$txtZipCode")
    text_input.clear()
    text_input.send_keys(zip + Keys.ENTER)
    html = driver.page_source


    soup = BeautifulSoup(html, "html.parser")
    station_name = soup.find_all("a", id = lambda x: x and x.endswith("StationName"))
    station_brand = soup.find_all("span", id = lambda x: x and x.endswith("StationBrandName"))
    station_address = soup.find_all("a", id = lambda x: x and x.endswith("StationAddress"))
    station_city_state = soup.find_all("span", id = lambda x: x and x.endswith("StationCityState"))
    station_price = soup.find_all("span", id = lambda x: x and x.endswith("UnlPrice"))
    
    # a
    # span
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl02_StationName
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl02_StationBrandName
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl02_StationAddress
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl02_StationCityState
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl02_UnlPrice

    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl03_StationName
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl03_StationBrandName
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl03_StationAddress
    # ctl00_ContentPlaceHolder1_searchResults_stationList_gvResults_ctl15_StationName

    # data = soup.find_all("td")
    # for a in data:
    #     print(a.text)


    with open("wj.csv", "a") as output_file:
        csvwriter = csv.writer(output_file)

        for (name, brand, address, city, price) in itertools.zip_longest(station_name, station_brand, station_address, station_city_state, station_price, fillvalue = "NA"):
            csvwriter.writerow([name.text, brand.text, str(address.text + ", " + city.text), price.text])
    
ny = [11368, 11369, 11372, 11373, 11374, 11375, 11354, 11355, 11367, 11370, 11356]
la = [90011, 90001, 90058, 90028, 90255, 90002, 90003, 90023, 90270, 90278, 90044]
ch = [60629, 60707, 60607, 60634, 60171, 60160, 60165, 60659, 60164, 60131, 60645]
ho = [77084, 77024, 77002, 77069, 77054, 77021, 77051, 77027, 77033, 77081, 77045]
px = [85003, 85339, 85045, 85048, 85041, 85040, 85044, 85253, 85015, 85226, 85034]

wc = [67202, 67214, 67213, 67211, 67218, 67203, 67217, 67206, 67208, 67212, 67209]
ta = [98402, 98403, 98405, 98406, 98407, 98421, 98465, 98466, 98422, 98408, 98404]
pp = [33026, 33321, 33071, 33025, 33324, 33319, 33068, 33313, 33312, 33351, 33328]
cn = [29401, 29403, 29412, 29414, 29405, 29482, 29423, 29455, 29439, 29464, 29407]
wj = [84088, 84084, 84095, 84118, 84119, 84006, 84047, 84123, 84065, 84070, 84094]

ca = [48187, 48154, 48150, 48167, 48170, 48152, 48185, 48135, 48335, 48186 ,48125]

sleeptime = random.uniform(2, 4)

for zipcode in wj:
    print("~")
    print(zipcode)
    print("~")
    sleep(sleeptime)
    get_data(str(zipcode))
    sleep(sleeptime)
    print("~")


# all_divs = soup.find('div', {'id' : 'nameSearch'})
# job_profiles = all_divs.find_all('a')
  
# # printing top ten job profiles
# count = 0
# for job_profile in job_profiles :
#     print(job_profile.text)
#     count = count + 1
#     if(count == 10) :
#         break
  
# driver.close() # closing the webdriver