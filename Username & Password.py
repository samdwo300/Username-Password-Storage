# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:05:29 2020

I would like to create a GUI for this at some point, maybe using TKinter? 

@author: samdw
"""
import numpy as np
import  pandas as pd
import matplotlib as plt
import random as rd



# Create empty dataframe to store usernames/password
dictionary = {'Username': [] , 'Password': []}
dataframe = pd.DataFrame(data = dictionary, columns = ['Username','Password'] )


# Function that determines if the username entered is valid (not already in the list of current usernames)
def valid_user_name(user_name):
    for i in dataframe['Username']:
        if i == user_name:
            return True
            break
        else:
            continue
    return False

# Function that determines if the password is correct for a given username
def valid_password(password):
    for i in dataframe['Password']:
        if i == password:
            return True
            break
        else:
            continue
    return False

# Function that determines if the entered username has already been taken 
def existing_username():
    for i in dataframe['Username']:
        if i == user_name:
            return True
            break
        else:
            continue
    return False



prompt_1 = input("Have you created a username/password (Y/N)")
if prompt_1 == "Y":
    username = input("Enter Username: ")
    while valid_user_name(user_name) == False:
        user_name = input("Invalid username please try again: ")
        if valid_user_name(user_name) == True:
            break
    password = input("Enter Password: ")
    while valid_password(password) == False:
        password = input("Invalid username please try again: ")
        if valid_password(password) == True:
            break
elif prompt_1 == "N":
    user_name = input("Create Username: ")
    while valid_user_name(user_name) == True:
        user_name = input("Username already exists please enter a new username: ")
        if valid_password(password) == False:
            break
    password = input("Create Password: ")
    dataframe = dataframe.append({'Username': user_name, 'Password':password}, ignore_index = True)
    
    
    


















