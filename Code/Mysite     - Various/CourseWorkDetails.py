from os import getcwd
from sys import exit

try:
    from passlib.hash import pbkdf2_sha256
except:
    print "Can't import the library needed, please run 'pip install -r " + getcwd() + "\\requirements.txt'"
    exit(0)
# This attempts to import the password hashing, and otherwise exits.


class CourseworkDetail:
    """Class for the coursework details."""
    def __init__(self, moduleCode, moduleTitle, moduleTutor, cwNumber, cwTitle, dateIssued, dateDue, assessType,
                 moduleMark):
        # Initial a new instance of a class with the module info.
        self.moduleCode = moduleCode
        self.moduleTitle = moduleTitle
        self.moduleTutor = moduleTutor
        self.cwNumber = cwNumber
        self.cwTitle = cwTitle
        self.dateIssued = dateIssued
        self.dateDue = dateDue
        self.assessType = assessType
        self.moduleMark = moduleMark
        self.studentID = None
        self.studentName = None

    def assignStudentDetails(self, studentID, studentName):
        # Allows you to save the student id and name.
        self.studentID = studentID
        self.studentName = studentName

    def displayStudentInfo(self):
        # Print out the student ID and Name.
        if self.studentID and self.studentName:
            print "studentID : ", self.studentID, ", Name: ", self.studentName
        else:
            print "No student info found for this student."


# Quick log in system that tells you if pw is correct to show off hashing function.
if __name__ == "__main__":
    # Only runs if it is run directly, not imported into another file.
    while True:
        print "Press 1 to log in."
        print "Press 2 to create an account."
        print "Press 3 to exit."
        # Print out a menu

        try:
            userInput = int(input(""))
        # This code checks that the answer input is an int. This helps prevent malicious code from being injected into the program.
        except:
            print "Not an integer"
            continue

        if userInput == 1:
            print "Log in"
            userInputUser = raw_input("Enter your username: ")
            userInputPass = raw_input("Enter your password: ")
            # Allows the user to input a username and a password
            try:
                target = open(userInputUser + '.txt', 'r+')
                hash1 = target.read()
                # Opens their username text file and reads it.
            except:
                print "You don't have an account, please make one."
                # If there is no textfile with their username, tells them.
                continue
            if pbkdf2_sha256.verify(userInputPass, hash1):
                # Checks the hashed password against the saved one.
                print "correct password"
            else:
                print "wrong password"
            break

        elif userInput == 2:
            # Allows the user to create an account with a username and password.
            print "Create account"
            userInputUser = raw_input("Enter a username: ")
            userInputPass = raw_input("Enter a password: ")
            hash1 = pbkdf2_sha256.encrypt(userInputPass, rounds=200000)
            # Hashes the password
            target = open(userInputUser+'.txt', 'w')
            target.write(hash1)
            # Writes their password to a text file called their username
            target.close()
            break

        elif userInput == 3:
            # Exits the program.
            print "exit"
            exit(0)

        else:
            print "Integer not 1/2/3"

    cw1 = CourseworkDetail("code1", "title1", "tutor1", "number1", "cwtitle1", "issued1", "due1", "type1", "mark1")
    cw2 = CourseworkDetail("code2", "title2", "tutor2", "number2", "cwtitle2", "issued2", "due2", "type2", "mark2")
    cw3 = CourseworkDetail("code3", "title3", "tutor3", "number3", "cwtitle3", "issued3", "due3", "type3", "mark3")
    # Tests the class creation, creates three instances of the class.

    cw1.assignStudentDetails("Test1", "cw1")
    cw2.assignStudentDetails("Test2", "cw2")
    # Adds two test students to two instances of the class.

    cw1.displayStudentInfo()
    cw2.displayStudentInfo()
    cw3.displayStudentInfo()
    # Prints out the student info from the class instances.
