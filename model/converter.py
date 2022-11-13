from kneed import KneeLocator
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import csv
import datetime

def findValueInTable(section, region, file):
    reader = csv.reader(file, delimiter=';')

    x = 0

    value = -1

    for column in reader.__next__():
        x += 1
        if column.lower() == section:
            break

    for row in reader:
        if row[0].lower() == region:
            try:
                value = row[x].replace(' ', '')
            except Exception:
                value = 0.0

            if value == '':
                value = 0.0
            else:
                try:
                    value = float(value)
                except Exception:
                    value = 0.0
            break
    
    file.seek(0)

    return value

clusteringCSVFile = open('clusteringCSV.csv', 'w', newline='')
valproductFile = open('valproduct.csv', "r", encoding="utf-8")
oborotFile = open('oborot.csv', "r", encoding="utf-8")
kolvoFile = open('kolvo.csv', "r", encoding="utf-8")

clusteringCSVWriter = csv.writer(clusteringCSVFile)
clusteringCSVWriter.writerow(["Оборот X Коэф.риска", "Валловый продукт / Кол-во предприятий"])

datasetFile = open('hackathon.csv', 'r', encoding='utf-8')
datasetReader = csv.reader(datasetFile, delimiter=';')

counter = 0

datasetReader.__next__()
for datasetRow in datasetReader:

    counter += 1

    if counter % 1000 == 0:
        print(str(counter / 4000000 * 100) + '%', counter, sep=' - ')

    region = datasetRow[2].lower()
    section = datasetRow[5].replace(';', ',').lower()
    date = datasetRow[1].split('-')
    dateFromFoundation = datetime.date.today() - datetime.date(int(date[0]), int(date[1]), int(date[2]))
    
    days = dateFromFoundation.days
    years = int(days / 365.25)

    riskRatio = 1

    if years < 3:
        riskRatio = 0.5
    elif years < 10:
        riskRation = 0.8
    
    valproduct = findValueInTable(section, region, valproductFile)
    oborot = findValueInTable(section, region, oborotFile)
    kolvo = findValueInTable(section, region, kolvoFile)

    if kolvo == 0:
        clusteringCSVWriter.writerow([oborot * riskRatio, 0])
    else:
        clusteringCSVWriter.writerow([oborot * riskRatio, valproduct / kolvo])


