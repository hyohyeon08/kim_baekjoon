memo = [1, ]
a = int(input())

for i in range(1, a+1):
    memo.append(memo[i-1]*i)

print(memo[a])