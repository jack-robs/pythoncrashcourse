#16.09.2018
#9-3 Users, Ch 9: Classes
#9-5 cont'd, add more attributes/methods

class Users():
    
    def __init__(self, first_name, last_name, sex, age, race):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.race = race
        self.login_attempts = 0
    
    def describe_user(self):
        print(
            '\nname: ' + self.first_name.title() + self.last_name.title() +
            '\nsex: ' + self.sex +
            '\nage: ' + str(self.age) +
            '\nrace: ' + self.race
            )
        
    def greet_user(self):
        print('Hello ' + self.first_name.title() + self.last_name.title())
    
    def increment_login_attempts(self, attempts):
        self.login_attempts += attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
new_user = Users('jack', 'robertson', 'male', 26, 'white')
print(new_user.login_attempts)
#increment logins
new_user.increment_login_attempts(1)
print(new_user.login_attempts)

#increment logins
new_user.increment_login_attempts(1)
print(new_user.login_attempts)

#increment logins
new_user.increment_login_attempts(1)
print(new_user.login_attempts)

#rest logins
new_user.reset_login_attempts()
print(new_user.login_attempts)


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
