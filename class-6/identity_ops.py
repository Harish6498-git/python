x = [1, 2, 3]
y = x  # y now refers to the same object as x
result = x is y
# result will be True
print(result)

a = "hello"
b = "world"
result = a is not b
# result will be True
print(result)