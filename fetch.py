import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = f"https://books.toscrape.com/"
HEADERS = {"User-Agent": "Mozilla/5.0"}


def fetch(url):
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            return response.text
        return None
    except:
        return None


def parse_content(html, url):
    soup = BeautifulSoup(html, "lxml")

    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").get_text(strip=True)
        price = float(price.replace("Â£", ""))
        availability = book.select_one(".instock.availability").get_text(strip=True)
        image_src = requests.compat.urljoin(url, book.select_one("img")["src"])
        content.append(
            {
                "title": title,
                "price": price,
                "availability": availability,
                "image_src": image_src,
            }
        )


if __name__ == "__main__":
    content = []
    page_number = 1
    for i in range(3):
        full_url = BASE_URL + f"catalogue/page-{page_number}.html"
        html_string = fetch(full_url)
        if html_string:
            parse_content(html_string, full_url)
            page_number += 1
        else:
            continue

    df = pd.DataFrame(content)
    print(df.shape)
    print(df)
