def pado_ban(n : int):
    if(n == 0 or n == 1 or n == 2):
        return 1
    
    dp = [0]*(n+1)
    dp[0], dp[1], dp[2] = 1,1, 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-3] + dp[i-2]
    return dp[-2]

w = int(input())
for i in range(w):
    n = int(input())
    print(pado_ban(n))