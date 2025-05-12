#n1 = 1 n2 = 3 n3 = 5 ||| n1*2 + n2 = n3 |||

n = int(input())
if(n-1 == 0): print(1)
elif(n-1 == 1): print(3)
else:
    dp = [0] * (n)
    dp[0], dp[1] = 1,3
    for i in range(2, n):
        dp[i] = dp[i-2] * 2 + dp[i-1]
    print(dp[-1] % 10007)

