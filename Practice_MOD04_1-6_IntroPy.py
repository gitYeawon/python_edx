#!/usr/bin/env python
# coding: utf-8

# # 1-6.2 Intro Python Practice
# ## Nested Conditionals
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - create nested conditional logic in code  
# - print format print using escape sequence (**\**)

# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Tasks</B></font>  

# In[1]:


# [ ] print a string that outputs the following exactly: The new line character is "\n"

print("The new line character is \"\\n\"")


# In[2]:


# [ ] print output that is exactly (with quotes): "That's how we escape!"

print("That's how we escape!")


# In[4]:


# [ ] with only 1 print statement and using No Space Characters, output the text commented below  

# 1       one
# 22      two
# 333     three

print("1\tone\n22\ttwo\n333\tthree")


# # &nbsp;
# ## Program: quote_me() Function
# quote_me takes a string argument and returns a string that will display surrounded with **added double quotes** if printed  
# - check if passed string starts with a double quote (`"\""`), then surround string with single quotations 
# - if the passed string starts with single quote, or if doesn't start with a quotation mark, then surround with double quotations  
# 
# Test the function code passing string input as the argument to quote_me() 

# In[25]:


# [ ] create and test quote_me()

def quote_me(string) :
    
    if string.startswith("\"") :
        return "'" + string + "'"
    
    else :
        return '"'+ string + '"'
print(quote_me("ha"))
print(quote_me('ha'))
print(quote_me("\"this is so annoying \""))


# # &nbsp;
# ### Program: shirt order 
# First get input for color and size  
# - White has sizes L, M 
# - Blue has sizes M, S  
# 
# print available or unavailable, then  
# print the order confirmation of color and size  
# 
# *
# **hint**: set a variable "available = False" before nested if statements and  
# change to True if color and size are avaliable*

# In[51]:


# [ ] create shirt order using nested if 
available = False

color = input("Choose color in White or Blue: ").lower()
size = input("Choose size in S,M,L: ").lower()

while not available:

    if color == "white" :
        
        if size == "L" or size == "M" :
            print("It is available")
            available = True
            
        else :
            print("It is not available")
            break

    elif color == "blue" :
        
        if size == "M" or size == "S" :
            print("It is available")
            available = True
            
        else :
            print("It is not available")
            break

    else :
        print("It is not available") 
    


# # &nbsp;
# ## Program: str_analysis() Function
# Create the str_analysis() function that takes a string argument.  In the body of the function:
# - Check `if` string is digits  
#   - if digits: convert to `int` and check `if` greater than 99  
#     - if greater than 99, print a message about a "big number"  
#     - if not greater than 99, print message about "small number"    
#   - if not digits: check if string isalpha
#     - if isalpha print message about being all alpha
#     - if not isalpha print a message about being neither all alpha nor all digit  
#     
# call the function with a string from user input 

# In[57]:


# [ ] create and test str_analysis()

def str_analysis(str) :
    if str.isdigit() :
        if int(str) > 99 :
            print("big number")
        else :
            print("small number")
    elif str.isalpha() :
        print(str)
    else :
        print("alpha or digit please")
        
str_analysis("5")


# # &nbsp;  
# ### Program: ticket_check() - finds out if a seat is available  
# Call ticket_check() function with 2 arguments: *section* and *seats* requested and return True or False  
# - **section** is a string and expects: general, floor
# - **seats** is an integer and expects: 1 - 10  
# 
# Check for valid section and seats
# - if section is *general* (or use startswith "g")  
#   - if seats is 1-10 return True 
# - if section is *floor* (or use starts with "f")
#   - if seats is 1-4 return True  
# 
# otherwise return False

# In[62]:


# [ ] create and call ticket_check()

def ticket_check(section, seats) :
    
    if section.startswith("g") :
        
        if 1 <= int(seats) <= 10 :
            return True
        
        else :
            return False
        
    elif section.startswith("f") :
        
        if 1 <= int(seats) <= 4 :
            return True
        
        else :
            return False
        
ticket_check("f", 4)
    


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
