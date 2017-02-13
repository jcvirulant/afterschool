import json


class Form(object):

    def __init__(self, args):
        super(Forms, self).__init__()
        self.form_type = 'f'
        self.form_number = 0


class Application(Form):
    """The Application class takes an input from the tessaract to build a form
        to be reviewed by a director.  After it has been reviewed and verified,
        the Application Class Creates Students, Guardians, etc """
    def __init__(self, args):
        self.form_type = 'app'
        # Get unique number... there is a special module for this.
        self.form_number = 0
        self.student_name = [lname, fname, mname]
