def build_profile(first, last, **user_info):
    """Build a Dictionary containing user information"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_profile('albert', 'eintein', 
                             location='Princeton', field='Pyhsics')

print(user_profile)