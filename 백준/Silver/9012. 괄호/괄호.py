num = int(input())

for i in range(num):
    new_stack = []
    g = input()
    
    for i in (g):
        if(new_stack and new_stack[-1] == '(' and i == ')'):
            new_stack.pop()
        else:
            new_stack.append(i)
    print("YES" if len(new_stack) == 0 else "NO")