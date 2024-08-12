N, M = map(int, input().split())
b = [i for i in range(1, N+1)]

for i in range(M):
    i,j = map(int, input().split())
    temp = b[i-1:j]
    temp.reverse()
    b[i-1:j] = temp

for i in range(N):
    print(b[i], end = ' ')