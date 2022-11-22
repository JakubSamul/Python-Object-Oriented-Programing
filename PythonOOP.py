class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Cccc'
emp_1.email = 'Corey.cccc@company.com'
emp_1.pay = 50000

emp_2.first = 'John'
emp_2.last = 'Aaaaa'
emp_2.email = 'John.Aaaaa@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

