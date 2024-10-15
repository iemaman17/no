import numpy as np
import numpy.ma as ma
# masking 

a = np.array([1,2,3,np.nan,np.inf])

b = ma.array(a,mask=[0,0,0,1,1])
print(b.mean())

print(b)



#this is called masking 


c = np.arange(21)
print(ma.masked_where(c%2==0,c)) 








