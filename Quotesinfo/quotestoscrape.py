'''In this mini project i am trying to scrape quotes along with author and tags
 while also doing pagination and saving that to an excel file'''

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

# Start URL is page 1
base_url = 'http://quotes.toscrape.com'
current_page = '/page/1/'

# We will store all quotes in this list
all_quotes = []

# Keep going while there are more pages
while current_page:
    print(f"Scraping page: {current_page}")  # ✅ Inside the loop
    # Get the full page HTML
    response = requests.get(base_url + current_page)
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all quote blocks
    quote_blocks = soup.find_all('div', class_='quote')

    # Go through each quote block
    for quote in quote_blocks: 
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        tags = [tag.text for tag in quote.find_all('a', class_='tag')]

        # Save this quote’s data
        all_quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    # Find the "Next" button to go to next page
    next_button = soup.find('li', class_='next')
    if next_button:
        current_page = next_button.find('a')['href']  # e.g., /page/2/
    else:
        current_page = None  # No more pages

    time.sleep(1)  # Slow down to avoid hitting server too fast

# Print the result

print(f"Scraped {len(all_quotes)} quotes!")

df = pd.DataFrame(all_quotes)
df.to_excel("quotestoscrape.xlsx", index=False)
print("✅ Saved to quotestoscrape.xlsx")