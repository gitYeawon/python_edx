#!/usr/bin/env python
# coding: utf-8

# #  Module 2 Required Coding Activity  
# Introduction to Python Unit 1  
# 
# This is an activity based on code similar to the Jupyter Notebook **`Practice_MOD02_1-3_IntroPy.ipynb`** which you may have completed.
# 
# | Some Assignment Requirements |  
# |:-------------------------------|  
# | **NOTE:** This program requires a **function** be defined, created and called. The call will send values based on user input.  The function call must capture a `return` value that is used in print output.  The function will have parameters and `return` a string and should otherwise use code syntax covered in module 2.  |  
#  
# ## Program: fishstore()
# create and test fishstore()
# - **fishstore() takes 2 string arguments: fish & price**
# - **fishstore returns a string in sentence form**  
# - **gather input for fish_entry and price_entry to use in calling fishstore()**
# - **print the return value of fishstore()**
# >example of output: **`Fish Type: Guppy costs $1`**

# In[21]:


# [ ] create, call and test fishstore() function 
# then PASTE THIS CODE into edX
#def fishstore(fish, price):
#    return ("Fish Type: " + fish +" coats $" +price)

#def choose_fish():
#    user_fish = input("fish entry: ").title()
#    return user_fish

#def choose_price():
#    user_price = input("price_entry: ")
#    return user_price

#print(fishstore(choose_fish(), choose_price()))

def fishstore(fish, price):
    return ('Fish Type: ' + fish +' costs $'+ price)

#def choose_fish():
fish_entry = input("Enter Fish: ")
#    return fish_entry

#def choose_price():
price_entry = input("Enter Price: ")
#    return price_entry

print(fishstore(fish_entry,price_entry))


# ### Need assignment tips and clarification? 
# See the video on the "End of Module coding assignment > Module 2 Required Code Description" course page on [edX](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+4T2017/course)    
# 
# # Important:  [How to submit the code in edX by pasting](https://courses.edx.org/courses/course-v1:Microsoft+DEV236x+1T2017/wiki/Microsoft.DEV236x.3T2018/paste-code-end-module-coding-assignments/)

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
