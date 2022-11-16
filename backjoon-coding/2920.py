a = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
    if not a[i] > a[i -1]:
        ascending = False
    if not a[i] < a[i -1]:
        descending = False

if ascending == True:
    print('ascending')
elif descending == True:
    print('descending')
else:
    print('mixed')

##################################################################

aa = input()
# aa = '1 2 3 4 5 6 7 8'
if aa == '1 2 3 4 5 6 7 8':
    print('ascending')
elif aa == '8 7 6 5 4 3 2 1':
    print('descending')
else:
    print('mixed')