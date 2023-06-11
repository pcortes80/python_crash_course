# Define a dictionary called 'users' with
# two keys: one each for the usernames 'aeinstein' 
# and 'mcurie'

users = {
    'aeistein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

# Python assignes each key to the variable username, and
# the dictionary associated with each username is 
# assigned to the variable user_info.
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
