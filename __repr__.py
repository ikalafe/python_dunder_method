class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"
    
emp = Employee("علی", 7000000)
print(repr(emp))