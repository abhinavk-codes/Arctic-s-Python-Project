# Program to enter a list of names and print them in Alphabetical order
names = []

n = int(input("Enter number of names : "))
for i in range(n) :
    names.append(input("Enter name : "))

sorted_names = sorted(names)

for i in range(n) :
    print(sorted_names[i])
