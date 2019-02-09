import csv
import pandas as pd

amaz = []
flip = []
amaz_data=[]
flip_data=[]
with open('amazon_f.csv', 'r',encoding="utf-8") as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        if len(row[5]) == 10 and row[5].isdigit():
            amaz.append(row[5])
            amaz_data.append(row)
csvFile.close()
with open('All_Data.csv', 'r') as File:
    reader = csv.reader(File)
    for row in reader:
        if len(row[11]) == 10:
            flip.append(row[11])
            flip_data.append(row)
csvFile.close()
dl = open('commom.csv', 'w')
fli=[]
ama=[]
for x in amaz:
    if x in flip:
        i=amaz.index(x)
        j=flip.index(x)
        ama.append(amaz_data[i])
        fli.append(flip_data[j])
with open('amazon_final.csv','w',encoding="utf-8") as amazon:
    writer=csv.writer(amazon)
    writer.writerows(ama)        

with open('flipkart_final.csv', 'w', encoding="utf-8") as flipkart:
    writer = csv.writer(flipkart)
    writer.writerows(fli)
dl.close()
