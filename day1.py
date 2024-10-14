import numpy as np 

#advance indexing 

#this is the now one indexing in the numpy 


a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

print(a[0:3]) #by this we are selecting the rows like in th eg we are selecting the whole matrix if we do [1:3]w
#we will select the second row means 1 index row and 3 row a(2 index row )

#by using the list for the selecting 

print(a[[0,2]]) # in this we are selecting only o index row ( 1 row ) and the 2 index row ( means  3 rd row ) 

#imp indexing method( dimensional indexing)

print(a[:,:]) # in this first jam(:)  means for the row and second is for columns 
print(a[0,:]) # this will give only [1,2,3] becuase we selected only o index row 
print(a[:,0]) # this will give only [1,4,7] becuase we selected only o index columns 
#and as on we can give 1 index in both rows and columns and 2 index and so on !!!!!
#we have np.newaxis property for giving the new axises 
print(a[np.newaxis,0,:]) #u can see the difference in both above one and below one we got addtional axises
print(a[:,0,np.newaxis]) #same here also  we got it in horizontal 

# we can mix the dimensional indexing iwth other indexing also 
#eg 

print(a[[0,2],[2,0], np.newaxis]) #in this will get only [3 ,7]

# we use bolleans for the indexing also like this : - 

print(a[[0],[True,False,True]]) # in this we will get the [1 ,3 ] because i gave the false value to the 2 and i only selected the 1st row !!
