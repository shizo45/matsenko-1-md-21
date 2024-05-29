import random
list = []
for i in range (1, 10):
    list.append(random.randint(0, 9))
print(*filter(lambda x : list.count(x) > 1, list))