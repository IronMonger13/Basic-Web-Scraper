import requests
from bs4 import BeautifulSoup

books = []
page_number = 1

while True:
    url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        html_string = response.text
        soup = BeautifulSoup(html_string, "lxml")

        # print(soup.title.text)
        # print(soup.find("h1").text)
        # print(soup.find_all("h1"))
        # print(soup.find_all("a")[:5])
        # # print(soup.find("div", class_="container-fluid page"))
        # print(soup.select("article.product"))

        for book in soup.select("article.product_pod"):
            title = book.h3.a["title"]
            price = book.select_one(".price_color").get_text(strip=True)
            books.append({"title": title, "price": price})

        page_number += 1

    else:
        break

print(books)
