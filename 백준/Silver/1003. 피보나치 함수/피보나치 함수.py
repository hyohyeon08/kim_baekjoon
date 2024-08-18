ch = int(input())

for num in range(ch):
    a = int(input())
    c = [0, 1]

    if(a == 0):
        print("1 0")
    elif(a == 1):
        print("0 1")
    else:
        for i in range(2, a+1):
            c.append(c[i -1] + c[i - 2])
        print(c[i-1], c[i])