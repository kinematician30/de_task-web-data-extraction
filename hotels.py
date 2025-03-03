import requests # make a request to retrieve the page
from bs4 import BeautifulSoup # html parser
import pandas as pd

base_url = "https://hotels.ng/hotels-in-abia"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36q (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

print("Connecting..")
response_page = requests.get(base_url, headers=header)

if response_page.status_code == 200:
    print("Connected Successfully")
else:
    print("Connection not successful!")

# To parse the html page...
parsed_page = BeautifulSoup(response_page.text, 'html.parser')

hotel_listing = parsed_page.find_all('div', class_="listing-hotels")

for listing in hotel_listing:
    hotel_name = listing.find('h2', class_="listing-hotels-name").text
    print(hotel_name)
