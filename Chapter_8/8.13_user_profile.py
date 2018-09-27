def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about the user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('ajay', 'kallukalam', can='quiet', \
        makes='terrible decisions')

print(user_profile)


