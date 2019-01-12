import requests
from bs4 import BeautifulSoup



def acrawler():

    isbn = "0345453743"
    url = "https://www.amazon.in/dp/" + isbn
    print("URL= " , url)
    # while loop here
    source = requests.get(url, "html.parsar")
    source_code = source.text
    soup = BeautifulSoup(source_code)

    for link in soup.find_all('a'):
        print(link.get('href'))


acrawler()
