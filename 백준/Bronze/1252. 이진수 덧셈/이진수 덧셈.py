a, b = input().split()
a = int(a, 2)
b = int(b, 2)

answer = bin(a+b)
print(answer[2:])