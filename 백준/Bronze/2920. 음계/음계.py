ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]

m = list(map(int, input().split()))

if ascending == m:
    print('ascending')
elif descending == m:
    print('descending')
else:
    print('mixed')
