class Employee:
    raise_amount = 1.04 #class variable
    def __init__(self, first, last, email, pay): #constructors
        self.fname = first
        self.lname = last
        self.email = email
        self.pay = pay

    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)
    
    def PayInc(self):
        self.pay = self.pay*raise_amount #showing me error


emp_1 = Employee("Akshat","Girdhar","akshat@gmail.com", 60000)
emp_2 = Employee("ved","upadhye","ved@gmail.com", 50000)

print(emp_1.raise_amount)


