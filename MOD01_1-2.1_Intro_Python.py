#!/usr/bin/env python
# coding: utf-8

# # 1-2.1 Intro Python
# ## Strings: input, testing, formatting
# - **input() - gathering user input**  
# - print() formatting 
# - Quotes inside strings
# - Boolean string tests methods
# - String formatting methods
# - Formatting string input()
# - Boolean `in` keyword 
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - **gather, store and use string `input()`**  
# - format `print()` output
# - test string characteristics
# - format string output
# - search for a string in a string

# # &nbsp;  
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font> 
# 
# ## input()  
# ### get information from users with `input()`  
# the **`input()`** function prompts the user to supply data returning that data as a string
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7a8881cb-0bdd-493c-b1a1-9849a95d05e6/Unit1_Section2-1-input-basic.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7a8881cb-0bdd-493c-b1a1-9849a95d05e6/Unit1_Section2-1-input-basic.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 

# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>  

# In[1]:


# review and run code - enter a small integer in the text box
print("enter a small int: ")
small_int = input()
print("small int: ")
print(small_int)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## storing input in a variable
# - **[ ]** create code to store input in student_name variable  
# an input box should when run
# - **[ ]** type a name in the input box and press **Enter**
# - **[ ]** determine the **`type()`** of **student_name**

# In[2]:


# [ ] get input for the variable student_name
print("enter your name: ")
user_name = input()
print("your name is " + user_name)

# [ ] determine the type of student_name



# <font size="4" color="#B24C00"  face="verdana"> <B>Task 1 continued...</B></font>  
# > **note**: **`input()`** returns a string (type = str) regardless of entry
# - if a string is entered **`input()`** returns a string
# - if a number is entered **`input()`** returns a string  
#   
# - **[ ]** determine the **`type()`**  of input below by entering
#   - a name
#   - an integer (whole number no decimal)
#   - a float a number with a decimal point

# In[3]:


# [ ] run cell several times entering a name a int number and a float number after adding code below
print("enter a name or number")
test_input = input()
# [ ] insert code below to check the type of test_input

type(test_input)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# ### user prompts using `input()`
# 
# the **`input()`** function has an optional string argument which displays the string intended to inform a user what to enter  
# **`input()`** works similar to **`print()`**&nbsp;in the way it displays arguments as output  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c607aa57-b18b-4f29-a317-7b13db66d8e8/Unit1_Section2-1-input-prompt.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c607aa57-b18b-4f29-a317-7b13db66d8e8/Unit1_Section2-1-input-prompt.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[4]:


student_name = input("enter the student name: ")  
print("Hi " + student_name)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>  
# ## prompting the user for input
# - **[ ]** create a variable named **city** to store input, add a prompt for the name of a city
# - **[ ]** print "the city name is " followed by the value stored in **city**

# In[5]:


# [ ] get user input for a city name in the variable named city
print("enter your faivorite city")
city = input()

# [ ] print the city name
print(city)


# 
# <font size="4" color="#B24C00"  face="verdana"> <B>Task 2 cont...</B></font>  
# ## multiple prompts for user input
# often programs need information on multiple items
# - **[ ]** create variables to store input: **name**, **age**, **get_mail**
# - **[ ]** create prompts for name, age and yes/no to being on an email list
# - **[ ]** print description + input values   
# 
# >example print output:  
# `name = Alton`  
# `age =  17`  
# `wants email = yes`  
#   
# **tip**: with multiple input statements, after each prompt, **click 'in' the input box** to continue entering input 

# In[ ]:


# [ ]create variables to store input: name, age, get_mail with prompts
# for name, age and yes/no to being on an email list
name = input("your name :")
age = input("your age :")
get_mail = input("yes or no :")

# [ ] print a description + variable value for each variable

city = input("tell me your favorite city :")
print(city)
type(city)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
