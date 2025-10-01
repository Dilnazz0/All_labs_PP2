class String:
    def getString(self):
        self.s = input("Pishi Stroka: ")

    def printString(self):
        print(self.s.upper())
mystring=String()
mystring.getString()
mystring.printString()