#!/usr/bin/env python
# coding: utf-8

# # 1-6.1 Intro Python
# ## Nested Conditionals
# -  Nested Conditionals  
# - Escape Sequence print formatting "\\"
# 
# ><font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>
# - create nested conditional logic in code  
# - format print output using escape "\\" sequence 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Concepts</B></font>
# ## nested conditionals
# # Video: Unit1_Section6.1-nested-conditionals.mp4
# ### nested conditionals
# **if**  
# **&nbsp;&nbsp;&nbsp;&nbsp;if**  
# **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if**  
# **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else**  
# **&nbsp;&nbsp;&nbsp;&nbsp;else**  
# **else**  
# 
# ### Making a sandwich
# Taking a sandwich order starts with sandwich choices:
# > **Cheese or Veggie special?**  
# if the response is **"Cheese"** "nest" a sub ask:  
# >> **Manchego or Cheddar?**  
#   
#   
# |Nested &nbsp;**`if`**&nbsp; statement  flowchart  |
# | ------ | 
# | ![Image of sandwich order flowchart](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/flowchart_sandwich.png)   | 
# 

# # &nbsp;
# <font size="6" color="#00A0B2"  face="verdana"> <B>Examples</B></font>
# > ***TIP:*** click in input box before typing input 

# In[3]:


# simplified example
# [ ] review the code then run and following the flowchart paths

# ***TIP:*** click in input box before typing

sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')

if sandwich_type.lower() == "c":
    # select cheese type
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich")
    else:
        print("Here is your Manchego Cheese sandwich") 

else:
    print("Here is your Veggie Special")


# In[7]:


# full example: handling some invalid input and elif statement
# [ ] review the code then run following the flowchart paths including **invalid responses** like "xyz123"

# ***TIP:*** click in input box before typing

print("Hi, welcome to the sandwich shop.  Please select a sandwich.")
sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
# select sandwich type sandwich_type = input('"c" for Cheese or "v" for Veggie Special: ')
print()
    
if sandwich_type.lower() == "c":
    # select cheese type
    print("Please select a cheese.")
    cheese_type = input('"c" for Cheddar or "m" for Manchego: ')
    print()
    
    if cheese_type.lower() == "c":
        print("Here is your Cheddar Cheese sandwich.  Thank you.")
    elif cheese_type.lower() == "m":
        print("Here is your Manchego Cheese sandwich.  Thank you.") 
    else:
        print("Sorry, we don't have", cheese_type, "choice today.")

elif sandwich_type.lower() == "v":
    print("Here is your Veggie Special. Thank you.")
        
else:
    print("Sorry, we don't have", sandwich_type, "choice today.")
print()
print("Goodbye!")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 1</B></font>
# ## Nested `if` 
# ### [ ] Program: Say "Hello"
# - using nested **`if`**
#   
# |Say "Hello" flowchart  |
# | ------ | 
# |  ![Image: Say "Hello" flowchart](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/flowchart_say_hello.png) | 

# In[18]:


# [ ] Say "Hello" with nested if
# [ ] Challenge: handle input other than y/n

print("Hello")

greeting = input("Say 'Hello' y/n? ").lower()

if greeting == "y" :
    
    print("Please slect.. ")
    which_greeting = input("Full 'Hello?' y/n ").lower()
    
    if which_greeting == "y" :
        print("Hello")
    else :
        print("Hi")
        
else :
    print("(Friendly nod)")


# # &nbsp;
# <font size="6" color="#B24C00"  face="verdana"> <B>Task 2</B></font>
# ## Nested `if` - testing for `False`
# ### Program:  [ ] 3 Guesses
# - use nested if statements complete the flowchart code
# - create a **`birds`** string variable with the names of 1, 2, 3 or more birds to make it easier
# - get **`bird_guess`** input and use **`bird_guess in bird_names`** to generate Boolean True/False
# - if the the guess is wrong (**`False`**) create a sub test until the user has had 3 guesses
#   
# |3 Guesses ("Guess the Bird") flowchart  |
# | ------ | 
# | ![Image of Guess the Bird flowchart](https://iajupyterprodblobs.blob.core.windows.net/imagecontainer/flowchart_guess_the_bird.png)   | 

# In[28]:


# [ ] Create the "Guess the bird" program 

birds = "sparrow", "magpie", "eagle"

print("Guess the bird")
print("- It can fly")
bird_guess1 = input("1st try: ")

if not bird_guess1 in birds :
    
    print("Beep !! ")
    print("- Dark color")
    bird_guess2 = input("2nd try: ")
    
    if not bird_guess2 in birds :
        print("Beep !! ")
        print("- Bold") 
        bird_guess3 = input("3nd try: ")
        
        if not bird_guess3 in birds :
            print("Beep !!")
            print("out of tries")
        
        elif bird_guess3 in birds :
            print("Yes 3rd try! ")
   #         break
            
    elif bird_guess2 in birds :
        print("Yes 2nd try! ")
     #   break
            
elif bird_guess1 in birds :
    print("Yes! 1st try! ")
    #break


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft

# In[ ]:




