#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

def create_login(email,name,username,password):
    """
    function to create a new account for password locker
    """
    new_user=User(email,name,username,password)
    return new_user

def save_login(user):
    """
    Function to save user login details
    """
    user.save_login()

def create_existing_credentials(social_app_name ,app_username , app_password):
    """
    function to create existing credentials accounts 
    """
    new_credential=Credentials(social_app_name ,app_username , app_password)
    return new_credential

def save_credentials(credential):
    """
    function to save credentials
    """
    credential.save_credentials()

def delete_credential(credential):
    """
    function to delete credentials
    """
    credential.delete_credential()


