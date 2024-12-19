#3d Array
"""
from numpy import * 
a=ones((2,3),dtype=int)
print(a)
"""

from numpy import *
arr= array([[4,5,6],[7,8,9]])
print(arr)

'''
from numpy import *
arr= array([[4,5,6],[7,8,9]])
print(arr+5)

'''
"""
#gives sum of all
from numpy import *
arr= array([[4,5,6],[7,8,9]])
print(sum(arr))
"""

#gives min of 
from numpy import *
arr= array([[4,5,6],[7,8,9]])
print(arr.min())



#0th row show 
from numpy import *
arr= array([[4,5,6],[7,8,9]])
print(arr[0])


#1 st row 2nd column  show 9 number 
from numpy import *
arr= array([[4,5,6],[7,8,9]])
print(arr[1,2])

'''
'''
#1 st row 2nd column  show 9 number 
from numpy import *
arr= array([[4,5,6],[7,8,9]])
print(arr[1][2])



'''
#program to accept elements into in t 2 dim array anddisplay them


import numpy as np

#accept no of row,col
r,c =[int(i) for i in input('how many row, cols?').split(',')]

#create a 2d array and fill it with 0s
arr=np.zeros((r,c),dtype=int)

#accept 
print('Enter array elements row by row: ' )
for i in range (r):
    arr[i] =[int(i) for i in input().split()]

#display 2d array
print('DIsplay 2d array is : ',)
for i in range(r):
    print(arr[i])
'''
"""
#accept a metrix elements from kaybord and disply it transpose matric


import numpy as np
#accept no of row,col
r,c =[int(i) for i in input('how many row, cols?').split(',')]

#create a 2d array and fill it with 0s
arr=np.zeros((r,c),dtype=int)

#accept 
print('Enter array elements row by row: ' )
for i in range (r):
    arr[i] =[int(i) for i in input().split()]

#display 2d array
print('DIsplay 2d array is : ',)




#  same as above 
print(arr[i] for i in input().split())

#convert 2d array into a metrix
mat=mat.transpose()

#display transpose matrix is:')

print('transpose matrix is :')



print(mat)
"""
"""
# accept s mstrix element from kb display transpose

# matrix is created by 2D array only

r,c =[int(i) for i in input('How many roes and column you want?').split()]

#create a 2d array and fil with 0
arr=np.zeros((r,c),dtype=int)

#enter array element
print('Enter array element row by row: ')

for i in range(r):
    arr[i] = [int(i) for i in input().split()]

#convert array into matrix
mat=matrix(arr)    # matrix method or matrix function

#printing matrix
print('\nmat is: ')
for i in range(r):
    print(mat[i])

# print transpose matrix
print('\ntranspose matrix is: ')
trans=mat.T
print(trans)

"""
