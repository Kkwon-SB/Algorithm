#왕실의 나이트

'''
경우의 수가 8가지이므로 직접 구현
'''

now = input()

list(now)
answer = 0

if int(now[1]) > 2 and str(now[0]) < 'h':
    answer += 1
if int(now[1]) > 2 and now[0] > 'a':
    answer += 1
if int(now[1]) < 7 and now[0] < 'h':
    answer += 1
if int(now[1]) < 7 and now[0] > 'a':
    answer += 1
if int(now[1]) > 2 and now[0] < 'g':
    answer += 1
if int(now[1]) < 7 and now[0] < 'g':
    answer += 1
if int(now[1]) > 2 and now[0] > 'c':
    answer += 1
if int(now[1]) < 7 and now[0] > 'c':
    answer += 1

print(answer)
