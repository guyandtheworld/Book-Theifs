import requests
from bs4 import BeautifulSoup



def acrawler():

    isbn = ["0345453743","1847370292"]
    for i in range(len(isbn)):
        url = f"https://www.amazon.in/dp/{isbn[i]}"
        print("URL = " , url)
        # while loop here
        source = requests.get(url)
        source_code = source.text
        soup = BeautifulSoup(source_code, "lxml")
        section = soup.find('div', id='booksTitle')
        title = section.span.text
        print(title)
        # for link in soup.find_all('a'):
        #         print(link.get('href'))


acrawler()
