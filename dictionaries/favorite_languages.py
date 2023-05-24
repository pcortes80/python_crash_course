favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#language = favorite_languages['sarah'].title()
#print(f"Sarah's favorite language is {language}.")
#for key, value in favorite_languages.items():
#    print(f"\nKey: {key.title()}")
#    print(f"Value: {value}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Using keys() method
#for name in favorite_languages.keys():
#    print(name.title())

# friends list:
friends = ['phil', 'sarah', 'jen']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    else:
        print(f"\t{name.title()}, please take our poll!.")        
