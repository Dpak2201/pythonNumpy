import numpy as np
#creating a scalar value
a=np.array(34)
#print(a.ndim ,a.shape)
#creating a one dimensional array 
b=np.array([1,2,3,4])
#print(b.ndim,b.shape)
#creating multi diemnsional array 
c=np.array([[[1,2,3],[2,3,4]],[[4,5,6],[6,7,8]]])
#print(c.ndim , c.shape)
#arange method 
d=np.arange(0,10,1) 
e=np.linspace(0,10,25)
#print(d,e)
#logspace
f=np.logspace(1,4,2)
#print(f)
#zeros
g=np.zeros(5,dtype=int)
h=np.zeros([2,3])
#print(g)
#ones
i=np.ones([2,3],dtype=int)
#print(i)
#full
j=np.full([2,3],8.5)
#print(j)
#randomNumberGeneration
k=np.random.rand(2,3)#random for float number generation
#print(k)
l=np.random.randint(20,80,[3,4])#random integer generation
#print(l)
m=np.random.randn(2,3)#normal distribution random number generation
#print(m)
#type casting 
n=np.array([1,2.2,3.4,4.5])
print(n)
m=n.astype(np.int64)
print(m,m.dtype)


