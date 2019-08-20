# use * to import everything
from BEGINNER.BreakingIntoModules.student import *


class HihSchoolStudent(Student):
    # override the class attribute of Student
    school_name = "Springfield HighSchool"

    def get_school_name(self):
        return "This is a high school student, not student of " + super().school_name + " but of " + self.school_name

    def get_name_capitalize(self):
        # super() keyword gets a method or variable form parent class Student
        original_value = super().get_name_capitalize()
        return original_value + "-HS"
