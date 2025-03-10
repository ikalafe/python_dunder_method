class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __lt__(self, other):
        return self.salary < other.salary

emp1 = Employee("نیما", 4000000)
emp2 = Employee("پریسا", 6000000)
print(emp1 < emp2)