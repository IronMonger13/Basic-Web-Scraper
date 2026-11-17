import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    html_string = response.text
    soup = BeautifulSoup(html_string, "lxml")

    print(soup.title.text)
    print(soup.find("h1").text)
    print(soup.find_all("h1"))
    print(soup.find_all("a")[:5])
    # print(soup.find("div", class_="container-fluid page"))
    print(soup.select("article.product"))

else:
    print(f"ERROR: {response.status_code}")
