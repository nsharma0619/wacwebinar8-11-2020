class Employee:
    raise_amount = 1.04 #class variable
    def __init__(self, first, last, pay): #constructors
        self.fname = first
        self.lname = last
        self.email = self.fname + self.lname + "@company.com"
        self.pay = pay

    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)
    
class Developer(Employee):
    def __init__(self, first, last, pay, current_project): #constructors
        super().__init__(first, last, pay)
        self.current_project = current_project

dev1 = Developer("akshat","girdhar", 50000, "teaching webinar")
print(dev1.getFullName())


