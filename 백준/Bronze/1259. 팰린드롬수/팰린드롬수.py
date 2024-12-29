while True:
    num = input()
    if(num == '0'): break
    check = num == num[::-1]
    print("yes" if check else 'no')