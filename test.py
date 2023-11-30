from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

# Set the URL of the web page
url = "https://zefoy.com"

# Open the web page in a Chrome browser
driver = webdriver.Chrome()
driver.get(url)

# Wait for the page to load
driver.implicitly_wait(10)

# Get the HTML source of the page
html = driver.page_source

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Remove the elements containing ads
for ad in soup.select(".ad"):
    ad.decompose()

# Save the modified HTML
modified_html = str(soup)

# Overwrite the HTML of the web page with the modified HTML
driver.execute_script(f"document.documentElement.innerHTML = {modified_html!r}")
sleep(10)
# Close the browser
driver.close()
