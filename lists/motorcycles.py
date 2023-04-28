motorcycles = ['honda', 'yamaha', 'suzuky']
print(motorcycles)

print("Modify the name of element 0:")
motorcycles[0] = 'ducati'
print(motorcycles)

print("Add a new element to the list:")
motorcycles.append('honda')
print(motorcycles)

print("How to use pop() function")
first_owned = motorcycles.pop()
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)
