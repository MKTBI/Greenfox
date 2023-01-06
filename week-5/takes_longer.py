q = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."
index = q.find("you ")
q1 = q[:index] + " always takes longer than " + q[index:]
print(q1)
