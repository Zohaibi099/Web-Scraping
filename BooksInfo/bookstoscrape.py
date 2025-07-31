import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Step 1: Base URL and first page
base_url = "https://books.toscrape.com/catalogue/"
current_page = "page-1.html"

# All books list
all_books = []

# Keep going while next page exists
while current_page:
    full_url = base_url + current_page
    print(f"Scraping page: {current_page}")

    response = requests.get(full_url)
    soup = BeautifulSoup(response.text, 'lxml')

    # Get all books
    books = soup.find_all("article", class_="product_pod")

    # Extract data
    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text
        stock = book.find("p", class_="instock availability").text.strip()
        all_books.append({
            'title': title,
            'price': price_text,
            'stock': stock
        })

    # Handle next button
    next_button = soup.find('li', class_='next')
    if next_button:
        next_href = next_button.find('a')['href']

        # 👇 Smart handling of base_url shift
        if 'catalogue/' not in current_page and 'catalogue/' in next_href:
            base_url = "https://books.toscrape.com/catalogue/"
        
        current_page = next_href
    else:
        current_page = None

    time.sleep(1)

# Save to Excel
df = pd.DataFrame(all_books)
df.to_excel("bookstoscrape.xlsx", index=False)
print("✅ Scraped", len(all_books), "books and saved to bookstoscrape.xlsx")
