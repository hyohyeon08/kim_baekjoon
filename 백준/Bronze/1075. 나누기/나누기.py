a = int(input())
b = int(input())

a //= 100
a *= 100

while True:
    if(a % b == 0):
        break
    a += 1

print(str(a)[-2:].zfill(2))