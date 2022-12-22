def fizz_buzz_table(n):
  table = []
  for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
      value = i * j
      if value % 3 == 0 and value % 5 == 0:
        row.append("FizzBuzz")
      elif value % 3 == 0:
        row.append("Fizz")
      elif value % 5 == 0:
        row.append("Buzz")
      else:
        row.append(value)
    table.append(row)
  return table

print(fizz_buzz_table(5))