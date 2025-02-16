jandon = [500, 100, 50, 10, 5, 1]
m = int(input())
m = 1000 - m
cnt = 0

for i in jandon:
    cnt += m // i
    m %= i

print(cnt)