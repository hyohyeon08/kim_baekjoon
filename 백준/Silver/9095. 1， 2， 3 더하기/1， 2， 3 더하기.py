import sys

n = int(sys.stdin.readline())
memo = [0,1,2,4]
re = 3

for i in range(n):
    num = int(sys.stdin.readline())
    for i in range(re, num):
        memo.append(memo[i-2] + memo[i-1] + memo[i])
    re = len(memo)-1
    print(memo[num])