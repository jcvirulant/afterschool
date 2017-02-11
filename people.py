# Class for people with in the project
# Will have subclasses for all other "types"
# Put placeholders for inputs
import datetime
import regex as r


class Person(object):
    """Person contains data to be gathered on Communities.
    Person is a parent class for Teachers, Students, Guardians,
    Authorized persons, and Counselors."""
    def __init__(self, arg):
        super(Persons, self).__init__()
        self.firstname = input("Enter {}'s First Name: ".format(self.str))
        self.lastname = input("Enter {}'s Last Name: ")
        self.address = input("Enter {}'s Address: ")
        self.birthdate = datetime.date(input("Enter {}'s Birthdate: "))
        self.age = datetime.now()-self.birthdate

# Create a sub class for a student


class Student(Person):
    """Students are a subclass of Person. Students are assigned to Pods.
        Students are assigned: teachers, guardians, authorized persons,
        counselors."""

    def __init__(self, arg):
        self.guardian = Gaurdian()
        self.authorized1 = Authorized_Pickup()
        self.authorized2 = Authorized_Pickup()
        self.counselor = Counselor()
        self.nickname = input("Enter Student's Nickname: ")
        self.grade = 0
        self.teacher = Teacher()
        self.attendance_record = A_Record()
        self.fitness_record = F_Record()


class Authorized_Pickup(Person):
    """Authorized_Pickup a parent of Guardian, Student, Counselor. """

    def __init__(self, arg):
        self.phone_number = get_phone()

    def get_phone(self):
        # use regex to verify phone_number
        pass

class Guardian(Person):
    """Guardians are a subclass of Authorized_Pickup.  Guardians have students"""


class Teacher(Person):
    """Teachers are a subclass of Person. Teachers are assigned to: Students.
        Teachers are assigned Courses."""

    def __init__(self, **kwargs):
        self.site = siteselect()
        self.course = courseselect()

class Team_Member(Person):
    self.name = name

    def __init__(self, **kwargs):
        self.type = type()

    def type(self):
        type = input("What type of Team Member is {}? [C]aptain, "
                     "[S]pecialist, or [G]uide\n".format(name))
        if type == "P":
            self.pod = Pod()
        elif type == "C":
            self.site = siteselect()
