import numpy as np
import numpy.ma as ma


# view and copy 

a = np.full((3,3),9)
b = a[0:1]

print(b)

b[0,1] = 3
print(b)
print(a)# this is view and this both array a and b are refering at the same address therefore b make change to the a array 

#we can copy method 

a1 = np.full((2,2),5)
b1 = a1.copy()

print(b1)
b1[0,1]= 10
print(b1)
print(a1) # we can see that both are the different and b1 didnt make any changes like above one !!!

# we can other method like this 

a2 = np.arange(12).reshape(4,3)

b2 = a2[[0,1]]

print(b2)
b2[1,2] = 10
print(b2)
print(a2) # in this method we use the list inthe indexing 






