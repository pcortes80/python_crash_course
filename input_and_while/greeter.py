prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nwhat is your firt name? "

# this way is how to build a multi-line string

name = input(prompt)
print(f"\nHello, {name}!")
