## Properties

class SoftwareEngineer:
    
    def __init__(self):
        self._salary = None # protected variable (private in practice) 

    # getter
    @property
    def salary(self): 
        # checks, constrains, calculations 
        return self._salary

    # setter
    @salary.setter
    def salary(self, value): 
        self._salary = value

    # salary.deleter
    @salary.deleter
    def salary(self): 
        del self._salary

se = SoftwareEngineer()

se.salary = 6000
print(se.salary)
del se.salary


# Recap of oop4 and oop5
# encapsulation
# public, private methods, attributes
# _func(), _attribute for protected (encapsulaiton)
# getter and setter (only way to access protected variables from outside)
# getter -> @property
# setter -> x.setter