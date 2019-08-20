from BEGINNER.Test.test_one import Robot


class Human(Robot):
    speech = True
    walking = True
    good_at_math = False

    def buying_things(self, num):
        if not self.current_finaces(num):
            print("probably not")
        else:
            print("oh yeah")

    def current_finaces(self, num):
        if num < 1000:
            return False
        return True
