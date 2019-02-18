#18.09.2018
#use randint module


from random import randint 

class Die():
    """Simulate a 6-side die, and rolls of the die"""
    def __init__(self):
        self.sides = 6
        
        
    def roll_die(self, name, num_rolls):
        """Roll dice 10x, print result each time"""
        print('Rolling die, ' + name)
        rolls = 0 
        while rolls < num_rolls:
            if rolls == num_rolls:
                break
            roll = randint(1, 6)
            print(roll)
            rolls += 1
        
    
my_die = Die()
my_die.roll_die('jack', 10)
my_die.roll_die('jack', 20)
