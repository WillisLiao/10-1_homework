container = {}
container['A'] = 2/9 * 1/4 * 1/2
container['B'] = 1/3 * 1/2 * 1/2
container['C'] = 2/7 * 1/3 * 1/3
# Normalize
pro = sum(i for i in container.values())
for i, p in container.items():
    container[i] = p / pro
print(container['B']*container['C'])