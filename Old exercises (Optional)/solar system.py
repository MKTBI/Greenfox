# "Saturn" is missing from the planetList
# Insert it into the correct position
# Create a method called "put_saturn()" which has a list parameter and returns the correct list

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
# Expected output: "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"

def put_saturn(list) -> list:
    list.insert(5,"Saturn")
    return list

print(put_saturn(planet_list))