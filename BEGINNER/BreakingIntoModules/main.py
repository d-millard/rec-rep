# a better way to import is to use
from BEGINNER.BreakingIntoModules.hs_student import HihSchoolStudent
# use * if you want to import everything
# import hs_student when using this to import you must prefix when referring to HighSchoolStudnet with hs_student.

james = HihSchoolStudent("james")
print(james.get_name_capitalize())
print(james.get_school_name())
