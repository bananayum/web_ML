import numpy as np
from sklearn.datasets.samples_generator import make_blobs
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

centers=[[-2,2],[2,2],[0,4]]

x,y=make_blobs(n_samples=60,centers=centers,random_state=0,cluster_std=0.60)
plt.figure(figsize=(16,10),dpi=144)
c=np.array(centers)
k=5
clf=KNeighborsClassifier(n_neighbors=5)
clf.fit(x,y)
xsam=[0,2]
ysam=clf.predict(xsam)
neighbors=clf.kneighbors(xsam,return_distance=False)
plt.scatter(x[:,0],x[:,1],c=y,s=100,cmap='cool')
plt.scatter(c[:,0],c[:,1],s=100,marker='^',c='orange')
plt.scatter(xsam[0],xsam[1],marker='x',c=ysam,s=100,cmap='orange')
plt.show()
