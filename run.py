#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

def create_login(email,name,username,password):
    """
    function to create a new account for password locker
    """
    new_user=User(email,name,username,password)
    return new_user

