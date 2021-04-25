#!/usr/bin/env python
# coding: utf-8

# # 1-1.4 Intro Python
# ##  Getting started with Python in Jupyter Notebooks
# - Python 3 in Jupyter notebooks
# - `print()`
# - comments  
# - data types basics
# - variables  
# - **Addition with Strings and Integers**
# - **Errors**  
# - character art  
# 
# -----
# 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - use Python 3 in Jupyter notebooks
# - write working code using `print()` and `#` comments  
# - write working code using `type()` and variables
# - combine Strings using string addition (+)
# - **add numbers in code (+)**  
# - **troubleshoot errors**  
# - create character art

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Addition: Numbers and Strings  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a8befa5f-b4a5-4081-87c0-8846be85c719/Unit1_Section1.4-Addition.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a8befa5f-b4a5-4081-87c0-8846be85c719/Unit1_Section1.4-Addition.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ### Numeric addition
# **Numeric addition** Single line *math equations*, run in a code cell, will output a sum 
# ```python
# # adding a pair of single digit Integers
# 3 + 5  
# ```  
# ## String addition
# **string addition** single line *equations*, run in a code cell, will output a single concatenated string  
# > **Tip:** all strings must be in quotes  
#     
# ```python
# # adding a pair of strings
# "I wear " + "a hat"  
# ```  
# We can also **add variables** as long as we add strings to strings and numbers to numbers

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# ## String and Number Addition

# In[1]:


# [ ] Review and run code for adding a pair of 2 digit Integers
23 + 18


# In[2]:


# [ ] Review and run code for adding 2 strings
"my name is " + "Alyssa"  


# In[4]:


# [ ] Review and run code for adding a variable string and a literal string
shoe_color = "brown"
"my shoe color is " + shoe_color


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1: multi-part</B></font>
# ## String and Number Addition

# In[6]:


# [ ] add 3 integer numbers
a = 0
a + 3


# In[10]:


# [ ] add a float number and an integer number
a = 1
a + 3.0 + 4


# In[12]:


# [ ] Add the string "This notebook belongs to " and a string with your first name

name = 'me'
"This notebook belongs to " + name


# In[13]:


# [ ] Create variables sm_number and big_number and assign numbers then add the numbers
sm_number = 1
big_number = 5

sm_number + big_number


# In[15]:


# [ ] assign a string value to the variable first_name and add to the string ", remember to save the notebook frequently"

first_name = 'nami'
first_name + " Remember to save the notebook"


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# ## use addition in variable assignments  
# It is common to store the results of addition in a variable  
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/48aefdf7-8f2f-4080-97e9-c25477f71248/Unit1_Section1.4-Assignment.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/48aefdf7-8f2f-4080-97e9-c25477f71248/Unit1_Section1.4-Assignment.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# ## use addition in `print ()`   
# Use **`print()`** to show the results of multiple lines of output  
#  

# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# ## addition in variable assignments and in `print()`

# In[16]:


# [ ] review & run code for assigning variables & using addition
add_two = 34 + 16
first_name = "Alton"
greeting = "Happy Birthday " + first_name

print(add_two)
print(greeting)


# In[18]:


#  [ ] review & run code for Integer addition in variables and in a print function
int_sum = 6 + 7
print(int_sum)
print(11 + 15)
print(int_sum)


# In[20]:


# string addition in variables and in print()function
hat_msg = "I do not wear " + "a hat"  
print(hat_msg)
print("at " + "dinner" + hat_msg)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2: multi-part</B></font>
# ## create Integer addition and  string addition output

# In[24]:


# [ ] perform string addition in the variable named new_msg (add a string to "my favorite food is ")
new_msg = "My favorite food is"
print(new_msg + " Pizza")



# In[26]:


# [ ] perform Integer addition in the variable named new_msg (add 2 or more Integers)
new_sum =   0
print(new_sum + 4 - 2)



# In[27]:


# [ ] create and print a new string variable, new_msg_2, that concatenates new_msg + a literal string
new_msg_2 = 'frog'
print(new_msg + 'eat it' + new_msg_2)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# ## Errors!
# Encountering **Errors** and troubleshooting errors are fundamental parts of computer programming
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7ab2739a-95e6-4399-9b84-19ac5698bbea/Unit1_Section1.4-TypeError.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7ab2739a-95e6-4399-9b84-19ac5698bbea/Unit1_Section1.4-TypeError.vtt","srclang":"en","kind":"subtitles","label":"english"}])

# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[28]:


# [ ] review & run code
print("my number is " + "123") #string, represents a text character
print("my number is " + 123) #number, with numeric value 


# #### TypeError
# The line&nbsp; **`print("my number is " + 123)`** causes the **`TypeError`** message to appear  
# >`TypeError: Can't convert 'int' object to str implicitly`  
# 
# When adding to the string&nbsp; `"my number is "`&nbsp; the compiler is experiencing another string, but finds a number ***`123`**  
# 
# Python cannot convert the Integer &nbsp; `123`&nbsp; to a string without explicit instruction (in code) 
#   
# in other words, python only allows combining *like types*
# - **`str`** + **`str`**
# - **`int`** + **`int`**
# 

# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ## Fix `TypeError` 
# - Review the code in the cells below and then run the code
# - Fix any errors and run until the code no longer shows errors

# In[30]:


# [ ] review and run the code - then fix any Errors
total_cost = "3" + "45"
print(total_cost)


# In[32]:


# [ ] review and run the code - then fix any Errors
school_num = "123"
print("the street number of Central School is " + school_num)


# In[33]:


# [ ] Read and run the code - write a hypothesis for what you observe adding float + int
#  [ ] HYPOTHESIS: 

print(type(3.3))
print(type(3))
print(3.3 + 3)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font> 
# ## More Errors
# ### SyntaxError & NameError
# - **SyntaxError** - breaks code formatting rules of python
# - **NameError** - object is not defined (can't be found)  
# 
# Python has a specific grammar that it follows that is referred to as **syntax**.  
# The print function syntax rules for output of a single string include 
# - parentheses **` ( ) `** containing a **string** follow **`print`** (SyntaxError)
# - strings have **matching quotation marks** (SyntaxError)
# - `print` is lowercase and correctly spelled (NameError)
# 
# Failure to follow any of these rules results in a `SyntaxError` or `NameError` when the code is run  
# 

# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# ## SyntaxError
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1a1cd6c0-793f-4bcb-a0a0-c9f95a302142/Unit1_Section1.4-SyntaxNameErrors.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/1a1cd6c0-793f-4bcb-a0a0-c9f95a302142/Unit1_Section1.4-SyntaxNameErrors.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - Improperly formatted string (quotes don't match) that results in a SyntaxError

# In[34]:


# [ ] review and run the code for properly and improperly formatted print statement
print("Hi!")
## Improper format - non matching quotes
print('I like the morning") 


# - note that the misspelling of "`prin`" below results in a NameError

# In[35]:


# [ ] review and run the code 
prin('hi')


# - EOF = "end of file" found in code below
# - Python went to the end of the file looking for, but not finding, a closing parenthesis 

# In[36]:


# [ ] review and run the code missing the closing parenthesis  
print("where are my socks?" 


# - In code below: a parenthesis inside quotations will be seen a part of a string and not as a parenthesis

# In[37]:


# { ] review and run the code 
print("my socks are in the wrong bin)" 


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# ## Fix Errors

# >**Tip**: explaining errors to a partner often reveals a solution (works even if explaining error to a pencil) 

# In[39]:


# [ ] repair the syntax error 
print('my socks do not match') 
      


# In[41]:


# [ ] repair the NameError  
print("my socks match now") 


# In[43]:


# [ ] repair the syntax error 
print()"Save the notebook frequently")


# In[ ]:


# [ ] repair the NameError 
student_name = "Alton"
print(STUDENT_NAME)


# In[ ]:


# [ ] repair the TypeError
total = 3
print(total + " students are signed up for tutoring")


# A parenthesis inside quotations will be seen a part of a string and not as a parenthesis

# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
