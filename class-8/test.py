def get_coordinates():
    return (3, 4)

x, y = get_coordinates()  # Unpack the returned tuple (x=3, y=4)
print(f"x: {x}, y: {y}")





def get_coordinates(a, b):
    return (a, b)

result = get_coordinates(10, 5)
print(f"a: {result[0]}, b: {result[1]}")