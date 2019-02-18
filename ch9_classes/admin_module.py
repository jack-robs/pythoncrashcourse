#dependencies: Users(), Privileges

from user_module import Users
from privileges_module import Privileges

class Admin(Users):
    """Model a user with admin privileges"""
    def __init__(self, first_name, last_name, sex, age, race):
        """Initialize admin elements"""
        super().__init__(first_name, last_name, sex, age, race)
        self.privileges = Privileges()

my_admin = Admin('jack', 'robertson', 'male', 22, 'white')
my_admin.describe_user()
