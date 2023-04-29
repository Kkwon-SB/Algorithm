'''
#구현 - 시각 (20분)

하루의 모든 시간의 경우는 86400가지, (초단위)
제한시간2초이기 때문에 전체를 살펴보면된다.
'''
hours = int(input())
cnt = 0

for hour in range(hours+1):
    for min in range(60):
        for sec in range(60):=
            if '3' in (str(hour) + str(min) + str(sec)):
                cnt += 1
print(cnt)


''' 
다른 방법으로 푼 방법 : 시간당 경우의 수가 정해져 있음 (시간 단위에 3포함되어있을 경우 (3, 13,23) + 3600 )

#3중 for문을 2중 for문으로 바꿈 - O(n3) 에서 O(n2) 단축 

'''
hours = int(input())

cnt = 0
three = 0

if hours >= 23:
    three += 3
elif hours >= 13:
    three += 2
elif hours >= 3:
    three += 1

for min in range(60):
    for sec in range(60):
        if '3' in (str(min) + str(sec)):
                cnt += 1

print(cnt*((hours+1) - three) + 3600 * three)
