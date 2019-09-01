import numpy as np

a=np.array([[3,2000],
            [2,3000],
            [4,5000],
            [5,8000],
            [1,2000]],dtype='float')

mean=np.mean(a,axis=0)
norm=a-mean
scope=np.max(norm,axis=0)-np.min(norm,axis=0)
norm=norm/scope
print(norm)

u,s,v=np.linalg.svd(np.dot(norm.T,norm))
print(u)

ureduce=u[:,0].reshape(2,1)
# print(ureduce)

r=np.dot(norm,ureduce)

# print(r)

z=np.dot(r,ureduce.T)
z=np.multiply(z,scope)+mean
print(z)