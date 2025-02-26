def bu_she(K, n):
    c = 0
    li = []

    for i in range(K+1):
        li2 = []
        if(len(li) == 0):
            for j in range(1, n+1):
                li2.append(j)
        else:
            for j in range(1, n+1):
                li2.append(sum(li[c][:j]))
            c += 1
        li.append(li2)
    return li[K][n-1]

    
num = int(input())

for i in range(num):
    K = int(input())
    n = int(input())
    print(bu_she(K, n))
