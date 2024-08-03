class Employee:
    salary = 10000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, val):
        self.increment = val / self.salary


e1 = Employee()

print(e1.salaryAfterIncrement)
e1.salaryAfterIncrement = 20000
print(e1.increment)
