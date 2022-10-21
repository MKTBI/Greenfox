apple = ["first", "second", "third"]
old_third = apple[2]
old_first = apple[0]
apple[0] = apple[2]
apple[2]  = old_first
print(apple)