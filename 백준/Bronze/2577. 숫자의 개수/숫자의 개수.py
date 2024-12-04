n1 = int(input())
n2 = int(input())
n3 = int(input())
an = str(n1*n2*n3)

for i in range(10):
    print(an.count(str(i)))