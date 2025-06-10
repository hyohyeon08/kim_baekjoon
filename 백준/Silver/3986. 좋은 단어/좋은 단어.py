def good_word(n):
    stack = [0, n[0]]
    for i in range(1, len(n)):
        if(stack[-1] == n[i]):
            stack.pop()
            continue
        stack.append(n[i])
    if(len(stack) == 1): return 1
    else: return 0

num = int(input())
check = 0
for i in range(num):
    n = list(input())
    check += good_word(n)

print(check)
