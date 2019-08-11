class Robot:
    from random import randint
    speech = False
    walking = False
    good_at_math = True

    def __init__(self, name, le):
        self.name = name
        self.le = le
        self.unit_num = []

    def calc_unit_number(self):
        i = 0
        if self.le == 3:
            while i < 3:
                self.calc_random()
                i += 1
            return self.unit_num
        while i < 6:
            self.calc_random()
            i += 1
        return self.unit_num

    def calc_random(self):
        r_dict = {"Unit Number": self.randint(0, 9)}
        self.unit_num.append(r_dict)

    def get_unit_num(self):
        self.unit_num = self.calc_unit_number()
        for k in self.unit_num:
            yield str("{0}".format(k["Unit Number"]))

    def __str__(self):
        st = ""
        for y in self.get_unit_num():
            st += "" + y + ""
        return "The robot formally named: {0} has a generated unit number of {1}.".format(self.name, st)
