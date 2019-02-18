#18.09.2018
#parent class that'll get imported into a child, and also into work_file

class Person():
    def __init__(self, first_name, last_name, height, sex, race):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.sex = sex
        self.race = race
    
    def person_summary(self):
        print('This person has the followin traits: ')
        print('\n' +
            '\nfirst name: ' + self.first_name.title() +
            '\nlast name: ' + self.last_name.title() +
            '\nheight (in): ' + str(self.height) + 
            '\nsex: ' + self.sex +
            '\nrace: ' + self.race
            )


