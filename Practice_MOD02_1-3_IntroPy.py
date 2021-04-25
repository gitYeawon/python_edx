#!/usr/bin/env python
# coding: utf-8

# # 1-3 Intro Python Practice
# ## Functions Arguments & Parameters
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - **create functions with a parameter**  
# - **create functions with a `return` value** 
# - **create functions with multiple parameters**
# - **use knowledge of sequence in coding tasks**  
# - **use coding best practices** 

# ## &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Tasks</B></font>

# In[3]:


# [ ] define and call a function short_rhyme() that prints a 2 line rhyme
def short_rhyme():
    print()
    print()

print(short_rhyme())


# In[7]:


# [ ] define (def) a simple function: title_it() and call the function
# - has a string parameter: msg
# - prints msg in Title Case
def title_it(msg):
    return msg.title()
print(title_it("boy"))


# In[29]:


# [ ] get user input with prompt "what is the title?" 
# [ ] call title_it() using input for the string argument
user_input = input("What is the title?")
title_it((user_input))


# In[42]:


# [ ] define title_it_rtn() which returns a titled string instead of printing
# [ ] call title_it_rtn() using input for the string argumetnt and print the result

def title_it_rtn(movie):
    return movie.title()

movie_sub = input()
print(title_it_rtn(movie_sub))


# ## Program: bookstore()
# create and test bookstore()
# - **bookstore() takes 2 string arguments: book & price**
# - **bookstore returns a string in sentence form** 
# - **bookstore() should call title_it_rtn()** with book parameter  
# - **gather input for book_entry and price_entry to use in calling bookstore()**
# - **print the return value of bookstore()**
# >example of output: **`Title: The Adventures Of Sherlock Holmes, costs $12.99`**

# In[47]:


# [ ] create, call and test bookstore() function

#def function_that_prints():
#    print ("I printed")

#def function_that_returns():
#    return "I returned"

#f1 = function_that_prints()
#f2 = function_that_returns()
#print ("Now let us see what the values of f1 and f2 are")
#print (f1)
#print (f2)
def bookstore(book, price) :
    example = ("Title : " ,book, ", costs: $",price)
    return example

book_title = input("book title: ")
book_price = input("book costs: ")
print(bookstore(book_title,book_price))


# ### Fix the error

# In[24]:


def fishstore(fish, price):
    return ("Fish Type: " + fish +" coats $" +price)

def choose_fish():
    user_fish = input("fish entry: ").title()
    return user_fish

def choose_price():
    user_price = input("price_entry: ")
    return user_price

print(fishstore(choose_fish(), choose_price()))


# 
# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
