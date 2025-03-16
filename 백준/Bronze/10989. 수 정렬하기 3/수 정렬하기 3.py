import sys

num = int(input())

cnt = [0]*10001

for _ in range(num):
    a = int(sys.stdin.readline())
    cnt[a] += 1

for i in range(1, 10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)