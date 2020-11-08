class Employee:
    raise_amount = 1.04 #class variable
    def __init__(self, first, last, email, pay): #constructors
        self.fname = first
        self.lname = last
        self.email = self.fname + self.lname + "@company.com"
        self.pay = pay

    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)
    
    @staticmethod
    def getCompanyName():
        return "WAC"

emp_1 = Employee("Akshat","Girdhar","akshat@gmail.com", 60000)

print(emp_1.getCompanyName())
