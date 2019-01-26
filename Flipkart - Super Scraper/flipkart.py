# Author: S Sandeep Pillai (github.com/Corruption13)
import requests
from bs4 import BeautifulSoup
import sys
from lxml.html import fromstring
import os
import time
start = time.time()

# from itertools import cycle             # Pulled out proxy switching till fixing an issue. Rest works fine.


'''
    This is a program that can scrape N number of books from Flipkart.com's "Best-seller books" list.
    You can pause the crawler at any time, it'll pick up from the last search page. Use this feature with caution,
    it's very buggy.
    ISSUES: Delete "backup.csv" in root folder if issues persist to refresh the data set.
    
    
    You may EDIT the two lines below to MODIFY the crawler for your needs.

'''

no_of_pages_to_scrape = 50  # Accepted values:  1 to 50
base_url = "https://www.flipkart.com/books/educational-and-professional-books/pr?sid=bks,enp&q=books&otracker=categorytree"


'''
    HOW TO EDIT URL
    
    
    Edit the above "base_url" variable with that of other search category after modifying the url*
    EXAMPLE:
    To search educational books list, click on that in flipkart, and copy paste that url. 
    The URL during documentation was 
    "https://www.flipkart.com/books/educational-and-professional-books/pr?sid=bks,enp&otracker=categorytree"
    
    * MAKE SURE YOU ARE !NOT! ON PAGE 2 or ANOTHER PAGE, ensure you are on PAGE 1 when copying the URL!

'''
print("Use master.py to run my script!")
if not os.path.exists("Data"):
    os.makedirs("Data")
    print("Welcome to My Flipkart scraper, new user!")



def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies





def fcrawler_books(url):      # Main function that scrapes the url provided.

    try:
        source = requests.get(url)
        source_code = source.text                           # BS4 stuff, ignore.
        soup = BeautifulSoup(source_code, "lxml")

        for item in soup.find_all("title"):

            # print("URL = ", url)

            language = " "
            binding = " "
            publisher = " "
            genre = " "
            isbn13 = " "
            isbn10 = " "
            pages = " "
            edition = " "
            stars = " "
            rating = " "
            reviews = " "
            # Details of book


            price = soup.find("div", {"class": "_1vC4OE _3qQ9m1"}).string

            temp_title = soup.find("h1", {"class": "_9E25nV"}).find("span").contents
            imp_detail = str(temp_title[-1]).split(',')

            title = str(temp_title[0]).replace(',', '-')
            authors = str(imp_detail[2:])[2:-3].replace(',', ' and ')
            #file.write(', ' + item.string[:-37])


            try:
                stars = soup.find("div", {"class": "_1i0wk8"}).string
                for i in soup.find_all("div", {"class": "row _2yc1Qo"}):
                    obj = i.string
                    if obj[-1] == "&":
                        rating = obj[:-10].replace(',', '')
                    else:
                        reviews = obj[:-8].replace(',', '')


            except Exception:
                pass
            print('\nTitle: ', title, end=' ')
            #print("\nAuthors: ", authors)
            print("Price: ", price)
            #print( stars, 'with', rating, 'votes and', reviews, 'reviews')
            for book in soup.find_all("li", {"class": "_2-riNZ"}):
                # print(book.string)  # Uncomment for messy console.
                detail = book.string.replace(",", " &")
                if detail[0:8] == "Language":
                    language = detail[10:]
                elif detail[0:7] == "Binding":
                    binding = detail[9:]
                elif detail[0:9] == "Publisher":
                    publisher = detail[11:]
                elif detail[0:5] == "Genre":
                    genre = detail[7:]
                elif detail[0:4] == "ISBN":
                    isbn_num = detail[6:].split('&')
                    isbn13 = str(isbn_num[0])  # Excel doesnt have 13 digit flat number, hence string
                    isbn10 = str(isbn_num[1])
                elif detail[0:5] == "Pages":
                    pages = detail[7:]
                elif detail[0:7] == "Edition":
                    edition = str(detail[9:]).replace(',', '-')


            file.write('\n' + url)
            file.write(', Rs: ' + price[1:].replace(',', ''))
            file.write(', ' + title)
            file.write(', ' + authors)
            file.write(',' + stars )
            file.write(',' + rating)
            file.write(',' + reviews)
            file.write(',' + language)
            file.write(',' + binding)
            file.write(',' + publisher)
            file.write(',' + genre)
            file.write(',' + isbn10)
            file.write(',' + isbn13)
            file.write(',' + pages)
            file.write(',' + edition)

    except Exception:
        print("\nERROR, THE GIVEN URL - PAGE HAS ISSUE OR CUSTOM URL SET UP WRONG!\n")


def scrape_books(max_value):        # Number of books to be scraped


    page = 1

    counter = 1
    '''
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    '''
    try:
        while page <= max_value and page <= 50:         # Flipkart only has 50 pages right now, change if future update.

            url = base_url + "&page=" + str(page)                  # URL Constructor
            '''
            proxy = next(proxy_pool)
            source = requests.get(url, proxies={"http": proxy})
            '''
            source = requests.get(url)
            source_code = source.text                   # BS4 stuff, ignore.
            soup = BeautifulSoup(source_code, "lxml")


            for links in soup.find_all("a", {'class': "Zhf2z-"}):
                url = "https://www.flipkart.com" + links.get('href')
                #print("\n[", counter, "]", end=" ")
                counter = counter + 1
                fcrawler_books(url)

            print('\n', "#"*20)

            page = page + 1
            print("##",page-1,'##')






    except KeyboardInterrupt:
            print("42")


'''

END OF FUNCTION DEFINITIONS

'''


def main(url, pages):

    global base_url, no_of_pages_to_scrape
    base_url = url
    no_of_pages_to_scrape = pages
    genre = url[31]
    i = 32
    while url[i]!= '/':
        genre += url[i]
        i += 1

    global file
    file = open("Data/" + genre + ".csv", 'w')
    file.write("URL, Price, Title, Author, Stars, Ratings Count, Reviews Count, Language, Binding, Publisher, Genre, ISBN10, ISBN13(Double Click to view), Pages, Edition")

    scrape_books(no_of_pages_to_scrape)        # Number of books/40 to be scraped


    file.close()
    data = open("Data/" + genre + ".csv", 'r')
    back = open('Data/All_Data.csv', 'a')  # Creates a backup file incase you need to pause.
    data.readline()
    back.write('\n')
    back.write(data.read())

    end = time.time()
    print("TIME FOR EXECUTION == ", end - start)




#main()

print("Thank you for using my crawler, send suggestions at github.com/Corruption13\n\n")