import numpy as np

#searching and iterating over the array 

#searching 

a = np.array([2,4,3,8,0.1,38,5,1,0,9,6,88,76,0.1])

print(np.argmax(a)) # this give the index of max value 
print(a.max()) # this give the max value 

print(np.argmin(a)) # min value index 
print(a.min()) #min value 

print(np.nonzero(a)) # give the index of value who are non zero  

# iteraing 

a1 = np.arange(9).reshape(3,3)
print(a1)

for items in np.nditer(a1,order="C"):
    print(items, end=" ")#this is iteraing vertically 
print()

for items in np.nditer(a1,order="F"):
    print(items, end=" ")









