products = {
  "Milk": 1.07,
  "Rice": 1.59,
  "Eggs": 3.14,
  "Cheese": 12.60,
  "Chicken Breasts": 9.40,
  "Apples": 2.31,
  "Tomato": 2.58,
  "Potato": 1.75,
  "Onion": 1.10
}

bobList = {
  "Milk": 3,
  "Rice": 2,
  "Eggs": 2,
  "Cheese": 1,
  "Chicken Breasts": 4,
  "Apples": 1,
  "Tomato": 2,
  "Potato": 1
}

aliceList = {
  "Rice": 1,
  "Eggs": 5,
  "Chicken Breasts": 2,
  "Apples": 1,
  "Tomato": 10
}

# How much does Bob pay?
bobTotal = 0
for item, amount in bobList.items():
  bobTotal += products[item] * amount
print("Bob pays", bobTotal)

# How much does Alice pay?
aliceTotal = 0
for item, amount in aliceList.items():
  aliceTotal += products[item] * amount
print("Alice pays", aliceTotal)

# Who buys more Rice?
if bobList.get("Rice", 0) > aliceList.get("Rice", 0):
  print("Bob buys more rice")
elif bobList.get("Rice", 0) < aliceList.get("Rice", 0):
  print("Alice buys more rice")
else:
  print("Bob and Alice buy the same amount of rice")