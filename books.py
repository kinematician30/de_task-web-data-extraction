import pandas as pd
import requests
from bs4 import BeautifulSoup

target_url = "https://books.toscrape.com/"

# get the web page or gain access to the web page
response = requests.get(target_url)
content = response.content

# parse the content of our response
parsed = BeautifulSoup(content, "html.parser")

# Crawl and Extract
books = []  # storage for our extracted info

# converter
word_to_num = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
}

targets = parsed.find('ol', class_="row")

article = targets.find_all('article', class_="product_pod")
for target in article:
    title = target.find('h3').find('a').attrs['title']
    star_rating = word_to_num[target.find('p').attrs['class'][-1]]
    price = target.find('p', class_='price_color').text[1:]
    record = {
        "Title": title,
        "Rating": star_rating,
        "Price": price
    }
    print(record)
    # save it in a storage
    books.append(record)

data = pd.DataFrame(books, columns=["Title", "Rating", "Price"])
data.to_csv("..\\assignmnet\\Extracted.csv", index=False)
print("Done!")

print(data.head(10))

# Save to file
# columns_name = ['Title', 'Star Rating', 'Price']
# with open("extracted.csv", mode='w') as file:
#     csvwriter = csv.writer(file)
#     csvwriter.writerow(columns_name)
#     csvwriter.writerows(books)
#     print('Done Closing the file now!')

# with open("extracted.csv", mode='r') as file:
#     f = file.read()
#     print(f)

# Assignment.
# Give me in this format
# 1,A Light in the Attic,3.0,51.77(float)
