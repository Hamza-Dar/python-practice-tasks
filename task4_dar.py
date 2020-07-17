class capString:
    """Takes a string input and prints it in All UPPER CASE"""
    str= ""

    def __init__(self):
        self.str= ""

    def getString(self):
        self.str= input("Enter your String: ")

    def printString(self):
        print(self.str.upper())


obj= capString()
print(obj.__doc__)
obj.getString()
obj.printString()
