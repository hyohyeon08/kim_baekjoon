N, M = map(int, input().split())

N_list = []
M_list = []

for i in range(N):
    N_list.append(list(map(int, input().split())))
for i in range(N):
    M_list.append(list(map(int, input().split())))
for i in range(N):
    for j in range(M):
        print(N_list[i][j] + M_list[i][j], end=" ")
    print()
