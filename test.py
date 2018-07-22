a = list(range(1, 5))
b = [i + 2 for i in a]
print(b)

# map()方式
b = map(lambda x: x + 2, a)
print(list(b))

b = map(lambda x, y: x + y, a, range(10, 15))
print(list(b))

l = [1, 3, -2, 3, 3, 55, 7]
print(sorted(l))
