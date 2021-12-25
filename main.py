import requests
from bs4 import BeautifulSoup
import bs4.element

names = ["IRCTC.NS"]
url = "https://finance.yahoo.com/quote/{0}?p={0}&.tsrc=fin-srch"

source = requests.get(url.format(names[0])).text
soup = BeautifulSoup(source, "lxml")

current_stock_data = soup.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px) W(100%)")
print(current_stock_data)
