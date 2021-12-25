import requests
from bs4 import BeautifulSoup
import bs4.element

names = ["IRCTC.NS"]
url = "https://finance.yahoo.com/quote/{0}?p={0}&.tsrc=fin-srch"


def get_name_of_stock(element: bs4.element) -> str:
    """
    Fetch the name of the stock
    :param element: bs4.element
    :return: str
    """
    prev_element = element.previous_sibling
    company_name = prev_element.find("h1").text
    print(company_name)
    return company_name


def get_stock_summary(element: bs4.element):
    available_summaries = element.find_all("div", attrs={"data-test": True})
    left_side_summary = available_summaries[0].table.tbody
    right_side_summary = available_summaries[1].table.tbody


def get_live_stock(tickers: list[str]):
    """
    Scrape the data from the website
    :param tickers: list[str]
    :return: None
    """
    for ticker in tickers:
        source = requests.get(url.format(ticker)).text
        soup = BeautifulSoup(source, "lxml")

        current_stock_data = soup.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px) W(100%)")
        get_name_of_stock(current_stock_data)

        summary = soup.find("div", id="quote-summary")
        get_stock_summary(summary)


if __name__ == '__main__':
    get_live_stock(names)
