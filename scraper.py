
import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup


URL = "https://quotes.toscrape.com/"
OUTPUT_FILE = Path(__file__).with_name("scraper_data.csv")


def scrape_quotes():
    """Scrape quotes and authors from the target website."""
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    data = []

    for quote, author in zip(quotes, authors):
        data.append({
            "Quote": quote.get_text(strip=True),
            "Author": author.get_text(strip=True),
        })

    return data


def save_to_csv(data):
    """Save scraped data to a CSV file."""
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Quote", "Author"])
        writer.writeheader()
        writer.writerows(data)


def main():
    try:
        data = scrape_quotes()
        save_to_csv(data)

        print("Scraping completed successfully!")
        print(f"Total records scraped: {len(data)}")
        print(f"Data saved to: {OUTPUT_FILE}")

    except requests.RequestException as error:
        print("Failed to access the website.")
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
