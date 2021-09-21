import random
class Person:
    def __init__(self):
        self.pstid='unknown'
        self.brth='01.01.2001'

    def showdata(self):
        print("Noma'lum shaxs")

    def generatePassportID(self):
        first_part=["AA", "AB", "AC", "AF"]
        numbers="0123456789"
        self.pstid=""
        self.pstid+=random.choice(first_part)
        for i in range(7):
            self.pstid+=random.choice(numbers)


class Driver(Person):
    def __init__(self, fullName, exp, health):
        super().__init__()
        self.fullName=fullName
        self.exp=exp
        self.health=health
        super().generatePassportID()

    def showData(self):
        print("Driver:{0}, {1}, {3}, {4}".format(self.fullName, self.exp, self.health, self.pstid, self.brth))

driver=Driver("Bob", 12, "good")
driver.showData()