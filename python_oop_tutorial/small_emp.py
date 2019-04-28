class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'
emp_1.fullname = 'Corey Schafer'
emp_1.fullname = 'Bennett Levine'
del emp_1.fullname
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

