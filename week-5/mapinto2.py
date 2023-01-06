bookMap = {
  "978-1-60309-452-8": "A Letter to Jo",
  "978-1-60309-459-7": "Lupus",
  "978-1-60309-444-3": "Red Panda and Moon Bear",
  "978-1-60309-461-0": "The Lab"
}

# Print all the key-value pairs in the desired format
for isbn, title in bookMap.items():
  print(title, "(ISBN:", isbn + ")")

# Remove the key-value pair with key 978-1-60309-444-3
del bookMap["978-1-60309-444-3"]

# Remove the key-value pair with value The Lab
for isbn, title in list(bookMap.items()):
  if title == "The Lab":
    del bookMap[isbn]

# Add the key-value pairs to the map
bookMap["978-1-60309-450-4"] = "They Called Us Enemy"
bookMap["978-1-60309-453-5"] = "Why Did We Trust Him?"

# Print whether there is an associated value with key 478-0-61159-424-8 or not
if "478-0-61159-424-8" in bookMap:
  print("There is a value associated with key 478-0-61159-424-8")
else:
  print("There is no value associated with key 478-0-61159-424-8")

# Print the value associated with key 978-1-60309-453-5
print(bookMap["978-1-60309-453-5"])
