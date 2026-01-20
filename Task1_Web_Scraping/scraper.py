import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "https://quotes.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

quotes = []

# Extract data
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]

    quotes.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })

# Convert to DataFrame
df = pd.DataFrame(quotes)

# Save to CSV
df.to_csv(r"E:/Task1_Web_Scraping/quotes_data.csv", index=False)

print("Data scraped successfully!")
