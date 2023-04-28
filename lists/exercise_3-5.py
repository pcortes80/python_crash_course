guests = ['Gloria', 'Jose','Pablo', 'Melissa', 'Isabel']
print(f"The guest list is {guests}.")

print(f"Dear {guests[0]}: you are invited to my party.")
print(f"Dear {guests[1]}: you are invited to my party.")
print(f"Dear {guests[2]}: you are invited to my party.")
print(f"Dear {guests[3]}: you are invited to my party.")
print(f"Dear {guests[4]}: you are invited to my party.")

print(f"Unfortunately, {guests.pop()} can't make it.")
new_guest = guests.append('Patricio')
print(f"The new guests list is {guests}.")
print(f"Dear {guests[0]}: you are invited to my party.")
print(f"Dear {guests[1]}: you are invited to my party.")
print(f"Dear {guests[2]}: you are invited to my party.")
print(f"Dear {guests[3]}: you are invited to my party.")
print(f"Dear {guests[4]}: you are invited to my party.")
