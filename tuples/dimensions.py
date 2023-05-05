dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])
print("Using for to loop over all elements:")
for dimension in dimensions:
    print(dimension)

"""Modify Tuple

We can't modify a tuple, but we can assign a new value to a variable.
"""
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)      
