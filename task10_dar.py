class Person:
    def __init__(self):
        self.gender=""


class Male(Person):
    def __init__(self):
        Person.__init__(self)
        self.gender= "Male"

    def getGender(self):
        print(self.gender)


class Female(Person):
    def __init__(self):
        Person.__init__(self)
        self.gender= "Female"

    def getGender(self):
        print(self.gender)


m = Male()
m.getGender()

f = Female()
f.getGender()


