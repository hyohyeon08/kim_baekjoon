n = int(input())
gedan = [int(input()) for _ in range(n)]
dp = [0]*(n)

if(len(gedan) <= 2):
    print(sum(gedan))
else:
    dp[0] = gedan[0]
    dp[1] = gedan[0] + gedan[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + gedan[i-1] + gedan[i], dp[i-2] + gedan[i])
    print(dp[-1])