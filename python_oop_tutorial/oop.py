# Python Object-Oriented Programming


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comapny.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(emp_1.first, emp_1.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 14)

print(Employee.is_workday(my_date))
# print(emp_1.email)
# print(emp_2.email)

# print(emp_1.fullname())

# print(Employee.fullname(emp_1))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# emp_1.set_raise_amt(1.07)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
# 
# first, last, pay = emp_str_1.split('-')
# 
# print(new_emp_1.fullname())
# print(new_emp_1.email)


