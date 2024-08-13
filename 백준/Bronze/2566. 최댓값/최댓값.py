a =[]

for i in range(9):
    a.append(list(map(int, input().split())))

a = sum(a, [])

print(max(a))
print(a.index(max(a)) // 9 + 1, a.index(max(a)) % 9 + 1)