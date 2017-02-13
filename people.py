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
        self.firstname = input("Enter {}'s First Name: ".format(self.type))
        self.lastname = input("Enter {}'s Last Name: ".format(self.type))
        self.address = input("Enter {}'s Address: ".format(self.type))
        self.birthdate = datetime.date(input("Enter {}'s Birthdate: "))
        self.age = round(int(datetime.now()-self.birthdate))

    def object_decoder(obj):
        if '__type__' in obj and obj['__type__'] == 'User':
            return Student(
                obj['lastname'],
                obj['firstname'],
                obj['middlename']
                )

        return obj

    # json.loads('{"__type__": "Student", "lastname": "Smith",
    # "firstname": "John"}', object_hook=object_decoder)

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

    def get_pickups(self):
        print(authorized1)

    class A_Record():
        """The A Record contains the attendance for a student and the functions
            for processing statistical data."""
        # Lists of datetimes
        self.absent_days = []
        self.tardy_days = []
        self.left_early_days = []

    class H_Record():
        """Contains all of the student's fitness records and assesments,
            nutrition records and assesments, health concerns etc.  It also
            contains functions to add, pull records, show progress
            over time.  It will also help to aggregate data on all the students
            when we put everything in a database."""

    class B_Record():
        """The B Record contains behavioral data including the Dessa and
            other assessments for measuring the social and behavioral
            progress."""

    class E_Record():
        """The E or Education Record contains educational assessments """

class Authorized_Pickup(Person):
    """Authorized_Pickup a parent of Guardian, Student, Counselor. """

    def __init__(self, arg):
        self.phone_number = get_phone()

    def __str__(self):
        print(self.lname)
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
