n = int(input())
check = 0

while n > 0:
    if(n >= 3):
        n -= 3
        check += 1
    else:
        n -= 1
        check += 1
        
print("CY") if check % 2 ==0 else print("SK")