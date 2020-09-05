import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):
    """
    test class for users behaviours
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user=User("britcommentator@gmail.com","Ted","Thanos11","****")

if __name__ == '__main__':
    unittest.main()