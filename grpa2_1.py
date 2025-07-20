x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

x1, x2 = x2, x1  # swap the values of `x1` and `x2`

y1, y2, y3 = y2, y3, y1  # circular swap of `y1`, `y2`, and `y3`

a = z  # create a new variable `a` with the value of `z`

del z  # delete the variable `z`

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)