"""
Model for aircraft flights.
Models the seating charts of flights, kinda like bus algorithm, but using classes.
"""


class Flight:

    # number is an instance method
    def number(self):
        return "A0N60"


test = Flight()

print(test.number())




