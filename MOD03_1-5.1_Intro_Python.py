#!/usr/bin/env python
# coding: utf-8

# # 1-5.1 Python Intro  
# ## conditionals, type, and mathematics extended  
# - **conditionals: `elif`**
# - **casting**  
# - basic math operators  
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - **code more than two choices using `elif`** 
# - **gather numeric input using type casting**  
# - perform subtraction, multiplication and division operations in code 
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## conditional `elif`
# 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a2ac5f4b-0400-4a60-91d5-d350c3cc0515/Unit1_Section5.1-elif.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/a2ac5f4b-0400-4a60-91d5-d350c3cc0515/Unit1_Section5.1-elif.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### a little review  
# - **`if`** means "**if** a condition exists then do some task." **`if`** is usually followed by **`else`**  
# - **`else`** means "**or else** after we have tested **if**, then do an alternative task"  
# 
# When there  is a need to test for multiple conditions there is&nbsp; **`elif`**
# - **`elif`**&nbsp; statement follows &nbsp;**`if`**, and means **"else, if "** another condition exists do something else
# - **`elif`**&nbsp; can be used many times
# - **`else`**&nbsp; is used after the last test condition (**`if`** or **`elif`**)
# 
# #### in psuedo code  
# **If** it is raining bring an umbrella  
# or **Else If** &nbsp;(`elif`) it is snowing bring a warm coat  
# or **Else** go as usual  
# 
# Like **`else`**, the **`elif`** only executes when the previous conditional is False

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[ ]:


# [ ] review the code then run testing different inputs
# WHAT TO WEAR
weather = input("Enter weather (sunny, rainy, snowy): ") 

if weather.lower() == "sunny":
    print("Wear a t-shirt")
elif weather.lower() == "rainy":
    print("Bring an umbrella and boots")
elif weather.lower() == "snowy":
    print("Wear a warm coat and hat")
else:
    print("Sorry, not sure what to suggest for", weather)


# In[ ]:


# [ ] review the code then run testing different inputs
# SECRET NUMBER GUESS
secret_num = "2"

guess = input("Enter a guess for the secret number (1-3): ")

if guess.isdigit() == False:
    print("Invalid: guess should only use digits")
elif guess == "1":
    print("Guess is too low")
elif guess == secret_num:
    print("Guess is right")
elif guess == "3":
    print("Guess is too high")
else:
    print(guess, "is not a valid guess (1-3)")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# 
# ## Program: Shirt Sale
# ### Complete program using &nbsp; `if, elif, else`
# - Get user input for variable size (S, M, L)
# - reply with each shirt size and price (Small = \$ 6, Medium = \$ 7, Large = \$ 8)
# - if the reply is other than S, M, L, give a message for not available
# - *optional*: add additional sizes

# In[2]:


# [ ] code and test SHIRT SALE


size = input("What size? (S,M,L): ").upper()

if not size.isalpha() :
    print("Please Choose S, M, L")
    
elif size == "S" :
    print("Cost: 6$")
    
elif size == "M" :
    print("Cost: 7$")
    
elif size == "L" :
    print("Cost: 8$")


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## casting
# Casting is the conversion from one data type to another Such as converting from **`str`** to **`int`**.
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4cbf7f96-9ddd-4962-88a8-71081d7d5ef6/Unit1_Section5.1-casting-input.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/4cbf7f96-9ddd-4962-88a8-71081d7d5ef6/Unit1_Section5.1-casting-input.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# ### `int()`
# the **`int()`** function can convert stings that represent whole counting numbers into integers and strip decimals to convert float numbers to integers
# - `int("1") = 1` &nbsp; the string representing the integer character `"1"`, cast to a number 
# - `int(5.1) = 5` &nbsp; the decimal (float), `5.1`, truncated into a non-decimal (integer)  
# - `int("5.1") = ValueError` &nbsp; `"5.1"` isn't a string representation of integer, `int()` can cast only strings representing integer values   
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[3]:


weight1 = '60' # a string
weight2 = 170 # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## casting with `int()` & `str()`

# In[10]:


str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result

add = int(str_num_1) + int(str_num_2) + int_num_3

print(add)


# In[11]:


str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as test strings and print the result


# <font size="4" color="#B24C00"  face="verdana"> <B>Task 2 cont...</B></font>
# ### Program: adding using `int` casting
# - **[ ]** initialize **`str_integer`** variable to a **string containing characters of an integer** (quotes)   
# - **[ ]** initialize **`int_number`** variable with an **integer value** (no quotes)
# - **[ ]** initialize **`number_total`** variable and **add int_number + str_integer** using **`int`** casting
# - **[ ]** print the sum (**`number_total`**)

# In[14]:


# [ ] code and test: adding using int casting
str_integer = "2"
int_number = 10
number_total = int(str_integer) + int_number
print(number_total)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## `input()`  strings that represent numbers can be "cast" to integer values
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[15]:


# [ ] review and run code
student_age = input('enter student age (integer): ')
age_next_year = int(student_age) + 1
print('Next year student will be',age_next_year)


# In[16]:


# [ ] review and run code
# cast to int at input
student_age = int(input('enter student age (integer): '))

age_in_decade = student_age + 10

print('In a decade the student will be', age_in_decade)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3</B></font>
# ## Program: adding calculator
# - get input of 2 **integer** numbers 
# - cast the input and print the input followed by the result
#   - Output Example: **`9 + 13 = 22`**  
# 
# Optional: check if input .isdigit() before trying integer addition to avoid errors in casting invalid inputs

# In[20]:


# [ ] code and test the adding calculator

num1 = int(input("Enter a number: "))
num2 = int(input("Ehter a number: "))

print("The calculation Will be", num1, "+", num2, "=" , num1 + num2 )


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
