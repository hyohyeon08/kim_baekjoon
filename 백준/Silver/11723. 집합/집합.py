import sys

input = sys.stdin.readline
num = int(input())

S = set()

for _ in range(num):
    cmd = input().split()
    
    if cmd[0] == "add":
        S.add(int(cmd[1]))
    elif cmd[0] == "remove":
        S.discard(int(cmd[1]))
    elif cmd[0] == "check":
        print(1 if int(cmd[1]) in S else 0)
    elif cmd[0] == "toggle":
        x = int(cmd[1])
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif cmd[0] == "all":
        S = set(range(1, 21))
    elif cmd[0] == "empty":
        S.clear()
