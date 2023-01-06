products = {
  "Eggs": 200,
  "Milk": 200,
  "Fish": 400,
  "Apples": 150,
  "Bread": 50,
  "Chicken": 550
}

# Which products cost less than 201? (just the name)
print("Products that cost less than 201:")
for name, price in products.items():
  if price < 201:
    print(name)

# Which products cost more than 150? (name + price)
print("\nProducts that cost more than 150:")
for name, price in products.items():
  if price > 150:
    print(name, price)
