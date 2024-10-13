num = int(input())
cnt = num

for i in range(num):
    w = input()
    for j in range(0, len(w)-1):
        if(w[j] == w[j+1]):
            pass
        elif(w[j] in w[j+1:]):
            cnt -= 1
            break

print(cnt)