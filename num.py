# The Declaration of one dimensional array
import numpy as np


# n=np.array([1,2,3])              #rank 1 array 
# print(n)
# print(type(n))
# print(n.shape)


# c=np.array([[1,2,3],[4,5,6]])    #rank 2 array
# print(c)
# print(type(c))   
# print(c.shape)
# print(c[0][1],c[1][2],c[1,0])


# a=np.zeros([4,4])                 #zero matrix using zeros([order of matrix for eg 2X2,4X3 etc.])
# print(a)
# b=np.ones([3,4])
# print(b)
# d=np.full([4,4],10)           #to create a matrix of same no. use
# print(d)                      #full() function to get the desired result np.full([range of matrix],the no. of the matrix)  
# e=np.eye(3)                   #to create an identity matrix eye()range function is used
# print(e)


# f=np.random.randint(0,90,[3,3])     #this function helps us to generate an array with random "integer"numbers
# print(f)                                   
# f=np.random.random([4,4])           #for float values use np.random.random(array size)
# print(f)


# x=np.array([[1,2],[3,4]])
# y=np.array([[5,6],[7,8]])            


# # z=x+y or z=np.add(x,y)  
# # z=np.subtract(y,x)                #arithmetic functions on matrices
# z=np.multiply(x,y)
# z=np.divide(y,x)
# print(z)


# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]]])

# print(a.ndim)                  #"ndim" function is used to check the dimension of a matrix
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# arr = np.array([1, 2, 3, 4], ndmin=5)  #"ndmin" function is used to create array of higher dimensions i.e. more than 3D

# print(arr.ndim)
# print(arr)

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])        

       # #this step is known as data slicing , We pass slice instead of index like this: [start:end]

# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1::3])

# print(np.dot(x,y))     #the dot() function in numpy performs the Dot product i.e. scalar multipication of two matrices
print (np.pi)            #np.pi function is used to print the value of pi