#child class, importing parent class

from parent import Person 

class Male(Person):
    """Modeling a Male, child class of Person"""
    def __init__(self, first_name, last_name, height, sex, race, job):
        super().__init__(first_name, last_name, height, sex, race)
        self.job = job
    
    def job_type(self):
        print('This man is a ' + self.job)
    
jack = Male('jack', 'robertson', 74, 'male', 'white', 'soldier')
jack.person_summary()
jack.job_type()
