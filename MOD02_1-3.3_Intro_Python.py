#!/usr/bin/env python
# coding: utf-8

# # 1-3.3 Intro Python
# ## Functions Arguments & Parameters
# - Creating a simple Function with parameters
# - Exploring Functions with `return` values 
# - Creating Functions with multiple parameters
# - **Sequence in python**  
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - create functions with a parameter  
# - create functions with a `return` value 
# - create functions with multiple parameters
# - **use knowledge of sequence in coding tasks**  
# - **Use coding best practices** 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## Sequence
# In programming, **sequence** refers to the order that code is processed.  Objects in Python, such as variables and functions, are not available until they have been processed. 
# 
# Processing sequence flows from the top of a page of code to the bottom. This often means that **Function definitions are placed at the beginning of a page of code.**
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29ebdee3-33e8-487f-9c73-621219e5e6d2/Unit1_Section3.3-Object_Sequence.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/29ebdee3-33e8-487f-9c73-621219e5e6d2/Unit1_Section3.3-Object_Sequence.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# In the sample below, the function **`hat_color`** cannot be accessed since it is initialized after it is called at the bottom of the code.  
# ```python
# have_hat = hat_available('green')  
#   
# print('hat available is', have_hat)
# 
# def hat_available(color):
#     hat_colors = 'black, red, blue, green, white, grey, brown, pink'
#     return(color.lower() in hat_colors)
# ```  
# This results in an error - the code flows from top to bottom is in the incorrect **sequence** 
# ```python
# NameError: name 'hat_available' is not defined
# ```
# In the statement &nbsp; **`have_hat = hat_available('green')`** &nbsp; the function &nbsp; **`hat_available()`** &nbsp; needs to be called after the function has been defined
# > **Note:** an argument or variable is said to be **hard coded** when assigned a literal or constant value.  
#     It is a good habit to avoid creating hard coded values in functions, such as  
#     `hat_colors = 'black, red, blue, green, white, grey, brown, pink'`

# ## &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[1]:



def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    # return Boolean
    return(color.lower() in hat_colors)
# review and run code - note: fix error in the following "tasks" section
have_hat = hat_available('green')  
  
print('hat available is', have_hat)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## Change the Sequence to fix the `NameError`
# - [ ] fix the code **sequence** so the &nbsp;**`hat_available()`** &nbsp;function is availabe when called and the code runs without error

# In[2]:



def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return(color.lower() in hat_colors)
# [ ] fix the sequence of the code to remove the NameError

have_hat = hat_available('green')  
  
print('hat available is', have_hat)




# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Programming Style Tip: Avoid Hard-Coding
# ### "Hard-coding" is placing data values directly into code
# An example of hard-coding from above is **`have_hat = hat_available('green')`**  where the argument `'green'` is hard-coded
# 
# A programming best practice is to **avoid hard-coding values when possible**
# - Use varibles and verse hard-coded 
# - Often preferable to use input such as a configuration file (advanced topic) or user input.
# These practices allow changing the data without disturbing the main code and makes code more reusable.
# 

# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## Program: bird_available
# The program should ask for user to "input a bird name to check for availability" and print a statement informing of availability
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/767e4db3-7909-4829-99db-fd6750ea5d54/Unit1_Section3.3-Bird_Available.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/767e4db3-7909-4829-99db-fd6750ea5d54/Unit1_Section3.3-Bird_Available.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### create this program with a Boolean function `bird_available()`
# - has parameter that takes the name of a type of bird
# - for this exercise the variable `bird_types = 'crow robin parrot eagle sandpiper hawk piegon'`
# - return `True` or `False` (we are making a Boolean function)
# - call the function using the name of a bird type from user input
# - print a sentence that indicates the availablity of the type of bird checked
# 

# In[13]:


# [ ] create function bird_available
#def bird_available(bird):
#    bird_types = ("crow, robin, parrot, eagle, sandpiper, hawk, piegon")
#    return (bird.lower in bird_type)

# [ ] user input
#user_bird = input()
# [ ] call bird_available
#bird_available(user_bird)
# [ ] print availbility status
#print("bird available is", bird_available())

def bird_available(bird) :
    bird_types = ("crow, robin, parrot, eagle, sandpiper, hawk, piegon")
    return (bird.lower() in bird_types)

my_bird = input("Enter your bird")
bird_available(my_bird)
print(bird_abvailable())


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ## Fix The Error
# 

# In[9]:


# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested

def practice() :
    try_this = input(" I am learning inputs")
    return try_this

#give_tries = practice()
print(practice())

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
