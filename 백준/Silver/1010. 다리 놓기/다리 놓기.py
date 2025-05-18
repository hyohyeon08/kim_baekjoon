num = int(input())
for i in range(num):
    n, m = map(int, input().split())
    
    dp = [1] * (m + 1)
    for i in range(1, m + 1):
        dp[i] = dp[i - 1] * i
    
    print(dp[m] // (dp[n] * dp[m-n]))