#!/usr/bin/env python
# coding: utf-8

# # 1-3.2 Intro Python
# ## Functions Arguments & Parameters
# - Creating a simple Function with a parameter
# - **Exploring Functions with `return` values**  
# - **Creating Functions with multiple parameters**  
# - Sequence in python  
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - create functions with a parameter  
# - **create functions with a `return` value**
# - **create functions with multiple parameters**
# - use knowledge of sequence in coding tasks 
# - Use coding best practices 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Calling a function with a return value  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/db990568-d940-4ede-a063-7e40ed25c978/Unit1_Section3.2-function-return.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/db990568-d940-4ede-a063-7e40ed25c978/Unit1_Section3.2-function-return.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - **`type()`** returns an object type
# -  **`type()`** can be called with a float the return value can be stored in a variable
# ```python
# object_type = type(2.33)
# ```  
# 
# ## creating a function with a return value  
# - **`return`** keyword in a function *returns* a value after *exiting* the function  
# 
# ```python
# def msg_double(phrase):
#       double = phrase + " " + phrase
#       return double
# ```  
# 

# ## &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>  
#   
# review and run the code

# In[14]:


# Message double returns the string Argument doubled
def msg_double(phrase):
      double = phrase + " " + phrase
      return double

# save return value in variable
msg_2x = msg_double("let's go")
print(msg_2x)

def msg_triple(sentence):
    triple = sentence + " " + sentence + " " + sentence
    return triple

tri = msg_triple("Excellent")
print(tri)


# In[18]:


# example of functions with return values used in functions
def msg_double(phrase):
      double = phrase + " " + phrase
      return double

def msg_triple(sentence) :
    triple = sentence + " " + sentence + " " + sentence
    return triple

# prints the returned object
print(msg_double("Save Now!"))
print(msg_triple("Happt New Year"))
# echo the type of the returned object
type(msg_double("Save Now!"))


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Doctor: a function that adds the "Doctor" title to a name
# - Define function `make_doctor()`&nbsp; that takes a parameter `name`
# - get user **input** for variable **`full_name`**
# - call the function using `full_name` &nbsp; as argument
# - print the return value

# In[31]:


# create and call make_doctor() with full_name argument from user input - then print the return value

def make_doctor(name) :
    full_name = input()
    return full_name

#make_doctor(input)

def make_doctor(name) :
    return "Doctor " + name

full_name = input("Enter your name ")
print(make_doctor(full_name))
#print(make_doctor("James"))


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Functions with multiple parameters
# Functions can have multiple parameters separated by commas
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d82c3856-61ff-4fa3-9a20-df8f6ea4dd7a/Unit1_Section3.2-MultiParam_Function.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/d82c3856-61ff-4fa3-9a20-df8f6ea4dd7a/Unit1_Section3.2-MultiParam_Function.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# ## &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>  
#   
# review and run the code

# In[28]:


def make_schedule(period1, period2):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title())
    return schedule

student_schedule = make_schedule("mathematics", "history")
print("SCHEDULE:", student_schedule)

def make_couple(one, the_other):
    couple = ("One: " + one + ", The Other: " + the_other)
    return couple

student = make_couple("Jame","Amy")
print(student)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# 
# ## Define `make_schedule()` adding a 3rd period to &nbsp; 
# - Start with the above example code
# - add a parameter period_3
# - update function code to add period_3 to the schedule
# - call **`student_schedule()`** with an additional argument such as 'science'
# - print the schedule

# In[32]:


# [ ] add a 3rd period parameter to make_schedule
# [ ] Optional - print a schedule for 6 classes (Tip: perhaps let the function make this easy)
# def low_case(words_in): 
#      return words_in.lower()  

#words_lower = low_case("Return THIS lower")
#print(words_lower)

def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3rd] " + period3.title())
    return schedule

student_schedule = make_schedule("mathematics", "history","science")
print("SCHEDULE:", student_schedule)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
