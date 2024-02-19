def apply_callback(callback, lst):
    return [callback(item) for item in lst]

numbers = [1, 2, 3, 4, 5]

mapped = map(lambda x: x * 2, numbers)

result = apply_callback(lambda x: x * 2, numbers)

print(result)