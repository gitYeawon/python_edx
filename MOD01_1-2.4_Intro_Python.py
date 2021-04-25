#!/usr/bin/env python
# coding: utf-8

# # 1-2.4 Intro Python
# ## Strings: input, testing, formatting
# - input() - gathering user input  
# - print() formatting   
# - Quotes inside strings 
# - Boolean string tests methods   
# - **String formatting methods**  
# - **Formatting string input()**  
# - **Boolean `in` keyword**  
# 
# -----
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - gather, store and use string `input()`  
# - format `print()` output  
# - test string characteristics  
# - **format string output**  
# - **search for a string in a string**  

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# ## String formatting methods
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/693e416c-ab73-4387-a0d2-5a47668ae4de/Unit1_Section2-4-String-Format_Methods.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/693e416c-ab73-4387-a0d2-5a47668ae4de/Unit1_Section2-4-String-Format_Methods.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# the following methods are applied to string objects
# - **.capitalize()** - capitalizes the first character of a string
# - **.lower()** - all characters of a string are made lowercase
# - **.upper()** - all characters of a string are made uppercase
# - **.swapcase()** - all characters of a string are made to switch case upper becomes lower and vice versa  
# - **.title()** - each 'word' separated by a space is capitalized

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>  
# ### String Formatting Methods

# In[1]:


print("ms. Browning is in her office.".capitalize())


# In[2]:


fav_color = "green"
print(fav_color.capitalize(), fav_color, fav_color,"and", fav_color.upper()+"!")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1: multi-part</B></font> 
# ### [ ] format with `.capitalize(), .lower(), .upper(), .swapcase()`
# > **Note:** use **print()**

# In[9]:


# [ ] get input for a variable, fav_food, that describes a favorite food
fav_food = input()

# [ ] display fav_food as ALL CAPS, used in a sentence

print(fav_food.upper())
# [ ] dispaly fav_food as all lower case, used in a sentence
print(fav_food.lower())

# [] display fav_food with swapped case, used in a sentence
print(fav_food.swapcase())

# [] display fav_food with capitalization, used in a sentence


print(fav_food.capitalize())


# In[18]:


fav_color = "Forest Green"
# [] display the fav_color variable as upper, lower, swapcase, and capitalize formatting in a single print() statement
print(fav_color.swapcase())


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## Formatting string input()
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/460107d8-5d62-432e-924b-a3c779b2e5c5/Unit1_Section2-4-Input-String_Formatting.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/460107d8-5d62-432e-924b-a3c779b2e5c5/Unit1_Section2-4-Input-String_Formatting.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# When storing input, sometimes a specific format is needed and formatting is applied to the **`input()`** function
# > **Note:** this technique overwrites the original user input in the variable with the formatted value 

# <font size="4" color="#00A0B2"  face="verdana"> <B>Example</B></font>

# In[19]:


# review and run code - test a capitalized color input
fav_color = input('What is your favorite color?: ').lower()
print(fav_color)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>  
# ### [ ] format &nbsp; ` input()` with ` .upper()`

# In[20]:


# [] input variable fav_color as upper
fav_color = input().upper()
# [] print fav_color

print(fav_color)


# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>  
# ## Boolean `in` keyword 
# [![view video](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/common/play_video.png)]( http://edxinteractivepage.blob.core.windows.net/edxpages/f7cff1a7-5601-48a1-95a6-fd1fdfabd20e.html?details=[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ef7e8587-8ce6-48a4-9a2f-fb0a09db287f/Unit1_Section2-4-Boolean-in.ism/manifest","type":"application/vnd.ms-sstr+xml"}],[{"src":"http://jupyternootbookwams.streaming.mediaservices.windows.net/ef7e8587-8ce6-48a4-9a2f-fb0a09db287f/Unit1_Section2-4-Boolean-in.vtt","srclang":"en","kind":"subtitles","label":"english"}])
# the **`in`** keyword can be used as a simple search returning **`True`** or **`False`** indication if a string is included in a target sequence.  
# ### comparing strings is case sensitive
# `'Hello'` is not the same as `'hello'`  

# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>

# In[21]:


# review and run code to test if a string is to be found in another string
menu = "salad, pasta, sandwich, pizza, drinks, dessert"
print('pizza' in menu)


# In[22]:


# review and run code to test case sensitive examples 
greeting = "Hello World!"
print("'hello' in greeting = ",'hello' in greeting)
print("'Hello' in greeting = ", 'Hello' in greeting)


# example below: **remove case sensitivity from a string comparison**

# In[23]:


# review and run code to test removing case sensitivity from a string comparison
greeting = "Hello World!"
print("'hello' in greeting = ",'hello' in greeting)
print("'Hello' in greeting = ", 'Hello' in greeting)
print("'hello' in greeting if lower used = ", 'hello'.lower() in greeting.lower())


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 3: multi-part</B></font>  
# **[ ] add code below** testing the **`menu`** string variable for `'pizza'`, `'soup'`, and `'dessert'` using keyword &nbsp; **`in`**
# - print each test on a separate line
# - print a description for each test &nbsp; (e.g. - "`Pizza in menu = True`")

# In[28]:


# [] print 3 tests, with description text, testing the menu variable for 'pizza', 'soup' and 'dessert'
menu = "salad, pasta, sandwich, pizza, drinks, dessert"

print('salad' in menu)
print('pizza' in menu)
print('soup' in menu)


# ## Program: What is on the menu
# ### [ ] Create a program where a user can check if an item is on the menu
# - store the user response in a variable menu_ask
# - use the menu from above and add some additional items
# - the program should be able to ignore case mismatch so that "hello" is found in "Hello World!"

# In[ ]:


# Create a program where the user supplies input to search the menu
menu = input("what do you want to eat")


# ### [ ] Challenge: Add to the menu
# - print the current menu
# - get user input for add_item variable
# - new_menu use string addition to add add_item to menu
# - print the new_menu
# testing
# - add a cell below add menu
# - check if an item is on the menu, check for previous items and the item you added

# In[32]:


# add to menu
current_meun = "pizza"
add_item = input("add")
new_menu = add_item+ ',' + menu
print(new_menu)


# In[33]:


# Testing Add to Menu - create user input to search for an item on the new menu

print('salad' in new_menu)


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 4</B></font>
# ## Fix The Error

# In[30]:


# [ ] fix the error
paint_colors = "red, blue, green, black, orange, pink"
print('Red in paint colors = ','red' in paint_colors)


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
