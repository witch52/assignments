# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:55:47 2023

@author: students
"""

#cycle5


import numpy as np


ar1 = np.array([1,2,3,4],float)
print("new array",ar1)
print(ar1.dtype)


ar1 = np.array([1,2,3,4],int)
print("new array",ar1)
print(ar1.dtype)


ar1 = np.array([1,2,3,4],bool)
print("new array",ar1)
print(ar1.dtype)

a=np.array([complex(2,3),complex(4,5)])
print(a)
print(a.ndim)

#reshape
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newa=a.reshape(4,3)
print(newa)

#array join
d=np.array([[1,2,3],[4,5,6]])
e=np.array([[7,8,9],[1,11,12]])
f=np.concatenate((d,e),axis = 1)
print(f)

#array split
a1=np.array([1,2,3,4,5,6,7,8,9,10])
b=np.split(a1, 2)
print(b)

a2=np.array([1,2,3,5,6,7,8,9,10])
b2=np.array_split(a2, 2)
print(b2)

#searching

newarray = np.array([4,2,1,3])
print(np.sort(newarray))

s = np.where(newarray == 4)
print(s)

s1 = np.where(newarray == 12)
print(s1)

arr = np.array_split(newarray,2)
print(arr)

arr1=np.array([1,2,3,4,5,6,7,8,9])
print(arr1[1:3])
print(arr1[0:])
print(arr1[:9])
print(arr1[1:])
arr1[1:2]=3
print(arr1)



#1d
ar1 = np.array([1,2,3,4])
print("array is",ar1)
print (ar1.ndim)
print (ar1.shape)

#2d
array2=np.array([[1,2,3],[4,5,6,]])
print(array2)







