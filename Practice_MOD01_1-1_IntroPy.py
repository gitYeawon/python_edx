#!/usr/bin/env python
# coding: utf-8

# # 1-1 Intro Python Practice
# ##  Getting started with Python in Jupyter Notebooks
# ### notebooks, comments, print(), type(), addition, errors and art
# 
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - use Python 3 in Jupyter notebooks
# - write working code using `print()` and `#` comments  
# - write working code using `type()` and variables
# - combine strings using string addition (+)
# - add numbers in code (+)
# - troubleshoot errors
# - create character art  
# 
# # &nbsp;
# >**note:** the **[ ]** indicates student has a task to complete  
#   
# >**reminder:** to run code and save changes: student should upload or clone a copy of notebooks 
# 
# #### notebook use
# - [ ] insert a **code cell** below   
# - [ ] enter the following Python code, including the comment: 
# ```python 
# # [ ] print 'Hello!' and remember to save notebook!
# print('Hello!')
# ```
# Then run the code - the output should be:  
# `Hello!`

# In[1]:


print('Hello!')


# #### run the cell below   
# - [ ] use **Ctrl + Enter**  
# - [ ] use **Shift + Enter**    

# In[3]:


print('watch for the cat')


# #### Student's Notebook editing
# - [ ] Edit **this** notebook Markdown cell replacing the word "Student's" above with your name
# - [ ] Run the cell to display the formatted text
# - [ ] Run any 'markdown' cells that are in edit mode, so they are easier to read

# #### [ ] convert \*this\* cell from markdown to a code cell, then run it  
# print('Run as a code cell')
# 

# ##  # comments
# create a code comment that identifies this notebook, containing your name and the date

# In[4]:


# It's my idea!


# #### use print() to 
# - [ ] print [**your_name**]
# - [ ] print **is using python!**

# In[5]:


# [ ] print your name
print('Yeawon')

# [ ] print "is using Python"
print('is using Python!')


# Output above should be:  
# `Your Name  
# is using Python!`  

# #### use variables in print()
# - [ ] create a variable **your_name** and assign it a string containing your name
# - [ ] print **your_name**

# In[6]:


# [ ] create a variable your_name and assign it a sting containing your name
your_name = 'yeawon'
#[ ] print your_name
print(your_name)


# #### create more string variables
# - **[ ]** create variables as directed below
# - **[ ]** print the variables

# In[7]:


# [ ] create variables and assign values for: favorite_song, shoe_size, lucky_number

favorite_song = "let's do it"
shoe_size = "235"
lucky_number = "Doesn't Exist "
# [ ] print the value of each variable favorite_song, shoe_size, and lucky_number

print(favorite_song)
print(shoe_size)
print(lucky_number)


# #### use string addition
# - **[ ]**  print the above string variables (favorite_song, shoe_size, lucky_number) combined with a description by using **string addition**
# >for example favorite_song displayed as:  
# `favorite song is happy birthday`

# In[8]:


# [ ] print favorite_song with description
print("favorite song is "+favorite_song)

# [ ] print shoe_size with description
shoe_size = "235"
print("shoe size is " +shoe_size)

# [ ] print lucky_number with description
print("lckcy number is "+lucky_number)


# ##### more string addition
# - **[ ]** make a single string (sentence) in a variable called favorite_lucky_shoe using **string addition** with favorite_song, shoe_size, lucky_number variables and other strings as needed 
# - **[ ]** print the value of the favorite_lucky_shoe variable string
# > sample output:  
# `For singing happy birthday 8.5 times, you will be fined $25`

# In[9]:


# assign favorite_lucky_shoe using
favorite_lucky_shoe = favorite_song + shoe_size + lucky_number
print(favorite_lucky_shoe)


# ### print() art

# #### use `print()` and the asterisk **\*** to create the following shapes
# - [ ] diagonal line  
# - [ ] rectangle  
# - [ ] smiley face

# In[14]:


# [ ] print a diagonal using "*"
print("*")

# [ ] rectangle using "*"
print("    *")
print("  *   *" )
print("*********")



# [ ] smiley using "*"
print("  *   *" )
print("" )
print(" *     *" )
print("  *   *" )
print("   ***" )



# #### Using `type()`
# -**[ ]** calulate the *type* using `type()`

# In[15]:


# [ ] display the type of 'your name' (use single quotes)

your_name = 'yeawon'
type(your_name)


# In[16]:


# [ ] display the type of "save your notebook!" (use double quotes)
yell = "save your notebook!"
type(yell)


# In[17]:


# [ ] display the type of "25" (use quotes)


a = "25"
type(a)


# In[19]:


# [ ] display the type of "save your notebook " + 'your name'

a = "save your notebook" + 'your name'
type(a)


# In[20]:


# [ ] display the type of 25 (no quotes)

a = 25
type(a)


# In[21]:


# [ ] display the type of 25 + 10 

a = 25 + 50
type(a)


# In[22]:


# [ ] display the type of 1.55
a = 1.55
type(a)


# In[23]:


# [ ] display the type of 1.55 + 25

a = 1.55 + 25
type(a)


# #### Find the type of variables
# - **[ ]** run the cell below to make the variables available to be used in other code
# - **[ ]** display the data type as directed in the cells that follow

# In[25]:


# assignments ***RUN THIS CELL*** before starting the section

student_name = "Gus"
student_age = 16
student_grade = 3.5
student_id = "ABC-000-000"


# In[26]:


# [ ] display the current type of the variable student_name

type(student_name)


# In[27]:


# [ ] display the type of student_age
type(student_age)


# In[28]:


# [ ] display the type of student_grade
type(student_grade)


# In[29]:


# [ ] display the type of student_age + student_grade

type(student_age+student_grade)


# In[30]:


# [ ] display the current type of student_id

type(student_id)


# In[31]:


# assign new value to student_id 

student_id = 123456

# [ ] display the current of student_id

print(student_id)


# #### number integer addition
# 
# - **[ ]** create variables (x, y, z) with integer values

# In[ ]:


# [ ] create integer variables (x, y, z) and assign them 1-3 digit integers (no decimals - no quotes)
x = 5
y = 39
z = 1


# - **[ ]** insert a **code cell** below
# - **[ ]** create an integer variable named **xyz_sum** equal to the sum of x, y, and z
# - **[ ]** print the value of **xyz_sum** 

# In[32]:


xyz_sum = x + y + z
print(xyz_sum)


# ### Errors
# - **[ ]** troubleshoot and fix the errors below

# In[31]:


# [ ] fix the error 

print("Hello World!")    



# In[30]:


# [ ] fix the error 
print("strings have quotes and variables have names")


# In[28]:


# [ ] fix the error 
print( "I have $" + "5")


# In[27]:


# [ ] fix the error 
print('always save the notebook')
      


# ## ASCII art
# - **[ ]** Display first name or initials as ASCII Art
# - **[ ]** Challenge: insert an additional code cell to make an ASCII picture

# In[ ]:


# [ ] ASCII ART



# In[ ]:


# [ ] ASCII ART


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
