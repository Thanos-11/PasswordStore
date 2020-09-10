import unittest
from credentials import Credentials
import pyperclip

class  TestCredentials(unittest.TestCase):
    """
    test class for credentials behaviours
    """
    def setUp(self):
        """
        set up method to run before each test
        """
        self.new_credentials=Credentials("instagram","jesuisTed","123456")

    def test_init(self):
        """
        to check if the objects are initialised correctly
        """
        self.assertEqual(self.new_credentials.social_app_name,"instagram")
        self.assertEqual(self.new_credentials.app_username,"jesuisTed")
        self.assertEqual(self.new_credentials.app_password,"123456")

    def test_save_credentials(self):
        """
        test case to check if the objects are being saved in the credentials_list
        """
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
        """
        does a clean up after each test case has been done 
        """
        Credentials.credentials_list=[]

    def test_save_multiple_credentials(self):
        """
        test case to check if more credentials can be saved
        """
        self.new_credentials.save_credentials()
        test_credential=Credentials("facebook","j.suisTed","122345")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credential(self):
        """
        test case to check if we can delete credentials
        """
        self.new_credentials.save_credentials()
        test_credential=Credentials("facebook","k.murimi","password123")
        test_credential.save_credentials()

        test_credential.delete_credential()
        self.assertEqual(len(Credentials.credentials_list),1)

    # def test_find_social_by_app_name_and_username(self):
    #     """
    #     test to check if we can find app name and username and display their passwords
    #     """
    #     self.new_credentials.save_credentials()
    #     test_credential=Credentials("facebook","j.suisTed","122345")
    #     test_credential.save_credentials()
    #     # test_credential2=Credentials("facebook","Ted.mwangi","12345password")
    #     # test_credential2.save_credentials()

    #     found_account=Credentials.find_account("facebook","j.suisTed")
    #     self.assertEqual(found_account.app_username,test_credential.app_username)

    def test_find_social_by_app_name(self):
        """
        test to check if we can find app name and display their passwords
        """
        self.new_credentials.save_credentials()
        test_credential=Credentials("facebook","j.suisTed","122345")
        test_credential.save_credentials()
        test_credential2=Credentials("facebook","Ted.mwangi","12345password")
        test_credential2.save_credentials()

        found_account=Credentials.find_account("facebook")
        self.assertEqual(found_account.app_username,test_credential.app_username)

    def test_credentials_exist(self):
        """
        test to check if a credential exist
        """
        self.new_credentials.save_credentials()
        test_credential=Credentials("facebook","j.suisTed","122345")
        test_credential.save_credentials()

        credentials_exist=Credentials.credential_exist("j.suisTed")
        self.assertTrue(credentials_exist)

    def test_display_credentials(self):
        """
        test to show the credentials to the user
        """
        
        self.assertEqual(Credentials.credential_display(),Credentials.credentials_list)

if __name__=='__main__':
    unittest.main()