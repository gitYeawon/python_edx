#!/usr/bin/env python
# coding: utf-8

# # 1-5 Intro Python Practice  
# ## conditionals, type, and mathematics extended   
# &nbsp;
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - code more than two choices using **`elif`** 
# - gather numeric input using type casting  
# - perform subtraction, multiplication and division operations in code  &nbsp;  
# 

# # &nbsp;  
# <font size="6" color="#B24C00"  face="verdana"> <B>Tasks</B></font>

# ### Rainbow colors
# ask for input of a favorite rainbow color first letter: ROYGBIV  
# 
# Using `if`, `elif`, and `else`:  
# - print the color matching the letter  
#     - R = Red  
#     - O = Orange  
#     - Y = Yellow  
#     - G = Green
#     - B = Blue
#     - I = Indigo
#     - V = Violet
#     - else print "no match"
# 

# In[79]:


# [ ] complete rainbow colors

fav_color = input().title()

if fav_color == "R" :
    print("Red")
elif fav_color == "O" :
    print("Orange")
elif fav_color == "Y" :
    print("Yellow")
elif fav_color == "G" :
    print("Green")
elif fav_color == "B" :
    print("Blue")
elif fav_color == "I" :
    print("Indigo")
elif fav_color == "V" :
    print("Violet")
else :
    print("No match")
    
    
    


# In[78]:


# [ ] make the code above into a function rainbow_color() that has a string parameter, 
# get input and call the function and return the matching color as a string or "no match" message.
# Call the function and print the return string.

def rainbow_color(fav_color) :
    
    #fav_color = input().title()

    if fav_color.title() == "R" :
        return("Red")
    elif fav_color.title() == "O" :
        return("Orange")
    elif fav_color.title() == "Y" :
        return("Yellow")
    elif fav_color.title() == "G" :
        return("Green")
    elif fav_color.title() == "B" :
        return("Blue")
    elif fav_color.title() == "I" :
        return("Indigo")
    elif fav_color.title() == "V" :
        return("Violet")
    else :
        return("No match")
    
rainbow_color(input("Choose ROYGBIV: "))
    


# # &nbsp;  
# **Create function age_20() that adds or subtracts 20 from your age for a return value based on current age** (use `if`) 
# - call the funtion with user input and then use the return value in a sentence  
# example `age_20(25)` returns **5**: 
# > "5 years old, 20 years difference from now"

# In[66]:


# [ ] complete age_20()

def age_20(current_age) :
    
    
    if current_age > 20 :
        
        return str(current_age - 20) + " years old. 20 years diffrence from now "
    
    if current_age < 20 :
        
        return str(current_age + 20) + " years old. 20 years diffrence from now "
    
print(age_20(34))
    


# **create a function rainbow_or_age that takes a string argument**
# - if argument is a digit return the value of calling age_20() with the str value cast as **`int`** 
# - if argument is an alphabetical character return the value of calling rainbow_color() with the str
# - if neither return FALSE

# In[ ]:


# [ ]  create rainbow_or_age()
def rainbow_or_age() :
    


# In[ ]:


# [ ]  add 2 numbers from input using a cast to integer and display the answer 
    a = int(input())
    b = int(input())


# In[52]:


# [ ] Multiply 2 numbers from input using cast and save the answer as part of a string "the answer is..."
# display the string using print
a = int(input())
b = int(input())
print("The answer is..." , (a*b))


# In[ ]:


# [ ] get input of 2 numbers and display the average: (num1 + num2) divided by 2

    print((a + b) / 2)


# In[44]:


# [ ] get input of 2 numbers and subtract the largest from the smallest (use an if statement to see which is larger)
# show the answer

a = int(input())
b = int(input())
if a > b :
    print(a - b)
elif a == b :
    print(a - b)
else:
    print(b - a)


# In[45]:


# [ ] Divide a larger number by a smaller number and print the integer part of the result
# don't divide by zero! if a zero is input make the result zero
# [ ] cast the answer to an integer to cut off the decimals and print the result

a = int(input())
b = int(input())

if a > b :
    print(a / b)
elif a == b :
    print(a / b)
else:
    print(b / a)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
