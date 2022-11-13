import csv
import pickle
import numpy as np
import pandas as pd
from kneed import KneeLocator
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import KMeans


def creating_model():
    data = pd.read_csv("clusteringCSV.csv", encoding="cp1254")
    x = data.loc[:, ['Îáîğîò X Êîıô.ğèñêà', 'Âàëëîâûé ïğîäóêò / Êîë-âî ïğåäïğèÿòèé']].values
    km = KMeans(n_clusters = 5, init = 'k-means++')
    km.fit(x)
    pickle.dump(km, open("save.pkl", "wb"))


def using_model():
    data = pd.read_csv("clusteringCSV.csv", encoding="cp1254")
    x = data.loc[:, ['Îáîğîò X Êîıô.ğèñêà', 'Âàëëîâûé ïğîäóêò / Êîë-âî ïğåäïğèÿòèé']].values
    km = pickle.load(open("save.pkl", "rb"))
    labels = km.predict(x)
    centroids = km.cluster_centers_

    plt.scatter(x[labels == 0, 0], x[labels == 0, 1], s=21, c='pink', label='Кластер 1')
    plt.scatter(x[labels == 1, 0], x[labels == 1, 1], s=21, c='green', label='Кластер 2')
    plt.scatter(x[labels == 2, 0], x[labels == 2, 1], s=21, c='red', label='Кластер 3')
    plt.scatter(x[labels == 3, 0], x[labels == 3, 1], s=21, c='blue', label='Кластер 4')
    plt.scatter(x[labels == 4, 0], x[labels == 4, 1], s=21, c='purple', label='Кластер 5')

    plt.title('KMeans Clustering', fontsize=20)
    plt.xlabel('Оборот с учетом времени деятельности ИП, млрд.руб ')
    plt.ylabel('Доля ВВП на одно предприятие / кол-во предприятий')
    plt.legend()
    plt.grid()
    plt.show()

    with open("hackathon.csv", "r", encoding="utf-8") as f:
        with open('result.csv', "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            reader = csv.reader(f, delimiter=";")
            i = 0
            reader.__next__()
            for row in reader:
                writer.writerow([row[0], labels[i]+1])
                i+=1

using_model()