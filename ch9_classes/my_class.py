#importing module into module
#working file

from parent import Person
from child import Male

alia = Person('alia', 'stevens', 66, 'female', 'black')
steve = Male('steve', 'jones', 44, 'male', 'white', 'cop')

alia.person_summary()
steve.person_summary()
steve.job_type()
