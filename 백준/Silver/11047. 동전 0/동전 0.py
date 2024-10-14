num, money = map(int, input().split())
new_money = []
cnt = 0

for i in range(num):
    m = int(input())
    new_money.append(m)

new_money.reverse()

for i in new_money:
    if(money >= i):
        cnt += money // i
        money -= (money // i) * i

print(cnt)