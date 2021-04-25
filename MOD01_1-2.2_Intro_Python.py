#!/usr/bin/env python
# coding: utf-8

# # 1-2.2 Intro Python
# ## Strings: input, testing, formatting
# - input() - gathering user input  
# - **print() formatting**  
# - Quotes inside strings
# - Boolean string tests methods
# - String formatting methods
# - Formatting string input()
# - Boolean `in` keyword 
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - gather, store and use string `input()`  
# - **format `print()` output**  
# - test string characteristics
# - format string output
# - search for a string in a string

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# ## comma print formatting
# ### print() comma separated strings 
# Python provides several methods of formatting strings in the **`print()`** function beyond **string addition**   
#   
# **`print()`** provides using **commas** to combine stings for output  
# by comma separating strings  **`print()`** will output each separated by a space by default
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ac97f001-e639-494e-aa15-e420efb5a7a8/Unit1_Section2-2-Print-Comma_Format.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ac97f001-e639-494e-aa15-e420efb5a7a8/Unit1_Section2-2-Print-Comma_Format.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# #### comma formatted `print()`
# - **[ ]** print 3 strings on the same line using commas inside the `print()` function 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[1]:


# review and run code

name = "Collette"

# string addition 
print("Hello " + name + "!")

# comma separation formatting
print("Hello to",name,"who is from the city")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>  
# **print 3 strings on the same line using commas inside the print() function**

# In[2]:


# [ ] print 3 strings on the same line using commas inside the print() function 
print("Hi", name , "Bye")


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# ## using commas in `print()` with strings and numbers together
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/46b436d7-31ed-4e9a-a4c9-55f9eaacfb84/Unit1_Section2-2-Print-String_Number.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/46b436d7-31ed-4e9a-a4c9-55f9eaacfb84/Unit1_Section2-2-Print-String_Number.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - **`print()`** function formatting with comma separation works different than with string addition.
# - **`print()`**  using comma separation can mix numbers (int & float) and strings without a TypeError
# 
# #### `print()` with numbers and strings together using commas
# - **[ ]** use a **`print()`** function with comma separation to combine 2 numbers and 2 strings

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[3]:


# review and run code
print("I will pick you up @",6,"for the party")


# In[4]:


# review and run code
number_errors = 0
print("An Integer of", 14, "combined with strings causes",number_errors,"TypeErrors in comma formatted print!")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>  
# **use a print() function with comma separation to combine 2 numbers and 2 strings**

# In[6]:


# [ ] use a print() function with comma separation to combine 2 numbers and 2 strings

print("Hi " , 1 ,"Bye ", 3)


# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>  
# **print() comma separated mixing of strings and variables**  
# by comma separating strings and/or string variables **`print()`** will output each separated by a space by default
#   
# **display text describing an address, made from stings and variables of different types**
# - initialize variables with input()
#   - street
#   - st_number
# - Display a message about the street and street number using comma separation formatting

# In[7]:


# [ ] get user input for a street name in the variable, street
street = input("street name :")
st_number = input("street number :")

# [ ] get user input for a street number in the variable, st_number

# [ ] display a message about the street and st_number
print(street)
print(st_number)


# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>  
# **`print()` number, strings, variables from input**
# - [ ] display text made from combining a variable, a literal string and a number

# In[9]:


# [ ] define a variable with a string or numeric value
a = 3
# [ ] display a message combining the variable, 1 or more literal strings and a number

print(a,' i like that')


# <font size="6" color="#B24C00"  face="verdana"> <B>Task 5</B></font>   
# ## Program: How many for the training?
# Create a program that prints out a reservation for a training class.  Gather the name of the party, the number attending and the time.
# >**example** of what input/output might look like:
# ```
# enter name for contact person for training group: Hiroto Yamaguchi  
# enter the total number attending the course: 7  
# enter the training time selected: 3:25 PM  
# ------------------------------  
# Reminder: training is schedule at 3:25 PM for the Hiroto Yamaguchi group of 7 attendees  
# Please arrive 10 minutes early for the first class  
# ```  
#   
# Design and Create your own reminder style  
# - **[ ]** get user input for variables:
#   - **owner**: name of person the reservation is for  
#   - **num_people**: how many are attending  
#   - **training_time**: class time
# - **[ ]** create an integer variable **min_early**: number of minutes early the party should arrive
# - **[ ]** using comma separation, print reminder text
#   - use all of the variables in the text
#   - use additional strings as needed
#   - use multiple print statements to format message on multiple lines (optional)

# In[11]:


# [ ] get input for variables: owner, num_people, training_time  - use descriptive prompt text
owner = input("reservation for")
num_people = input("how many people")
training_time = input("class time")
# [ ] create a integer variable min_early and "hard code" the integer value (e.g. - 5, 10 or 15)
min_early = 10
# [ ] print reminder text using all variables & add additional strings -  use comma separated print formatting

print(owner , "need to be in the class " , "at least" , min_early, "for", training_time, "total" , num_people, "people")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
