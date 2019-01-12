# Author: S Sandeep Pillai (github.com/Corruption13)
import requests
from bs4 import BeautifulSoup

isbnum = 9780000000000      # Lowest possible number?


def is_valid_isbn(isbn):        # Check if isbn number meets ISBN - Standards.

    isbn_sum = 0
    if len(isbn) == 13:

        for i in range(13):
            if(i % 2 == 0):
                isbn_sum = isbn_sum + int(isbn[i])  # asuming this is 0..9, not '0'..'9'

            else:
                isbn_sum = isbn_sum + int(isbn[i]) * 3

        if isbn_sum % 10 == 0:
            return True


    return False


def fcrawler(url):      # Main function that scrapes the url provided.

        source = requests.get(url)
        source_code = source.text                           # BS4 stuff, ignore.
        soup = BeautifulSoup(source_code, "lxml")

        for item in soup.find_all("title"):
            if item.string[:21] != "Online Shopping India":             # IF so, then item DOES NOT EXIST
                print("URL = ", url)
                print("Name:: ", item.string)
                for book in soup.find_all("li", {"class": "_2-riNZ"}):
                    print(book.string)
                print('\n'*3)


def main():
    for i in range(1000):
        if is_valid_isbn(str(isbnum + i)):
            url = "https://www.flipkart.com/placeholder/p/itmdytkfgwnuz7gt?pid=" + str(isbnum+i)
            fcrawler(url)


main()

