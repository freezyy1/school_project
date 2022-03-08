import itertools
# C - испания
a = set(itertools.permutations('ИГАC', r=4))

counter1 = 0
counter2 = 0
for i in a:
    if i[-1] == 'Г':
        counter1 += 1
    counter2 +=1

print(counter1 / counter2)
