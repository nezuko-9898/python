# 2D arry
import numpy as np
a = np.array([[10,20,30,40,50],[60,70,80,90,100]])

print(a[0,1])
print(a[1,2])


# slicing
b = np.array ([1,2,3,4,5,6,7,8,9,0])
print(b[1:4])


# type casting
c= np.array([1.1,2.1,3.1,4.1])
c1=  c.astype(int)
print(c1)

# COPY and  View

#COPY
original_arr=np.array([10,20,30,40,50])

new_arr = original_arr.copy()
new_arr [0]=90

print(original_arr)
print(new_arr)

#View

original_ar=np.array([90,80,70,60])

n_arr = original_ar.view()
n_arr [1]= 2

print(n_arr)
print(original_ar)

#shape numpy

o= np.array([[10,20,30,40,50],[60,70,80,90,100]])
print(o.shape)


#Reshape Array 1D to 2D

o1=np.array([1,2,3,4,5,6,7,8,9])
re_shape= o1.reshape(3,3)

print(re_shape)


#Reshape Array  1D to 3D


x1 = np.array([1,2,3,4,5,6,7,8,9,0,11,12])

r_shape = x1.reshape(2,2,3)
print(r_shape)


#iterating in  numpy
x2= np.array(['naruto','moring','start'])

for x in x2:
    print(x)



    

