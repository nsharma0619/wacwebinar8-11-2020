class Employee:
    raise_amount = 1.04 #class variable
    def __init__(self, first, last, email, pay): #constructors
        self.fname = first
        self.lname = last
        self.email = self.fname + self.lname + "@company.com"
        self.pay = pay

    def getFullName(self):
        return "{} {}".format(self.fname, self.lname)
    
    def PayInc(self):
        self.pay = self.pay * Employee.raise_amount

    @classmethod #alternative constructor
    def from_string(cls, string):
        fname, lname, email, pay = string.split("-")
        return cls(fname, lname, email, pay)


emp_3 = Employee.from_string("Neeraj-Sharma-nsharma-70000")

print(emp_3.pay)