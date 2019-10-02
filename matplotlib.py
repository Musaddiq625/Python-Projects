import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from sklearn.cluster import KMeans
x= [1, 5, 1.5, 8, 1, 9]
y= [2, 8, 1.8, 8, 0.6, 11]
plt.scatter(x,y)
X=([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])
kmean = KMeans(n_clusters=2)
kmean.fit(X)
centroids = kmean.cluster_centers_
labels = kmean.labels_
print(centroids)
print(labels)
colors = ['g.','r.','y.']
for i in range(len(X)):
       print('co-ordinates:',X[i],'label:', labels[i])
       plt.plot(X[i][0],X[i][1],colors[labels[i]],markersize=10)

plt.scatter(centroids[:,0], centroids[:,1],marker="X",s=100, linewidths=1,zorder=2)
plt.show()

