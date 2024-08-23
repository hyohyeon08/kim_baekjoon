a = [str(i) for i in range(1, 1001)]
new = []
n = 1
for i in a:
    new.extend([i]*n)
    n += 1

sum = 0
one, two = map(int, input().split())
for i in range(one-1, two):
    sum +=  int(new[i])
print(sum)