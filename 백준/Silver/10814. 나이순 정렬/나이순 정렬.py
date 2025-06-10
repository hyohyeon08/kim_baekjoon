num = int(input())
na = []

for i in range(num):
    age, name = input().split()
    na.append([int(age), name, i])

na.sort(key=lambda x: x[0])

for i in range(num):
    print(na[i][0], na[i][1])
