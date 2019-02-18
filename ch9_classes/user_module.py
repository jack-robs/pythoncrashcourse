#parent User class, imported into admin_module

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

