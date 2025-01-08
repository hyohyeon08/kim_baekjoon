import sys
num = int(sys.stdin.readline())

stack = []
    
    
for i in range(num):
    n = sys.stdin.readline().split()
    if(n[0] == 'push'):
        stack.append(n[1])
    elif(n[0] == 'pop'):
        if(len(stack) == 0):
            print('-1')
        else:
            print(stack.pop())
    elif(n[0] == 'size'):
        print(len(stack))
    elif(n[0] == 'empty'):
        if(len(stack) == 0):
            print('1')
        else:
            print('0')
    elif(n[0] == 'top'):
        if(len(stack) == 0):
            print('-1')
        else:
            print(stack[-1])