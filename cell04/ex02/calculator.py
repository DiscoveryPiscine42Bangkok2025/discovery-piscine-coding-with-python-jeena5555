x = [2, 8, 9, 48, 8, 22, -12, 2]

result = list(dict.fromkeys([n + 2 for n in x if n > 5]))

print(result)
