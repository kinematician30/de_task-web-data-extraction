from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setting option for headers
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36q (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
opt = Options()
opt.add_argument(header)
opt.add_argument('--headless')  # do not open a browser!

# Set up Selenium WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=opt)

driver.get("https://hotels.ng/hotels-in-abia")  # Load the page
page = driver.page_source
print(page)