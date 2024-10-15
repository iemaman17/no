import numpy as np
#sorting the array 
a = np.array([[3,8,2],
              [6,4,1],
              [7,0,9]])

print(np.sort(np.sort(a,axis=0),axis=1)) #this method is good but its not dinemical purely 

#another method

b = a.copy()
print(b)

b=b.flatten()
b=np.sort(b)
print(b.reshape(a.shape)) # by using this we can make sorting more dynamic 







