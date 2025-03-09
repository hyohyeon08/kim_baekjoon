import sys

num = int(sys.stdin.readline())
jung = []

for i in range(num):
    jung.append(sys.stdin.readline().strip())

set_jung = set(jung)
jung = list(set_jung)
jung.sort()
jung.sort(key=len)

for i in jung:
    print(i)