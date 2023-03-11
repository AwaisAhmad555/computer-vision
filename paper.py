import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
#from kmeans import KMeans
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

data = pd.read_csv("BankChurners.csv")

plot.scatter(data['Income_Category'],data['Total_Revolving_Bal'])
plot.xlabel('Income_Category')
plot.ylabel('Total_Revolving_Bal')
plot.show()

print(data[['Income_Category','Total_Revolving_Bal']])

print()

csv_list = data.iloc[:,[14]].values.reshape(-1)

index_list = []

for i, label in enumerate(csv_list):

    #print([i])

    index_list.append(i)

    pass

x = data[['Total_Revolving_Bal','Total_Revolving_Bal']]


new_x = data[['Total_Revolving_Bal']]

Kmeans = KMeans(7)

y_predict = Kmeans.fit_predict(new_x)

print(y_predict)

cluster = y_predict

data['cluster'] = cluster

data_cluster_1 = data[data.cluster == 0]
data_cluster_2 = data[data.cluster == 1]
data_cluster_3 = data[data.cluster == 2]
data_cluster_4 = data[data.cluster == 3]
data_cluster_5 = data[data.cluster == 4]
data_cluster_6 = data[data.cluster == 5]
data_cluster_7 = data[data.cluster == 6]

plot.scatter(data_cluster_1['Total_Revolving_Bal'],data_cluster_1['Education_Level'],color="black",label="cluster 1",marker="x")
plot.scatter(data_cluster_2['Total_Revolving_Bal'],data_cluster_2['Education_Level'],color="blue",label="cluster 2",marker="o")
plot.scatter(data_cluster_3['Total_Revolving_Bal'],data_cluster_3['Education_Level'],color="green",label="cluster 3",marker="*")
plot.scatter(data_cluster_4['Total_Revolving_Bal'],data_cluster_4['Education_Level'],color="red",label="cluster 4",marker="x")
plot.scatter(data_cluster_5['Total_Revolving_Bal'],data_cluster_5['Education_Level'],color="cyan",label="cluster 5",marker="o")
plot.scatter(data_cluster_6['Total_Revolving_Bal'],data_cluster_6['Education_Level'],color="yellow",label="cluster 6",marker="+")
plot.scatter(data_cluster_7['Total_Revolving_Bal'],data_cluster_7['Education_Level'],color="grey",label="cluster 7",marker="^")


plot.xlabel("Income_Category")
plot.ylabel("Total Revolving balance")


plot.legend()

plot.show()









"""

csv_list = data.iloc[:,[14]].values.reshape(-1)

index_list = []

for i, label in enumerate(csv_list):

    #print([i])

    index_list.append(i)

    pass

print(index_list.to)


print(data.iloc[:,[5,7,14]])

plot.scatter(data['Total_Revolving_Bal'],data['Total_Revolving_Bal'])
plot.show()

print()

print()

print(data['Total_Revolving_Bal'])


#print(data.iloc[:,[5,7,14]])

#print(data.iloc[:,[14]].values.reshape(-1))



"""