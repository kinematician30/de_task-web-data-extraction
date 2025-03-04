import pandas as pd
import requests  # make a request to retrieve the page
from bs4 import BeautifulSoup  # html parser

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
# Extracting all hotel listing flex
hotel_listing = parsed_page.find_all('div', class_="listing-hotels")

# Scraping and transformation of the unstructured data
all_hotels_listing = []
for listing in hotel_listing:
    hotel_name = listing.find('h2', class_="listing-hotels-name").text
    hotel_address = listing.find('p',
                                 class_='listing-hotels-address color-dark').text.strip().split()
    hotel_address = " ".join(hotel_address).split(' - ')
    address = hotel_address[1]
    city = hotel_address[0].split(',')[0]
    state = hotel_address[0].split(',')[1].strip()
    price = listing.find('p', class_='listing-hotels-prices-discount').text
    price = price.strip().split()[0].replace('₦', '').replace(',', '')
    rated = listing.find('p', class_='listing-hotels-rating')
    if rated is None:
        rating = "Not Available"
        index = "No Index"
    else:
        rating = rated.text.split(' - ')[0]
        index = rated.text.split(' - ')[1]
    facility = listing.find('div',
                            class_='listing-hotels-facilities d-none d-md-flex')
    if facility is None:
        all_facilities = "No facilities recorded"
    else:
        all_facilities = facility.find_all()
        all_facilities = [fac.find('p').text for fac in all_facilities if fac.find('p') is not None]
        all_facilities = ", ".join(all_facilities)
    likes = listing.find('div', class_='listing-hotels-likes').text
    likes = likes.strip().split()[0]

    # Finally Transformed data for temporary storage
    hotels_listing = {
        'hotel_name': hotel_name,
        'hotel_address': address,
        'city': city,
        'state': state,
        'price_per_night': price,
        'rating_score': rating,
        'rating_index': index,
        'facilities': all_facilities,
        'popularity': likes
    }
    all_hotels_listing.append(hotels_listing)

df_hotel = pd.DataFrame(all_hotels_listing)  # Convert to dataframe
df_hotel.to_csv("hotels.csv")  # save to csv
