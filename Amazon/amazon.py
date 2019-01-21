# Author: Pranav Shridhar (github.com/pranavmodx)

import requests
from bs4 import BeautifulSoup
import csv

outputFile = open("a_scrape.csv", "w")

with outputFile:
    csvWriter = csv.writer(outputFile)
    csvWriter.writerow(["Name", "URL", "Author", "Price", "No. of Ratings", "Rating", "ISBN"])

for pageNumber in range(1,3):
    inAmazonURL = requests.get(f"https://www.amazon.in/gp/bestsellers/books/ref=zg_bs_pg_{pageNumber}?ie=UTF8&pg={pageNumber}")
    inAmazonData = BeautifulSoup(inAmazonURL.content, "lxml")

    bookCounter = 0

    for bookDataFull in inAmazonData.find_all('div', attrs={'class': 'a-section a-spacing-none aok-relative'}):
        
        outputFile = open("a_scrape.csv", "a")
        bookData = bookDataFull
        if bookData.find('div', attrs={'class': 'p13n-sc-truncate p13n-sc-line-clamp-1'}) is None:
            bookName = "Not Available"
        else:
            bookName = bookData.find('div', attrs={'class': 'p13n-sc-truncate p13n-sc-line-clamp-1'}).get_text().strip()

        if bookData.find('a', attrs={'class': 'a-link-normal'}) is None:
            bookURL = "Not Available"
        else:
            bookLinkData = bookData.find('a', attrs={'class': 'a-link-normal'})
            if bookLinkData.get("href") is None:
                bookURL = "Not Available"
            else:
                bookLink = bookLinkData.get("href")
                bookURL = "https://www.amazon.in" + str(bookLink)

        if bookData.find('a', attrs={'class': 'a-size-small a-link-child'}) is None:
            bookAuthor = "Not Available"
        else:
            bookAuthor = bookData.find('a', attrs={'class': 'a-size-small a-link-child'}).get_text().strip()

        if bookData.find('span', attrs={'class': 'p13n-sc-price'}) is None:
            bookPrice = "Not Available"
        else:
            bookPrice = bookData.find('span', attrs={'class': 'p13n-sc-price'}).get_text().strip()

        if bookData.find('a', attrs={'class': 'a-size-small a-link-normal'}) is None:
            bookNoRatings = "Not Availble"
        else:
            bookNoRatings = bookData.find('a', attrs={'class': 'a-size-small a-link-normal'}).get_text().strip()
        if bookData.find('span', attrs={'class': 'a-icon-alt'}) is None:
            bookRating = "Not Available"
        else:
            bookRating = bookData.find('span', attrs={'class': 'a-icon-alt'}).get_text().strip()
        
        url_split = bookLink.split('/')[3]
        bookISBN = str(url_split[:10])
        print(bookISBN)

        if len(bookISBN)!=10:
            bookISBN = '00'+bookISBN

        with outputFile:
            csvWriter = csv.writer(outputFile)
            csvWriter.writerow([bookName, bookURL, bookAuthor, bookPrice, bookNoRatings, bookRating, bookISBN])

        bookCounter += 1
        if(bookCounter == 50):
            break
