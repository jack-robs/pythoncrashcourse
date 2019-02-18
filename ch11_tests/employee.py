#28.09.2018
'''
1)write  a class Employee()
2) __init__(): first name, last name, annual salary, store as attributes
3) give_raise(): add $5000 to the annual salary by default, buta ccepts different raise amount
4) write test case for Emloyee()
    -setUp(): instantiate employee instance 
    -test 1: test_give_default_raise
    -test 2: test_give_custom_raise
5) make sure tests pass
'''

class Employee():
    """A class to model an employee"""
    def __init__(self, first_name, last_name, annual_salary):
        """Model basic attributes of an employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, add_salary=101):
        self.annual_salary += add_salary  
        
        
