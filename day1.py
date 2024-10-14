import numpy as np 

#creating random array with numpy

# This is eg of rand() this generator only positive number
a = np.random.rand(5)
print(a) # this will create a random array between the value of 0 and 1 and this array will of 5 values in it and its a 1 d array 

b = np.random.rand(3,5)
print(b) # this is the 2 d array !!!

#randn() this genrator number close to 0 but they can be negative and positive also 
c = np.random.randn(2,5)
print(c)

#ranf() this will generate the random float values 
d = np.random.ranf((2,4))
print(d)

#randint for the integer values 
d1 = np.random.randint(0,100,(2,10))
print(d1)