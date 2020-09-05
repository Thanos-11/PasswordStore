class User:
    """
    a class for new users and login data
    """

    user_list=[]

 # created instance variables to take up email,name,username and password of user
 
    def __init__(self,email,name,username,password):
        self.email=email
        self.name=name
        self.username=username
        self.password=password
