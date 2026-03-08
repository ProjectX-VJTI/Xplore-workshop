# Web Communication: REST, GraphQL, and Scraping
# ----------------------------------------------
# requests: The industry standard for making HTTP requests.
# BeautifulSoup: A library for pulling data out of HTML and XML files.

import requests
from bs4 import BeautifulSoup
import json

# 1. REST API (GET Request)
# REST (Representational State Transfer) uses standard HTTP methods.
# We'll use JSONPlaceholder, a free fake API.

print("--- 1. REST API (JSONPlaceholder) ---")
rest_url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(rest_url)

if response.status_code == 200:
    data = response.json()
    print(f"Title: {data['title']}")
else:
    print("Failed to fetch REST data")


# 2. GraphQL API (POST Request)
# Unlike REST, GraphQL uses a single endpoint and you "ask" for specific data.
# We'll use the public Countries API.

print("\n--- 2. GraphQL API (Countries) ---")
graphql_url = "https://countries.trevorblades.com/"
query = """
{
  country(code: "IN") {
    name
    native
    capital
    emoji
    currency
  }
}
"""

# GraphQL requests are usually POST requests with the query in the JSON body
response = requests.post(graphql_url, json={'query': query})
if response.status_code == 200:
    country_data = response.json()['data']['country']
    print(f"Name: {country_data['name']} {country_data['emoji']}")
    print(f"Capital: {country_data['capital']}")
    print(f"Currency: {country_data['currency']}")


# 3. Web Scraping with BeautifulSoup
# Scrapes static HTML. We'll scrape a simple quotes site.

print("\n--- 3. Web Scraping (Quotes to Scrape) ---")
scrape_url = "http://quotes.toscrape.com/"
page = requests.get(scrape_url)
soup = BeautifulSoup(page.content, 'html.parser')

# Finding all quote spans with class 'text'
quotes = soup.find_all('span', class_='text', limit=3)

for i, quote in enumerate(quotes, 1):
    print(f"Quote {i}: {quote.text}")