#!/usr/bin/env python
# coding: utf-8

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 
# 

# In[1]:


for i in range(2000,3201):
    if i%7 == 0 and i%5!=0:
        print(i,end=',')
print("\b")


# 2. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name. 

# In[1]:


firstname = input("What is your first name?:")
lastname = input("What is your last?")
print(firstname[::-1] + " " + lastname[::-1])


# 3. Write a Python program to find the volume of a sphere with diameter 12 cm. 
# Formula: V=4/3 * π * r 
# 

# In[2]:


import math


# In[3]:


pi = math.pi

#Converting Diameter into radius
r = float(12/2)

V = (float(4/3)*(pi)*(r)**3)

print(V)


# In[ ]:




