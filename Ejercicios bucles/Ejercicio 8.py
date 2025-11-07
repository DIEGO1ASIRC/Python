y = [1,3,5,7,9]
x = 0

for i in range(5):
  print(y[x])
  x = x + 1
  for j in range(x):
    print("*", end=" ")
  print()