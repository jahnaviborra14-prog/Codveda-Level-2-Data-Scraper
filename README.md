# Codveda Level 2 - Data Scraper

## Project Description

This project is a Python-based web scraper developed as part of the Codveda Python Development Internship.

The scraper collects quotes and their corresponding authors from the "Quotes to Scrape" website and stores the extracted data in a CSV file.

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV

## Features

- Sends HTTP requests to the target website
- Extracts quotes from webpages
- Extracts corresponding author names
- Stores scraped data in CSV format
- Successfully scrapes 10 records
- Provides structured and reusable Python code

## Project Structure

```text
Codveda-Level-2-Data-Scraper/
│
├── scraper.py
├── scraper_data.csv
├── requirements.txt
├── README.md
└── LICENSE
## Installation

1. Install Python 3 on your system.
2. Open a terminal in the project folder.
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## How to Run

Run the following command in the terminal:

```bash
python scraper.py
```

The scraper collects quotes and author names from Quotes to Scrape and saves the results in `scraper_data.csv`.

## Expected Output

```text
Scraping completed successfully!
Total records scraped: 10
Data saved to: scraper_data.csv
```
