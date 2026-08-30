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
print(j)
