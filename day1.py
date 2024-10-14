import numpy as np 

#broadcasting 

a = np.array([1,2,3])
b = np.array([5])

print(a+b) # in this numpy automatically make 3 element in b of 5 means 1+5,2+5,3+5 that it

#imp note 
# in the numpy broadcastinng array are only compatiabel when they have same as them or they have one 
# eg 1st array dimneisonal are [3,2]
# 2st array dimneisonal can be like this [1,2] or [3,1] or [3,2] or [1,1]
#above you can see the rule of compatible that we should have a same number or 1 and also 1 is compatible with any numbner 

#example 

a1 = np.array([1,2]) #(1,2) this will be 
a2 = np.array([[2],[3]]) #(2,1)

#how this work ?
# 1st array is 1 D and other is 2 D 
#we can see that in the 2nd array the 0 index element have two elemnts so because of this 1st array we become twice menas like this :-
# [[1,2],[1,2]]
# so this complete the process and then 2nd array 1st index have 1 elment only and 1st array have 2 elments so this make the 2nd array like this :-
# [[2,2],[3,3]]
#now the addition will be like this:- 1+2,2+2,1+3,2+3 and final is :- [[3,4],[4,5]]

print(a1 + a2)
