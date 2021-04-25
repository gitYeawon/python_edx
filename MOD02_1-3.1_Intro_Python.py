#!/usr/bin/env python
# coding: utf-8

# # 1-3.1 Intro Python
# ## Functions Arguments & Parameters
# - **Creating a simple Function with a parameter**
# - Exploring Functions with `return` values 
# - Creating Functions with multiple parameters
# - Sequence in python  
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - **create functions with a parameter**  
# - create functions with a `return` value 
# - create functions with multiple parameters
# - use knowledge of sequence in coding tasks  
# - Use coding best practices 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## Calling Functions with Arguments
# Functions are used for code tasks that are intended to be reused 
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/621d10f8-23d5-4571-b0fd-aa12b0de98d8/Unit1_Section3.1-function-arguments.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/621d10f8-23d5-4571-b0fd-aa12b0de98d8/Unit1_Section3.1-function-arguments.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# 
# Python allows us to create **User Defined Functions** and provides many **Built-in Functions** such as **`print()`**  
# - **`print()`** can be called using arguments (or without) and sends text to standard output, such as the console. 
# - **`print()`** uses **Parameters** to define the variable Arguments that can be passed to the Function. 
# - **`print()`** defines multiple string/numbers parameters which means we can send a long list of Arguments to **`print()`**, separated by commas.   
# - **`print()`** can also be called directly with just its name and empty parentheses and it will return a blank line to standard output

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[ ]:


print('Hello World!', 'I am sending string arguments to print ')


# In[3]:


student_age = 17
student_name = "Hiroto Yamaguchi"
print(student_name,'will be in the class for',student_age, 'year old students.')


# In[1]:


print("line 1")
print("line 2")
# line 3 is an empty return - the default when no arguments
print()
print("line 4")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## Passing Arguments to &nbsp; `print()` 
# ### Many Arguments can be passed to print 
# 
# - update the print statement to use **`print()`** with **8** or more arguments

# In[2]:


#[ ] increase the number of arguments used in print() to 8 or more 
student_age = 17
student_name = "Hiroto Yamaguchi"
print(student_name,'will be in the class for',student_age, 'year old students.')


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## Create a simple Function
# Creating user defined functions is at the core of computer programming.  Functions enable code reuse and make code easier to develop and maintain.
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/35458114-6211-4d10-85bc-7c4eb7834c52/Unit1_Section3.1-Simplest_Functions.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/35458114-6211-4d10-85bc-7c4eb7834c52/Unit1_Section3.1-Simplest_Functions.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### basics of a user defined function
# - define a function with **`def`** 
# - use indentation (4 spaces)
# - define parameters
# - optional parameters 
# - **`return`** values (or none)
# - function scope (basics defaults)  
# 

# ### `def some_function():`
# use the &nbsp;**`def`** &nbsp;statement when creating a **function**  
# - use a function name that **starts with a letter** or underscore (usually a lower-case letter)
# - function names can contain **letters, numbers or underscores**
# - parenthesis &nbsp; **()**  &nbsp; follow the function name
# - a colon &nbsp; **:**  &nbsp; follows the parenthesis
# - the code for the function is indented under the function definition (use 4 spaces for this course)
# 
# ```python
# def some_function():
#    #code the function tasks indented here    
# ```
# The **end of the function** is denoted by returning to **no indentation**

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[7]:


# defines a function named say_hi
def say_hi():
    print("Hello there!")
    print("goodbye")


# In[5]:


# define three_three 
def three_three():
    print(33) 


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## Call a function by name
# Call a simple function using the function name followed by parenthesis.  For instance, calling print is  
# **`print()`**

# ## &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[8]:


# Program defines and calls the say_hi & three_three functions
# [ ] review and run the code

def say_hi():
    print("Hello there!")
    print("goodbye")
# end of indentation ends the function

# define three_three 
def three_three():
    print(33) 

# calling the functions
say_hi()
print()
three_three()


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## Define and call a simple function &nbsp; `yell_it()` 
# ### `yell_it()` &nbsp; prints the phrase with "!" concatenated to the end
# - takes no arguments
# - indented function code does the following
#   - define a variable for called **`phrase`** and intialize with a short *phrase*
#   - prints **`phrase`** as all upper-case letters followed by "!"
# - call &nbsp; `yell_it` &nbsp; at the bottom of the cell after the function &nbsp;**`def`**&nbsp; (**Tip:** no indentation should be used)

# In[13]:


#[ ] define (def) a simple function called yell_it() and call the function
def yell_it():
    print("ya ho !".upper())

yell_it()


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concept</B></font>
# ## Functions that have Parameters
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c84008fa-2ec9-4e4b-8b6b-15b9063852a1/Unit1_Section3.1-funct-parameter.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/c84008fa-2ec9-4e4b-8b6b-15b9063852a1/Unit1_Section3.1-funct-parameter.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# **`print()`** and **`type()`** are examples of built-in functions that have **Parameters** defined  
#   
# **`type()`** has a parameter for a **Python Object** and sends back the *type* of the object
#   
# an **Argument** is a value given for a parameter when calling a function  
# - **`type`** is called providing an **Argument** - in this case the string *"Hello"*
# ```python
# type("Hello")
# ```  
# 
# ## Defining Function Parameters
# - Parameters are defined inside of the parenthesis as part of a function **`def`** statement
# - Parameters are typically copies of objects that are available for use in function code
# ```python
# def say_this(phrase):  
#       print(phrase)
# ```  
# 
# ## Function can have default Arguments
# - Default Arguments are used if no argument is supplied
# - Default arguments are assigned when creating the parameter list
# ```python
# def say_this(phrase = "Hi"):  
#       print(phrase)
# ```

# ## &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[16]:


# yell_this() yells the string Argument provided
def yell_this(phrase):
    print(phrase.upper() + "!")
    
# call function with a string
yell_this("It is time to save the notebook")

def yell_this_too(sentence):
    print(sentence.upper() + "!")
    
yell_this_too("you are too loud")


# In[18]:


# use a default argument
def say_this(phrase = "Hi"):  
    print(phrase)
        
say_this("no way")
say_this("Bye")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# 
# ## Define `yell_this()` and call with variable argument 
# - define variable &nbsp; **`words_to_yell`** &nbsp; as a string gathered from user&nbsp; `input()`
# - Call &nbsp;**`yell_this()`** &nbsp;with &nbsp; **`words_to_yell`** &nbsp;as argument
# - get user input() for the string words_to_yell

# In[ ]:


# [ ] define yell_this() 
def yell_this():
    word_to_yell = input()
# [ ] get user input in variable words_to_yell
yell_this()
# [ ] call yell_this function with words_to_yell as argument


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
