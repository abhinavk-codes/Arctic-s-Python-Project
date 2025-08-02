# Program to input 5 five names in list and then display the shortest name!
names = []

# Input 5 names
for i in range(5):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Find the shortest name using min() with key=len
shortest = min(names, key=len)
print(f"The shortest name is: {shortest}")
