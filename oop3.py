## Inheritence

#inherits, extends, override
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working...")

class SoftwareEngineer(Employee): # this class inherits all the classes and functions from Employee
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding...")
        
    def debug(self):
        print(f"{self.name} is debugging...")

class Designer(Employee):

    def work(self):
        print(f"{self.name} is designing...")

    def draw(self):
        print(f"{self.name} is drawing...")

se = SoftwareEngineer("Max", 25, 6000, "Junior")

se.debug()
#se.work()

d = Designer("Lisa", 30, 7000)

#d.work()
d.draw()


# Polymorphism 

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
             SoftwareEngineer("Lisa", 30, 9000, "Senior"),
             Designer("Phillip", 27, 7000)]
             
def motivate_employees(employees):
    for employee in employees:
        employee.work()

motivate_employees(employees)


# Recap:
# inheritence: ChildClass(BaseClass)
# inherit, extend, override
# super().__init__()
# polymorphism