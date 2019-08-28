from random import random as ran


def run():
    while True:
        try:
            user_data = user_file("Please enter a valid file name you would like to encrypt: ")
            break
        except ValueError as e:
            print(e)

    # maybe scratch this idea
    # dont know
    # maybe make the program make a random key and output it with the encrypted document
    # the key would be on the set of characters actually used
    # wont need reference if do this
    # hard code key, make it random signs for each one
    # ref will be all the characters gotten from the documet
    # when the value is found
    print(int(20 + (ran() * 80)))
    while True:
        ran_gen = uni_gen()
        # this range gets all possible characters 0 - 97
        for i in range(int(1 + ran() * 97)):
            print(i)
            print(next(ran_gen))


    ref = {'a': ['%', ]}

    for key in ref:
        for value in (k for k in (item for item in uni_gen()) if str(chr(int(k, 16))) == key):
            # work on generator making random hexadecimal
            print(f"0x00{int(21 + (ran() * 60))}")
            ref[key].append(value)
            ref[key] = tuple(ref[key])
    print(ref)


# print(encrypt[int(ran() * len(encrypt))])
"C:\Test\he.txt"


def uni_gen(end=81):
    yield r"0x0020"
    for i in range(21, end):
        if i % 10 != 0:
            yield r"0x00{}".format(str(i))
        else:
            for a in ("A", "B", "C", "D", "E", "F"):
                yield r"0x00{}{}".format(str(i - 1)[0], a)
            yield r"0x00{}".format(str(i))


def user_file(text):
    try:
        with open(input(text)) as f:
            return f
    except (PermissionError, FileNotFoundError) as e:
        raise ValueError(e)



run()
