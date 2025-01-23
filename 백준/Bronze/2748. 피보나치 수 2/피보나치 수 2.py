num = int(input())
memo = [0,1]

for i in range(2, num+1):
    memo.append(memo[i-1] + memo[i-2])

print(memo[num])