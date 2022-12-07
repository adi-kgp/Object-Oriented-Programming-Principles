## Encapsulation and Abstraction

class SoftwareEngineer:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None # protected variable (private in practice) 
        self._num_of_bugs_solved = 0  # protected variable (private in practice)

    def get_salary(self):  # getter
        return self._salary

    def set_salary(self, base_value): # setter
        #check value, enforce constraints
        self._salary = self._calculate_salary(base_value) # application of abstraction

    def _calculate_salary(self, base_value):  # hidden function
        if self._num_of_bugs_solved < 10:
            return base_value
        if self._num_of_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

    def code(self):
        self._num_of_bugs_solved += 1

se = SoftwareEngineer("Max", 25)
print(se.age, se.name)

for i in range(70):
    se.code()

print(se._num_of_bugs_solved)
se.set_salary(6000)
print(se.get_salary())
