class Employee:
    def __init__(self, first, last, email, pay):
        self.fname = first
        self.lname = last
        self.email = email
        self.pay = pay


emp_1 = Employee("Akshat","Girdhar","akshat@gmail.com", 60000)
emp_2 = Employee("ved","upadhye","ved@gmail.com", 50000)

print(emp_1.fname)
