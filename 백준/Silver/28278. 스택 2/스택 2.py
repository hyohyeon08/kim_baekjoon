import sys
num = int(sys.stdin.readline())

stack = []

for i in range(num):
    n = sys.stdin.readline().split()
    
    if(n[0] == '1'):
        stack.append(n[1])
    elif(n[0] == '2'):
        if(len(stack) != 0):
            print(stack.pop())
        else:
            print('-1')
    elif(n[0] == '3'):
        print(len(stack))
    elif(n[0] == '4'):
        if(len(stack) != 0):
            print('0')
        else:
            print('1')
    elif(n[0] == '5'):
        if(len(stack) != 0):
            print(stack[-1])
        else:
            print('-1')