# Create the Team_Member subclass(Person)

from person import Person


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
