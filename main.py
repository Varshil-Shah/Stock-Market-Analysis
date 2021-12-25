import requests
from bs4 import BeautifulSoup
import bs4.element

names = ["IRCTC.NS"]
url = "https://finance.yahoo.com/quote/{0}?p={0}&.tsrc=fin-srch"


def get_name_of_stock(element: bs4.element):
    prev_element = element.previous_sibling
    company_name = prev_element.find("h1").text
    print(company_name)


def get_live_stock(tickers: list[str]):
    for ticker in tickers:
        source = requests.get(url.format(ticker)).text
        soup = BeautifulSoup(source, "lxml")

        current_stock_data = soup.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px) W(100%)")
        get_name_of_stock(current_stock_data)
        print(current_stock_data)


if __name__ == '__main__':
    get_live_stock(names)
