# S Sandeep Pillai
import flipkart
import multiprocessing

file = open("URL.txt", 'r')
page = file.readline()
try:
    pages_to_scrape = int(page[28:])
except:
    pages_to_scrape = 5


if __name__ == '__main__':
    jobs = []
    for line in file:
        if line[0]=='h':
            p = multiprocessing.Process(target=flipkart.main, args=(line, pages_to_scrape))
            jobs.append(p)
            p.start()


