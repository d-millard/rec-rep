class Student:
    # class attributes
    # tend to be static and standard across all instances
    school_name = "Springfield"
    # constructor method
    # uses __init__

    def __init__(self, name, student_id=332):
        # variables set with the self are available throughout the entire instance
        self.name = name
        self.student_id = student_id
    # self refers to instance of class
    # way refereed to class from class
    # used when calling methods/variables in class

    # string method
    # changes the output of print() reference
    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    # even though the school_name is static across all instances it still required self. to be called
    def get_school_name(self):
        return self.school_name
