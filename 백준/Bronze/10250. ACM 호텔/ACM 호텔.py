num = int(input())

for i in range(num):
    H, W, N = map(int, input().split())
    HW = []
    for j in range(1, H+1):
        HW.append([j])
    for j in range(1, N+1):
        HW[(j%H)-1].append(j)
    print(f"{HW[(N%H)-1][0]}{len(HW[(N%H)-1])-1:02}")