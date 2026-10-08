import requests
from bs4 import BeautifulSoup
import csv

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    with open("scraper_data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])

        for quote, author in zip(quotes, authors):
            writer.writerow([
                quote.get_text(strip=True),
                author.get_text(strip=True)
            ])

    print("Scraping completed successfully!")
    print(f"Total records scraped: {len(quotes)}")
else:
    print("Failed to access website.")
    print("Status code:", response.status_code)