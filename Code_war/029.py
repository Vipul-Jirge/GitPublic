k = set()
m = 1
for i in range(2,101):
    for j in range(2,101):
        k.add(i**j)
        m+=1

print(k.pop())