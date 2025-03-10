class Employee:
    def __init__(self, name, salary, emp_id):
        self.name = name
        self.salary = salary
        self.emp_id = emp_id

emp = Employee("رضا", 5000000, "E123")

print(emp.__dict__)

emp.__dict__["hire_date"] = "1403-01-01"

print(emp.__dict__)

print(emp.hire_date)

emp.__dict__["salary"] = 6000000
print(emp.salary)

print(emp.__dict__)