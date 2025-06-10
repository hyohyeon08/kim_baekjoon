def fac(n : int):
    check = 1
    zeros = 0
    for i in range(1, n+1):
        check *= i
    check = list(str(check))
    check.reverse()
    for i in check:
        if(i == "0"):
            zeros += 1
        else:
            break
    print(zeros)
    

n = int(input())

fac(n)
