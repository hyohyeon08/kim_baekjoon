alpa = "abcdefghijklmnopqrstuvwxyz"

nn = int(input())
n = input()

a_hash = 0

for i in range(len(n)):
    a_hash += (alpa.find(n[i]) + 1) * 31**i

print(a_hash % 1234567891)
