import numpy as np
import numpy.ma as ma

# vectorization 

a = np.arange(1,13).reshape(4,3)
print(a)

def remove_even(x):
    if x % 2 == 0:
        return 0
    else:
        return x
    
b= np.vectorize(remove_even)
print(b(a))   

#custom data types 

# in this we can make our owen data types like this :-

sif = np.dtype("U10, i4,f8")

new = np.array([("aman",24,4564.878),("noa",59,46.2),("sangwan",5,9.64),("ram",98,459.21)], dtype = sif)

print(new)
print(new.nbytes)
print(new.dtype)