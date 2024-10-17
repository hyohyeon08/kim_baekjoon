score = 0

hag = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0}
re = 0

for i in range(20):
    sub, cl, major = input().split()
    if(major == "P"):
        continue
    
    score += float(cl) * hag[major]
    re += float(cl)
    
print(score / re)