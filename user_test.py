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

    def test_save_login(self):
        """
        test case to check if the objects are saved in the user list
        """
        self.new_user.save_login()
        self.assertEqual(len(User.user_list,),1)

    def test_user_auth(self):
        """
        test_user_auth tests case to authenticate the user
        """
        self.new_user.save_login()
        test_user=User("tedletheorde@gmail.com","Theorde","Mosalah","1234password")
        test_user.save_login()
        self.assertTrue(self.new_user.user_auth("Mosalah","1234password"))
    

if __name__ == '__main__':
    unittest.main()