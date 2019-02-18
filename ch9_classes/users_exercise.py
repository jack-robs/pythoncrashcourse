#18.09.2018
#9-7/9-8: Inheritance 

class Users():
    """Model users of a computer system"""
    def __init__(self, first_name, last_name, sex, age, race):
        """Initilialize common user traits"""
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.race = race
        self.login_attempts = 0
    
    def describe_user(self):
        """Print out basic description of user"""
        print(
            '\nname: ' + self.first_name.title() + self.last_name.title() +
            '\nsex: ' + self.sex +
            '\nage: ' + str(self.age) +
            '\nrace: ' + self.race
            )
        
    def greet_user(self):
        """Print out greeting to user"""
        print('Hello ' + self.first_name.title() + self.last_name.title())
    
    def increment_login_attempts(self, attempts):
        """Track incrementally, login attempts"""
        self.login_attempts += attempts
    
    def reset_login_attempts(self):
        """reset login attempt tracker"""
        self.login_attempts = 0
        
class Admin(Users):
    """Model a user with admin privileges"""
    def __init__(self, first_name, last_name, sex, age, race):
        """Initialize admin elements"""
        super().__init__(first_name, last_name, sex, age, race)
        self.privileges = Privileges()
        

class Privileges():
    """Model Admin Privs in a sep class"""
    def __init__(self):
        privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = privileges 
    
    def show_privileges(self):
        """Print out admin privileges"""
        print('Admin can do the following:')
        for priv in self.privileges:
            print("-" + priv)

