#!/usr/bin/env python
# coding: utf-8

# 1.1 Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()
# 

# In[1]:


def myreduce(anyfunc, sequence):

 # Get first item in sequence and assign to result
  result = sequence[0]
 # iterate over remaining items in sequence and apply reduction function 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result


# In[10]:


# test myreduce function
def sum(x,y): return x + y
print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )


# 1.2 Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()
# 

# In[8]:


def myfilter(anyfunc, sequence):

 # Initialize empty list
 result = []
 # iterate over sequence of items in sequence and apply filter function
 for item in sequence:
  if anyfunc(item):
   result.append(item)

 # return funal output
 return result


# In[11]:


# test myfilter function
def ispositive(x):
 if (x <= 0): 
  return False 
 else: 
  return True

print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


# 2. Implement List comprehensions to produce the following lists.
# 
# Write List comprehensions to produce the following Lists
# 
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6],
# [4, 5, 6, 7], [5, 6, 7, 8]]
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[12]:


word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))


# In[13]:


# Compress above for loop into a single list comprehension using technique [i <Upper for condition> <lower for condition>]
input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))


# In[15]:


input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))


# In[16]:


input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))


# In[17]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# In[ ]:




