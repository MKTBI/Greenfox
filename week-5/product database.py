products = {
  "Eggs": 200,
  "Milk": 200,
  "Fish": 400,
  "Apples": 150,
  "Bread": 50,
  "Chicken": 550
}

# How much is the fish?
print("The fish costs", products["Fish"])

# What is the most expensive product?
mostExpensive = max(products, key=products.get)
print("The most expensive product is", mostExpensive)

# What is the average price?
total = 0
count = 0
for price in products.values():
  total += price
  count += 1
average = total / count
print("The average price is", average)

# How many products' price is below 300?
below300 = 0
for price in products.values():
  if price < 300:
    below300 += 1
print(below300, "products' price is below 300")

# Is there anything we can buy for exactly 125?
if 125 in products.values():
  print("There is something we can buy for exactly 125")
else:
  print("There is nothing we can buy for exactly 125")

# What is the cheapest product?
cheapest = min(products, key=products.get)
print("The cheapest product is", cheapest)
