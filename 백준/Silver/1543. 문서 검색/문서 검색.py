na = input()
n = input()
cnt = 0
i = 0

while i < len(na):
    if(n == na[i:len(n)+i]):
        i += len(n)
        cnt += 1
    else:
        i += 1

print(cnt)