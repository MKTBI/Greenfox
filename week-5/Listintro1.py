names = []

# Print out the number of elements in the list
print(len(names))

# Add "William" to the list
names.append("William")

# Print out whether the list is empty or not
if not names:
  print("The list is empty")
else:
  print("The list is not empty")

# Add "John" and "Amanda" to the list
names.extend(["John", "Amanda"])

# Print out the number of elements in the list
print(len(names))

# Print out the 3rd element
print(names[2])

# Iterate through the list and print out each name
for name in names:
  print(name)

# Iterate through the list and print
num = 0
for name in names:
  num += 1
  print(num , name)

# Remove the 2nd element
del names[1]

# Iterate through the list in a reversed order and print out each name
for name in reversed(names):
  print(name)

# Remove all elements
names.clear()

# Print out the number of elements in the list
print(len(names))