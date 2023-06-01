#!/usr/bin/env python
# coding: utf-8

# In[5]:


# numpy exercises

#This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow
#and in the numpy documentation. The goal of this collection is to offer a quick reference for both old
#and new users but also to provide a set of exercises for those who teach.


#If you find an error or think you've a better way to solve some of them, feel
#free to open an issue at <https://github.com/rougier/numpy-100>.
#File automatically generated. See the documentation to update questions/answers/hints programmatically.

#### 1. Import the numpy package under the name `np` (★☆☆)
#hint: import … as`

import numpy as np


# In[12]:


#### 2. Create a null vector of size 10 (★☆☆)
#`hint: np.zeros`
a = np.zeros((1,11))
a


# In[25]:


#### 3. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
#hint: array[4]`
a = np.zeros(10)
a[4] = 1
a


# In[27]:


#### 4. Create a vector with values ranging from 10 to 49 (★☆☆)
#hint: arange`
a = np.arange(10,50)
a


# In[35]:


#### 5. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
#hint: reshape`
a = np.random.randint(0., 8, (3, 3))
a


# In[37]:


#### 6. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
#`hint: np.nonzero`
a = [1,2,0,0,4,0]
a_zero = np.nonzero(a)
a_zero


# In[39]:


#### 7. Create a 3x3 identity matrix (★☆☆)
#hint: np.eye`
a = np.eye(3,3)
a


# In[43]:


#### 8. Create a 3x3x3 array with random values (★☆☆)
#hint: np.random.random`
a = np.random.random((3,3,3))
a


# In[64]:


#### 9. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
#hint: min, max`
a = np.random.rand(10, 10)
print(a)
print(a.max())
print(a.min())


# In[71]:


#### 10. Create a random vector of size 30 and find the mean value (★☆☆)
#hint: mean`

a = np.random.rand(30)
print(a)
print(a.mean())


# In[75]:


#### 11. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
#hint: np.diag`
a = np.diag([1, 2, 3, 4, 5])
print(a)


# In[79]:


#### 12. Normalize a 5x5 random matrix (★☆☆)
#hint: (x -mean)/std`
a = np.random.rand(5,5)
print(a)
print((a.mean()/a.std()))


# In[81]:


#### 13. How to find common values between two arrays? (★☆☆)
#hint: np.intersect1d`
a = [20,40,86,90,92]
b = [86,20,123,12,4234,578,57]
 
c = np.intersect1d(a, b)
print("Intersection = ", c)


# In[88]:


#### 14. Create a random vector of size 10 and sort it (★★☆)
#hint: sort`
a = np.random.random(10)
print("Original array:")
print(a)
a.sort()
print("Sorted array:")
print(a)


# In[91]:


#### 15. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
#hint: argmax`
a = np.random.random(10)
print("Original Array: ")
print(a)
a[a.argmax()] = 0
print("Max Value Replaced by 0 Array: ")
print(a)


# In[94]:


#### 16. Subtract the mean of each row of a matrix (★★☆)
#hint: mean(axis=,keepdims=)`

a = np.random.rand(3, 4)
print(a)

print("The mean value of 'a' matrix is: ", a.mean())

b = a - a.mean(axis=1, keepdims=True)

print(b)


# In[99]:


#### 17. How to get the n largest values of an array (★★★)
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5
sorted_index_array = np.argsort(Z)
sorted_array = Z[sorted_index_array]
print("Sorted Array: ", sorted_array)
result = sorted_array[-n :]
print("Result of n -this case 5- largest values of an array:" ,result)
#hint: np.argsort | np.argpartition`


# In[114]:


#### 18. Create a random 5*3 matrix and replace items that are larger than 4 by their squares ( Example:  6 --> 36) 
#hint: np.where`

a = np.random.randint(0,10, size =(5, 3))

print(a)

squared_matrix = np.where(a > 4, a ** 2, a)

print(squared_matrix)

