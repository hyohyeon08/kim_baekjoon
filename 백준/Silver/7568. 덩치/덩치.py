a = []
n = []
num = int(input())
for i in range(num):
    b, c = map(int, input().split())
    a.append([b, c])


for i in range(num):
    count = 0
    for j in range(num):
        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            count += 1
    n.append(count+1)

for i in n:
    print(i, end=' ')

            