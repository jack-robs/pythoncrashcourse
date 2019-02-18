#16.09.2018
#Arbitrary Keyword Arguments in Functions: def fxn(**param):

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value 
    return profile
    

user_profile = build_profile('albert', 'einstein', location='princeton', 
                                field='physics')
                                
print(user_profile)

for k, v in user_profile.items():
    print(k + ':\n', v)


user_profile = build_profile('jack', 'robertson', location='boston', job='swe',
                            wife='ali')
print('\n')
for k, v, in user_profile.items():
    print(k + ':\n' + v)
