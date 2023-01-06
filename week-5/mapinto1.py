charMap = {}

# Print out whether the map is empty or not
if not charMap:
  print("The map is empty")
else:
  print("The map is not empty")

# Add the key-value pairs to the map
charMap[97] = 'a'
charMap[98] = 'b'
charMap[99] = 'c'
charMap[65] = 'A'
charMap[66] = 'B'
charMap[67] = 'C'

# Print all the keys
print(charMap.keys())

# Print all the values
print(charMap.values())

# Add value D with the key 68
charMap[68] = 'D'

# Print how many key-value pairs are in the map
print(len(charMap))

# Print the value that is associated with key 99
print(charMap[99])

# Remove the key-value pair with key 97 and print the associated value
removedValue = charMap.pop(97)
print(removedValue)

# Print whether there is an associated value with key 100 or not
if 100 in charMap:
  print("There is a value associated with key 100")
else:
  print("There is no value associated with key 100")

# Remove all the key-value pairs
charMap.clear()

# Print how many key-value pairs are in the map
print(len(charMap))
