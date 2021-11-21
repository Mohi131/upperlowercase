#!/usr/bin/env python
# coding: utf-8

# In[2]:


s = ('The quick Brow Fox')
count1 = 0
count2 = 0
for a in s:
    if(a.isupper()) == True:
        count1+=1
    elif (a.islower()) == True:
        count2+=1
print("No of lower case character ", count1)        
print("No of upper case character ", count2)


# In[ ]:




