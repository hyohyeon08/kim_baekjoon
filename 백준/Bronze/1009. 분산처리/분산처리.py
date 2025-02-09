# n =int(input())

# for i in range(n):
#     a, b = map(int, input().split())
#     print(a**b % 10)
n =int(input())

for i in range(n):
    a,b=map(int,input().split())
    base=a%10
    
    if(base == 0): # 10으로 나눠짐
        print(10)
    elif(base == 1 or base == 5 or base == 6): #무엇을 제곱해도 1, 5, 6고정
        print(base)
    elif(base == 4 or base == 9): #4, 9는 거듭 제곱의 2칸 반복됨 : 그대로 가지거나 제곱한 값
        if b % 2 == 0:
            print((base**2)%10)
        else:
            print(base)
    else: # 2,3,7,8은 거듭 제곱이 4칸 반복
        if(b % 4 == 0): # 0 나눠지지 않으므로 미리 검사
            print((base**4)%10)
        else:
            print((base**(b%4))%10)
