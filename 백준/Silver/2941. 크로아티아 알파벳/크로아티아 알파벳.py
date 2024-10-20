a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

text = input()
d = len(text)


for i in a:
    d -= text.count(i)

print(d)