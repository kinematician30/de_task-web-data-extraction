Absolutely—here’s a clean, professional **README.md** you can use for this hotel scraper script:

---

# 🏨 Hotels.ng Web Scraper

This Python script scrapes hotel listings from [hotels.ng](https://hotels.ng) in Nigeria, extracting details like name, address, pricing, facilities, ratings, and popularity.

---

## 📋 Overview

The scraper performs the following steps:

1. **Connects** to the hotels.ng Abia hotels listing pages.
2. **Parses** each hotel’s data (name, address, price, ratings, facilities, popularity).
3. **Handles pagination** to scrape multiple pages automatically.
4. **Stores** all results in a CSV file (`hotels.csv`) for analysis.

---

## ⚙️ Requirements

* Python 3.x
* The following Python packages:

```bash
pip install pandas requests beautifulsoup4
```

---

## 🛠️ How to Run

1. Save the script to a `.py` file, e.g., `scrape_hotels.py`.
2. Open a terminal in the script’s directory.
3. Run:

```bash
python scrape_hotels.py
```

4. When completed, check `hotels.csv` in the same folder.

---

## 🧩 Script Breakdown

### 1️⃣ Fetch HTML Content

**Function:** `get_html_content(url, headers)`

* Sends an HTTP GET request to the specified URL.
* Returns HTML if successful.

---

### 2️⃣ Parse Hotel Listings

**Function:** `parse_hotel_listings(html_content)`

* Locates all hotel listing blocks on the page using BeautifulSoup.

---

### 3️⃣ Extract Hotel Data

**Function:** `extract_hotel_data(listing)`

For each hotel, extracts:

* **Hotel Name**
* **Address, City, State**
* **Price per Night**
* **Rating Score and Index**
* **Facilities**
* **Popularity (Likes)**

Handles missing data gracefully.

---

### 4️⃣ Handle Pagination

**Function:** `get_next_page_url(html_content)`

* Detects the “Next” button link to scrape additional pages automatically.

---

### 5️⃣ Save Data to CSV

At the end of scraping:

* All collected data is saved to `hotels.csv`.

---

## ✨ Example Output

Example CSV columns:

| hotel\_name       | hotel\_address  | city    | state | price\_per\_night | rating\_score | rating\_index | facilities                     | popularity |
| ----------------- | --------------- | ------- | ----- | ----------------- | ------------- | ------------- | ------------------------------ | ---------- |
| Grand Royal Hotel | 123 Main Street | Umuahia | Abia  | 15000             | 8.4           | Very Good     | Free WiFi, Restaurant, Parking | 12         |

---

## 💡 Notes

* **Politeness**: Includes a 2-second delay between pages to avoid overloading the server.
* **User-Agent**: A modern User-Agent header is used to avoid blocking.
* **Error Handling**: Skips any listings with missing fields.

---

## 🚀 Customization

To scrape a different state, edit the `base_url` in the `main()` function:

```python
base_url = "https://hotels.ng/hotels-in-lagos"
```

Replace `lagos` with any valid state slug.

---

## 🙌 Author

Created by \[Your Name].

Feel free to extend or modify this scraper for your projects!

---

Let me know if you’d like help tailoring this further!
