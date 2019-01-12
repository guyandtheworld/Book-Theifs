import requests
from bs4 import BeautifulSoup

def is_valid_isbn(isbn):

    sum = 0
    if len(isbn) == 13:

        for i in range(13):
            if(i % 2 == 0):
                sum = sum + int(isbn[i])  # asuming this is 0..9, not '0'..'9'

            else:
                sum = sum + int(isbn[i]) * 3

        if sum % 10 == 0:
            return True


    return False

print(is_valid_isbn("9780000000000"))
isbnum = 9788183225090



def fcrawler(url):

        print("URL = ", url)

        source = requests.get(url)
        source_code = source.text                           # BS4 stuff, ignore.
        soup = BeautifulSoup(source_code, "lxml")


        for item in soup.find_all("title"):
            if(item.string!="Buy Products Online at Best Price in India - All Categories | Flipkart.com"):
                print("Name:: ", item.string)
                for book in soup.find_all("li", {"class": "_2-riNZ"}):
                    print(book.string)
        print('\n'*5)

def main():
    for i in range(100):
        if is_valid_isbn(str(isbnum + i)):
            url = "https://www.flipkart.com/placeholder/p/itmdytkfgwnuz7gt?pid=" + str(isbnum+i)
            fcrawler(url)


main()
