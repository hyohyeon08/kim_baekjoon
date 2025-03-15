num = int(input())

for i in range(num):
    ox = list(input())
    ch = 0
    p_ch = 0
    for j in ox:
        if j == 'O':
            ch += 1
            p_ch += ch
        else:
            ch = 0
    print(p_ch)
