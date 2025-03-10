class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __eq__(self, other):
        return self.name == other.name and self.salary == other.salary
    
emp1 = Employee("مریم", 5000000)
emp2 = Employee("مریم", 5000000)
print(emp1 == emp2)