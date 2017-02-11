# Program Instance
# will need to write to JSON file
from user_information import security
import * from pytesseract

class Program:
    def __init__(self):
        self.setup()

    def setup(self):
        print("Welcome to Community Care\n")
        security()

    def process_attendance(self, attendance):
        # After being processed using OCR, an image is parsed for its type  for




    class Menu():
        self.options = ["HELP", "ADD_STUDENT", "DROP_STUDENT", "MAIN_MENU",
                    "SEARCH"]

        # How do we handle the security piece?
        # We will worry about this when we get to flask it will only the
        # Site Captain can login for the MVP

        # login = input("Login: ")
        # if login in usernames:
        #     password = input("Password: ")
        #     if password in passwords:
        #         break
        #     else:
        #         security()
