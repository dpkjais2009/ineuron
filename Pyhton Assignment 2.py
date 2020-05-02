#!/usr/bin/env python
# coding: utf-8

# 1. Create the below pattern using nested for loop in Python.
# 
# ![image.png](attachment:image.png)
# 
# 

# In[3]:


n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# 2. Write a Python program to reverse a word after accepting the input from the user.
# 
# Input word: ineuron
# Output: norueni

# In[8]:


word = input("Input a word to reverse: ")

for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[ ]:




