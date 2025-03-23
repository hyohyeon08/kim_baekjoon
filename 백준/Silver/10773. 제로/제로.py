num = int(input())
ch = []

for i in range(num):
    n = int(input())
    if(n == 0):
        ch.pop()
    else:
        ch.append(n)

print(sum(ch))