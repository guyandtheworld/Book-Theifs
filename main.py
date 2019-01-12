# Author: Pranav Shridhar (github.com/pranavmodx)
import requests
from bs4 import BeautifulSoup
import time


def acrawler():

    isbn = ["0345453743", "1547291817"]

    for i in range(len(isbn)):

        url = f"https://www.amazon.in/dp/{isbn[i]}"
        print("URL = ", url)
        source = requests.get(url)
        source_code = source.text
        soup = BeautifulSoup(source_code, "lxml")

        book_title = soup.find('div', id='booksTitle')
        title = book_title.span.text
        print(f"Book title : {title}")

        pd_details = soup.find('td', class_="bucket")
        elem = pd_details.div.ul

        print('Product Details')
        for li in elem.find_all('li')[0:5]:
            print(li.text)

        time.sleep(20)  # For reducing traffic


acrawler()
