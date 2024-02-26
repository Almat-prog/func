numbers = (1, 2, 3, 4, 5, -1, -2, -3, -4, -5)
even_numbers = filter(lambda x: x > 0,numbers)
squared_numbers = map(lambda x: x * x, even_numbers)
print(list(squared_numbers))
