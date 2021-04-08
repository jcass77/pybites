from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

PACKT = "https://bites-data.s3.us-east-2.amazonaws.com/packt.html"
CONTENT = requests.get(PACKT).text

Book = namedtuple("Book", "title description image link")


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT)

    book_main = soup.find("div", class_="dotd-main-book")
    title_div = book_main.find("div", class_="dotd-title")
    description = title_div.find_next_sibling("div").text.strip()
    image_div = book_main.find("div", class_="dotd-main-book-image")
    image = image_div.find("img").get("src")
    link = image_div.find("a").get("href")

    return Book(title_div.text.strip(), description, image, link)
