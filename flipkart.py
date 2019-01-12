import requests
from bs4 import BeautifulSoup



def fcrawler():

    isbn = ["9781582701707"]
    for i in range(len(isbn)):
        url = "https://www.flipkart.com/placeholder/p/itmdytkfgwnuz7gt?pid=" + isbn[i]
        print("URL = " , url)
        # while loop here
        source = requests.get(url)
        source_code = source.text
        soup = BeautifulSoup(source_code, "lxml")
        
        for item in soup.find_all("title"):
            print("Name:: " , item.string)
            
        for item in soup.find_all("li", {"class": "_2-riNZ"}):
            print(item.string)







fcrawler()
