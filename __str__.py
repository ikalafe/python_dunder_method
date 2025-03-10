class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"کارمند {self.name} با حقوق {self.salary} تومان"
    
emp = Employee("دانیال", "50_000_000")

print(emp)