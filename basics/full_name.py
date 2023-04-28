first_name = "ada"
last_name = "lovelace"
# f-string
# f is for format in Python
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)

# for Python 3.5 or earlier:
message = "{} {}".format(first_name, last_name)
print(message)
