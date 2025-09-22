import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the website (practice site)
url = "http://books.toscrape.com/catalogue/page-1.html"

# List to store extracted data
products = []

# Loop through first 5 pages (you can increase)
for page in range(1, 6):
    response = requests.get(f"http://books.toscrape.com/catalogue/page-{page}.html")
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all products on the page
    items = soup.find_all("article", class_="product_pod")

    for item in items:
        # Extract name
        name = item.h3.a["title"]

        # Extract price
        price = item.find("p", class_="price_color").text

        # Extract rating (class contains rating info)
        rating_class = item.find("p")["class"]
        rating = rating_class[1] if len(rating_class) > 1 else "No rating"

        # Append product details
        products.append([name, price, rating])

# Convert to DataFrame
df = pd.DataFrame(products, columns=["Product Name", "Price", "Rating"])

# Save to CSV
df.to_csv("products.csv", index=False, encoding="utf-8")

print("✅ Data extracted and saved to products.csv")
