s = input()
s = s.lower()

new_s = list(set(s))
new_s.sort()
a = 0
te = []

for i in new_s:
    ch = s.count(i) #2
    if(ch > a): 
        te = [i]
        a = ch
    elif(ch == a):
        te.append(i)

if(len(te) == 1):
    print(te[0].upper())
else:
    print("?")