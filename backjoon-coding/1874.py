#https://www.acmicpc.net/problem/1874
#스택 수열

a = int(input())
b = []
for _ in range(a):
    b.append(int(input()))

# a = 8
# b = [4,3,6,8,7,5,2,1]

c = [i for i in range(1,max(b)+1)]

now_num = b[0]
c_num = 0
cnt = 0
starts = ''
starts += ('+'* b[0])
starts += ('-')
c_num = c.index(b[0])
cnt = b[0]
c.remove(b[0])

for i in b[1:]:
    if i > now_num:
        now_num = i
        starts += ('+'* (i - cnt))
        starts += ('-')
        cnt = i
        c_num = c.index(i)
        c.remove(i)
    elif c.index(i) != c_num-1: #틀린경우
        print('NO')
        break    
    elif i < now_num:
        starts += ('-')
        c_num = c.index(i)
        c.remove(i)


if len(c) == 0:
    print('\n'.join(starts))
