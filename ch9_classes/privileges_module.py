#no dependencies, import into user_module, import into admin_module
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

