import requests
from bs4 import BeautifulSoup
import time
start = time.time()
# Author: S Sandeep Pillai (github.com/Corruption13)
'''
    This is a program that can execute N number of books from Flipkart.com using brute IDBN code scrapping.
    The base IDBN Number can be set below if you plan to execute this on multiple devices.

'''

Base_ISBNum = 9780000000000      # The'seed' baseline ISB Number, Change for each pc mining it for division of labor.
number_of_books_to_scrape = 50   # This is the amount of books to scrape. Setting this higher could get you throttled.


'''

        THE CODE BELOW NEED NOT BE EDITED.

'''


print("Begin Scrape!")


file = open("Data.csv", 'w')


def is_valid_isbn(isbn):        # Check if ISBN number meets ISBN - Standards. NOTE: Takes in String

    isbn_sum = 0                # Logic: https://www.instructables.com/id/How-to-verify-a-ISBN/
    if len(isbn) == 13:

        for i in range(13):
            if i % 2 == 0:
                isbn_sum = isbn_sum + int(isbn[i])

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
                print("Name:: ", item.string[:-37])
                file.write(item.string[:-37])
                for book in soup.find_all("li", {"class": "_2-riNZ"}):
                    print(book.string)
                    file.write(', ' + book.string)
                file.write('\n')
                return True         # Return True that a book has been verified to exist.

        return False    # If given URL returns #404 page.


def scrape_books(max_value):    # Number of books to be scraped
    counter = 0
    isbnum = Base_ISBNum
    while counter < max_value:
        if is_valid_isbn(str(isbnum)):
            url = "https://www.flipkart.com/placeholder/p/itmdytkfgwnuz7gt?pid=" + str(isbnum)      # URL Constructor
            if fcrawler(url):
                counter = counter + 1   # If book exists in website
        isbnum = isbnum + 1


scrape_books(number_of_books_to_scrape)        # Number of books to be scraped


file.close()
end = time.time()
print("TIME FOR EXECUTION == ", end - start)

