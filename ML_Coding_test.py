#!/usr/bin/env python
# coding: utf-8

# In[ ]:


squares={1:1,2:4,3:9,4:16,5:25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)


# In[ ]:


my_dict={'name':'Jack','age':26}
    
 my_dict['age']=27
print(my_dict)
my_dict['address']='Downtown'
print(my_dict)


# In[ ]:


test_list = [([1, 2, 3], 'gfg'), ([5, 4, 3], 'cs')] 
  
# printing original list 
print("The original list : " + str(test_list)) 
  
# Using list comprehension 
# Combining tuples in list of tuples 
res = [ (tup1, tup2) for i, tup2 in test_list for tup1 in i ] 
  
# print result 
print("The list tuple combination : " + str(res)) 


# In[ ]:


N = 3 
  
# printing N 
print("Number of times to repeat : " + str(N)) 
  
# N element incremental tuples 
# Using generator expression + tuple 
res = tuple((ele, ) * N for ele in range(1, 6)) 
  
# printing result 
print("Tuple sequence : " + str(res)) 


# In[ ]:




