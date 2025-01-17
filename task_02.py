# -*- coding: utf-8 -*-
"""Task_02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eg5F9OKYhA0IZetRpGYznLrKugAOvehW
"""

import numpy as np
import pandas as pd

from google.colab import files
uploded = files.upload()

import io
df = pd.read_csv(io.BytesIO(uploded["Mall_Customers.csv"]))
df.shape

df.head()

df["A"]= df[['Annual Income (k$)']]
df["B"]= df[['Spending Score (1-100)']]

x = df[["A","B"]]
x.head()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# %matplotlib inline

plt.scatter(x["A"],x["B"], s= 30, c="blue")
plt.show()

kmean = KMeans(n_clusters=5)
kmean.fit(x)

centers = kmean.cluster_centers_
print(kmean.cluster_centers_)

clusters = kmean.fit_predict(x)
df["label"] = clusters
df.head(100)

col=['green','blue','black','yellow','pink',]

for i in range(5):
    a=col[i]
  #print(a)
    plt.scatter(df.A[df.label==i], df.B[df.label==i], c=a ,label='cluster i')
    plt.scatter(centers[:,0],centers[:,1],marker='*',s=300,c='r',label="centroid")

x1 = x.loc[:,["A","B"]].values

wcss=[]
for k in range(1,11):
    kmeans = KMeans(n_clusters = k, init = "k-means++")
    kmeans.fit(x1)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(12,6))
plt.grid()
plt.plot(range(1,11),wcss,linewidth=2,color="red",marker='8')
plt.xlabel("number of clusters")
plt.ylabel("wcss")
plt.show()