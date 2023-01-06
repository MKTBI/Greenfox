# Create List A
ListA = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

# Create List B with the values of List A
ListB = ListA.copy()

# Print out whether List A contains "Durian" or not
if "Durian" in ListA:
  print("List A contains 'Durian'")
else:
  print("List A does not contain 'Durian'")

# Remove "Durian" from List B
ListB.remove("Durian")

# Add "Kiwifruit" to List A after the 4th element
ListA.insert(4, "Kiwifruit")

# Compare the size of List A and List B
if len(ListA) == len(ListB):
  print("The lists are the same size")
else:
  print("The lists are not the same size")

# Get the index of "Avocado" from List A
index = ListA.index("Avocado")
print("The index of 'Avocado' in ListA is:", index)

# Get the index of "Durian" from List B
try:
  index = ListB.index("Durian")
  print("The index of 'Durian' in ListB is:", index)
except ValueError:
  print("'Durian' is not in ListB")

# Add "Passion Fruit" and "Pomelo" to List B in a single statement
ListB += ["Passion Fruit", "Pomelo"]

# Print out the 3rd element from List A
print(ListA[2])

# Print all elements of List A
print(ListA)

# Print all elements of List B
print(ListB)
