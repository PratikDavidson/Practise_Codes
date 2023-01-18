class Employee:

    num_of_emps = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        Employee.num_of_emps += 1

    def __str__(self):
        return self.fname + ' ' + self.lname

    @property
    def fullname(self):
        return self.fname + ' ' + self.lname

    @fullname.setter
    def fullname(self, name):
        self.fname, self.lname = name.split(' ')

    @fullname.deleter
    def fullname(self):
        self.fname, self.lname = ("", "")
        print('Name Deleted!')


class Developer(Employee):

    def __init__(self, fname, lname, pay, lang):
        super().__init__(fname, lname, pay)
        self.lang = lang


class Manager(Employee):

    def __init__(self, fname, lname, pay, emp=None):
        super().__init__(fname, lname, pay)
        if emp:
            self.emps = []
        self.emps = [emp]

    def add_emp(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)

    def remove_emp(self, emp):
        if emp in self.emps:
            self.emps.remove(emp)

    def print_emps(self):
        print('manager: ' + self.fullname)
        for emp in self.emps:
            print('|__' + emp.fullname)


emp_1 = Employee('Pratik', 'Davidson', 50000)
emp_2 = Employee('Tim', 'Hudson', 60000)

print(emp_1.fullname)
print(emp_2.fullname)
print(Employee.num_of_emps)

del emp_1.fullname
print(emp_1.fullname)
emp_1.fullname = 'Pratik Davidson'
print(emp_1.fullname)

dev_1 = Developer('Pratik', 'Davidson', 50000, 'python')
dev_2 = Developer('Tim', 'Hudson', 60000, 'Java')

mgr = Manager('Kate', 'Harrington', 100000, dev_1)
mgr.add_emp(dev_2)
mgr.print_emps()
