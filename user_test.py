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

def test_init(self):
        """
        test case to see if the objects are initialised corectly
        """
        self.assertEqual(self.new_user.email,"britcommentator@gmail.com")
        self.assertEqual(self.new_user.name,"Ted")
        self.assertEqual(self.new_user.username,"Thanos11")
        self.assertEqual(self.new_user.password,"****")        

if __name__ == '__main__':
    unittest.main()