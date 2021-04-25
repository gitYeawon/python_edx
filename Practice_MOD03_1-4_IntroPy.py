#!/usr/bin/env python
# coding: utf-8

# # 1-4.3 Intro Python Practice
# ## Conditionals 
# <font size="5" color="#00A0B2"  face="verdana"> <B>Student will be able to</B></font>  
# - **control code flow with `if`... `else` conditional logic**  
#   - using Boolean string methods (`.isupper(), .isalpha(), .startswith()...`)  
#   - using comparision (`>, <, >=, <=, ==, !=`)  
#   - using Strings in comparisons  

# ## `if else`
# 

# In[5]:


# [ ] input avariable: age as digit and cast to int
# if age greater than or equal to 12 then print message on age in 10 years 
# or else print message "It is good to be" age

age = input()

if int(age) >= 12: 
    print(age +" in 10 years")
else:
    print("It is good to be " + age)






# In[25]:


# [ ] input a number 
# if number IS a digit string then cast to int
# print number "greater than 100 is" True/False
# if number is NOT a digit string then message the user that "only int is accepted"

a = input()

if a.isalpha() :
    print("only int is accepted")
else :
    print("greater than 100 is ", int(a) >= 100)


# ### Guessing a letter A-Z  
# **check_guess()** takes 2 string arguments: **letter and guess** (both expect single alphabetical character)   
#     - if guess is not an alpha character print invalid and return False
#     - test and print if guess is "high" or "low" and return False
#     - test and print if guess is "correct" and return True

# In[9]:


# [ ] create check_guess()
# call with test

letter = "Y"

def check_guess(letter,guess) :
    
    
    if not guess.isalpha() :
        print(invaild)
        return False
    
    if guess == letter.upper() :
        print("correct")
        return True 
    
    elif guess > letter.upper() :
        print("high")
        return False
    
    elif guess < letter.upper() :
        print("low")
        return False


#def cheese_program(order_amount):
#
#    try:
#        order_amount = float(order_amount)
#    except ValueError:
#        print("Enter numeric value")
#        return

#    if order_amount > maximum_order:
#        print(order_amount, "is more than currently available stock")
#    elif order_amount < minimum_order:
#        print(order_amount, "is less than currently available stock")
#    else:
#        print(order_amount, "pounds costs", "$", int(order_amount) * 5)


# In[12]:


# [ ] call check_guess with user input

check_guess(letter,input())


# ### Letter Guess
# **create letter_guess() function that gives user 3 guesses**
# - takes a letter character argument for the answer letter
# - gets user input for letter guess  
# - calls check_guess() with answer and guess
# - End letter_guess if 
#     - check_guess() equals True, return True  
#     - or after 3 failed attempts, return False

# In[25]:


# [ ] create letter_guess() function, call the function to test

trial = 3

def letter_guess():
    
    for i in range(trial) :
        guess = input("Enter your guess: ").upper()
    
        if check_guess(letter,guess) == True :
            #print("correct!")
            return True
    return False

if letter_guess():
    print("Congratulations")
else:
    print("Game Over, The Answer Was ",letter)


# ### Pet Conversation
# **ask the user for a sentence about a pet and then reply**  
# - get user input in variable: about_pet
# - using a series of **if** statements respond with appropriate conversation
#   - check if "dog" is in the string about_pet (sample reply "Ah, a dog")
#   - check if "cat" is in the string about_pet
#   - check if 1 or more animal is in string about_pet
# - no need for **else**'s
# - finish with thanking for the story

# In[26]:


# [ ] complete pet conversation

about_pet = input().lower()

if about_pet == "dog" :
    
    print("Boring")
    
if about_pet == "cat" :
    
    print("Also Boring")

if about_pet == "spider" :
    
    print("😅")
    
if about_pet == "pig" :
    
    print("I can respect you")


# [Terms of use](http://go.microsoft.com/fwlink/?LinkID=206977) &nbsp; [Privacy & cookies](https://go.microsoft.com/fwlink/?LinkId=521839) &nbsp; © 2017 Microsoft
