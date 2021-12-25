import requests
from bs4 import BeautifulSoup
import bs4.element

# names = ["IRCTC.NS"]
names = ["MSFT", "GOOG", "TSLA", "IRCTC.NS"]
url = "https://finance.yahoo.com/quote/{0}?p={0}&.tsrc=fin-srch"


def get_name_of_stock(element: bs4.element) -> str:
    """
    Fetch the name of the stock
    :param element: bs4.element
    :return: str
    """
    prev_element = element.previous_sibling
    company_name = prev_element.find("h1").text
    return company_name


def get_table_summary(element: bs4.element) -> list[dict]:
    """
    Loop all the <tr> in element
    :param element: bs4.element
    :return: list[dict]
    """
    details = []
    all_tr = element.find_all("tr")
    for tr in all_tr:
        all_td = tr.find_all("td")
        stock_detail = {tr.td.span.text: all_td[1].text}
        details.append(stock_detail)
    return details


def get_stock_summary(element: bs4.element) -> None:
    """
    Fetch the summary portion of the element
    :param element: bs4.element
    :return: None
    """
    available_summaries = element.find_all("div", attrs={"data-test": True})
    left_side_summary = available_summaries[0].table.tbody
    right_side_summary = available_summaries[1].table.tbody
    print(get_table_summary(left_side_summary))
    print(get_table_summary(right_side_summary))


def get_stock_header(element: bs4.element) -> list[dict]:
    """
    Loop all <fin-streamer> in element
    :param element: bs4.element
    :return: list[dict]
    """
    price_info = []
    for data in element.find_all("fin-streamer", attrs={"data-field": True}):
        price_data = {data.attrs['data-field']: data.text}
        price_info.append(price_data)
    return price_info


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
        print(get_name_of_stock(current_stock_data))

        summary = soup.find("div", id="quote-summary")
        print(get_stock_summary(summary))

        print(get_stock_header(current_stock_data))


if __name__ == '__main__':
    get_live_stock(names)
