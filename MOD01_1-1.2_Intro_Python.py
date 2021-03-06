#!/usr/bin/env python
# coding: utf-8

# # 1-1.2 Intro Python
# ##  Getting started with Python in Jupyter Notebooks
# - Python 3 in Jupyter notebooks
# - `print()`
# - Comments  
# - **data types basics**
# - **variables  **
# - addition with Strings and Integers 
# - Errors
# - character art  
# 
# -----
# 
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - use Python 3 in Jupyter notebooks
# - **write working code using `print()` and `#` comments**  
# - write working code using `type()` and variables
# - combine Strings using string addition (+)
# - add numbers in code (+) 
# - troubleshoot errors
# - create character art

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## What is a **String?**  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cbe90d91-876f-42f3-90df-2955588d02b0/Unit1_Section1.2-String.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/cbe90d91-876f-42f3-90df-2955588d02b0/Unit1_Section1.2-String.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# Strings were used in "Hello World!" print function examples. Strings are sets of characters.  In Python strings are in double or single quotes like `"Hello World!"` or `'after edit, save!'`  
#   
# A String is a common **type** of data, used in programming, consisting of a sequence of 1 or more characters. 
# * **A String is a sequence of characters** (aka: a *string* of characters)  
#     * Character examples: `A, B, C, a, b, c, 1, 2, 3, !, &`
# * A String in python is contained in quotes, single(') or double(")
#     * String examples:  "ABC", 'Joana Dias', 'I have 2 pet cats.', "item #3 cost \$3.29 USD"  
#     > **Note:** the quotes containing a string must come in matched pairs   
#     > - `"Hello"` or `'Hello'` are correctly formatted strings  
#     > - `"Hello'` is incorrectly formatted starting with double " and ending with single ' python needs a matching quote to know where the string ends

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[ ]:


# examples of printing strings with single and double quotes
print('strings go in single')
print("or double quotes")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>    
# ## print messages with "double quotes" and 'single' quotes

# In[2]:


# [ ] enter a string in the print() function using single quotes
print('hi')

# [ ] enter a string in the print() function using double quotes
print("Hi")


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Integers are another type
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7b0e6a97-551d-4f98-9646-679d30eb2ce4/Unit1_Section1.2-Integers.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/7b0e6a97-551d-4f98-9646-679d30eb2ce4/Unit1_Section1.2-Integers.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# - whole numbers such as `-2, -1, 0, 1, 2, 3` are Integers 
# - Integers are **not placed in quotes**  
#   
# A String can contain any character, this includes letters, spaces, punctuation, number digits and formatting. In a string with digits (`"123"`) the digits are text images rather than representations of numeric values.  
# 
# >**remember** a line of python code starting with the pound or hash symbol (**#**) indicates a **comment**  
# &nbsp;  
# comments are for humans to read and are not run by computers
# 
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[3]:


# printing an Integer with python
print(299)

# printing a string made of Integer (number) characters with python
print("2017")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font> 
# - **print Integers**
# - ** print strings made of Integer characters**

# In[5]:


# [ ] print an Integer

print(3)
# [ ] print a strings made of Integer characters

print("4")


# >**Student Tip:** look for **[ ]** , which indicates a task in the notebook needs to be completed.  
# Edit and Run to complete the task  

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Variables & Storing Strings in **Variables**  
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/bc5d7c7c-b30f-41d1-acc3-131fa4bc9634/Unit1_Section1.2-Variables.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/bc5d7c7c-b30f-41d1-acc3-131fa4bc9634/Unit1_Section1.2-Variables.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### Variables are named containers
# Computer programs often create storage for things that are used in repeated processing like item_price, student_name, stock_symbol. In python a variable  is a type of **object** that can be addressed by name to access the assigned contents.
# 
# #### Name a variable staring with a letter or underscore "_"
# There are different styles for creating variables this course uses lowercase descriptive names connected by underscores:
# - item_price
# - student_name
# - stock_symbol  
# 
# descriptive names reduce the need for comments in the code and make it easier to share code or read code written long ago
# 
# ### Variables can hold strings
# once a variable is **assigned**:
# >**`current_msg = "I am a string" `**  
#   
# a python program can refer to the variable, &nbsp; **`current_msg`**, &nbsp; in code  
# so that &nbsp;**` current_msg `**, can be used like the string value &nbsp;(**`"I am a string"`**) &nbsp; which it stores  
#   
# ### Variable reassignment
# We can reassign a variable, changing the contents.   **`current_msg = "new current message" `**  
# 
# ### Variables can be used in place of literals 
# If we initialize **`current_msg = "new current message" `** then  
# the literal string **` "new current message" `** and the variable **` current_msg `** are the same when used in code

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# - **Initializing variables**
# - **literals & variables** in printing
# - **Variable reassignment**

# In[6]:


# [ ] Review code and Run
# initialize the variable
current_msg = "I am a string"

# print literal string
print("I am a string")

# print variable string
print(current_msg)


# In[9]:


# [ ] Review code and Run
# assign a new string to the current_msg
current_msg = "Run this cell using Ctrl+Enter"
print(current_msg)
current_msg = "I don't want to"

print(current_msg)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font> 
# ## Program: assigning values to a string
# - in the cell below
#   - print the variable current_msg  
#   - assign a new string to current_msg  
#   - print the variable  current_msg again
# - run the code cell above and then run the cell below

# In[11]:


# { ] run cell above then run this cell after completing the code as directed

current_msg = "Deer"
print(current_msg)
current_msg = "Dog"
print(current_msg)


# **Q?:** In the cell above, why did the variable have a value to print before it was assigned?  
#   
# Jupyter notebooks run cells individually.  Any cell in the notebook can access a variable assigned from a cell that has been run in the current notebook session.

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Data types in variables
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/85de7ef1-bdd3-4460-849a-41e976bfdf46/Unit1_Section1.2-Types.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/85de7ef1-bdd3-4460-849a-41e976bfdf46/Unit1_Section1.2-Types.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# variables can be initialized with different data types.  Below we see item_price is a **decimal** (aka - float) and student_name is **string** 
#   
# ```python
# item_price = 10.25 #item_price initialized as a numeric value (no quotes)
# student_name ="Dias, Joana" #student_name initialized as a string
# license_plate = "123A" #license_plate initialized as a string
# ```
# 
# 
# ### Variables can start initialized as an Integer number data type  
# >```python 
# x = 22
# ``` 
# here the Integer `22`&nbsp; value was assigned to the variable &nbsp;**`x`**    
# 
# ### The type of data a variable holds can be changed,
# ### Python variables can change the **type** of data a variable holds  
# 
# >```python
# x = 22
# x = "I am a string"
# ```  
# 
# **` x `**&nbsp; changed type from Integer &nbsp;**`x = 22`**&nbsp; to string&nbsp; **`x = "I am a string"`**  
#    
# >>|Best Practice: Friendly Names |
# |------------------------------------------------------------------------------------------|
# | **Friendly name** examples, (`item_price, student_name,license_plate`), were used above. |  
#   
#   
# #### Variables help us to write code that can be used repeatedly
# A personalized letter can be sent to every student with individual names by using a name in a variable. Let's start with printing a name based on string variable.
# 
# Create a variable, `name`, at the top of the next cell. Assign a string value to &nbsp; `name `. 
# 
# > Remember to use the quotes for string values
# 
# example:
# 
# ```python
# name = "Joana Dias"
# print(name)
# ```

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[12]:


test_value = 22
print(test_value)
test_value = "Joana"
print(test_value)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4: multi-part</B></font> 
# ## Assign a variable and print the value
# - assign a string value to a variable **`student_name`**
# - print the value of variable **`student_name`**

# In[13]:


# [ ] assign a string value to a variable student_name
student_name = 'James'

# [ ] print the value of variable student_name
print(student_name)


# <font size="3" color="#B24C00"  face="verdana"> <B>Tasks 4 cont...</B></font> 
# ##  modified the value of a variable
# - assign the **`student_name`** variable  a different string value (a different name)
# - print the value of variable **`student_name`**
# - assign and print a 3rd value to **`student_name`**

# In[14]:


# [ ] assign the student_name variable  a different string value (a different name)
student_name = 'Joana'
# [ ] print the value of variable student_name
print(student_name)
# [ ] assign a 3rd different string value, to the variable name 
student_name = 'Mark'
# [ ] print the value of variable name
print(student_name)


# <font size="3" color="#B24C00"  face="verdana"> <B>Tasks 4 cont...</B></font> 
# ##  change variable type with reassignment
# - assigning a value to a variable called **`bucket`**
# - print the value of **`bucket`**
# - assign an Integer value (no quotes) to the variable **`bucket`**
# -  print the value of **`bucket`** 

# In[16]:


# [ ] assigning a value to a variable called bucket
bucket = '3'
# [ ] print the value of bucket 
print(bucket)
# [ ] assign an Integer value (no quotes) to the variable bucket
bucket = 5
# [ ] print the value of bucket 
print(bucket)


# ## Q?: What is the difference between `123` and  `'123'`?  
#   
# **A:** A String type **is not** a number, even if it  is all numeric digits
# * in Python code a number can be assigned to a variable: `x = 31`
# * a string of digits can be assigned to the variable **`id`**&nbsp; --> `id = "001023"`&nbsp; the quotations, mean the number symbols should be stored in the variable as **type** string, meaning the digits&nbsp;"`001023`"&nbsp; are treated as text
#     
# The **`print()`** function can print Integer or string values:
# ```python
# print(123) #integer, with numeric value
# print("123") #string, represents text characters
# ```  
# <font size="3" color="#B24C00"  face="verdana"> <B>Tasks 4 cont...</B></font> 
# - run the above code the next cell:  

# In[17]:


# [ ] print integer 123 number
print(123)
# [ ] print string "123" number
print('123')


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; ?? 2017 Microsoft
