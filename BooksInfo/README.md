# 📚 Book Info Scraper – books.toscrape.com

This mini project scrapes data from [books.toscrape.com](http://books.toscrape.com), a mock e-commerce site for books. The script extracts book titles, prices, and availability using **Python**, **Requests**, and **BeautifulSoup**, then saves the results into an Excel file.

---

## 🛠️ Tools & Libraries Used

- `Requests` – to fetch web pages
- `BeautifulSoup` – to parse HTML content
- `openpyxl / pandas` – to save the scraped data

---

## 🔍 What It Does

The script goes through the pages of the website and collects:

- 📖 Book Title  
- 💵 Price  
- ✅ Availability status  

It automatically moves to the next page until all books are scraped.

---

## 📁 Output

- ✅ **bookstoscrape.xlsx** – Excel file with scraped book data
- 🖼️ Screenshot of Output:

![Scraped Book Data](output.png)

---