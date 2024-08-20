def hnoi(n, go, tmp, to):
    if(n == 1):
        print("{} {}".format(go, to))
    else:
        hnoi(n-1, go, to, tmp)
        print("{} {}".format(go, to))
        hnoi(n-1, tmp, go, to)


num = int(input())
if(num <= 20):
    print(2**num-1)
    hnoi(num, 1, 2, 3)
else:
    print(2**num-1)