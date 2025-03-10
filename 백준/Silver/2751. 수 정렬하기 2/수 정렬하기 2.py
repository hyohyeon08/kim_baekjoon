import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

a = list(set(a))
a.sort()
for i in a:
    print(i)