def solution(people, limit):
    boat = 1
    people.sort()

    front = 0               #smallest
    last = len(people)-1    #biggest

    while (front != last) or (front < last):

        if people[front] + people[last] <= limit: #2명 가능
            front += 1
            last -= 1
        else:                                  #혼자만 가능
            boat += 1
            last -= 1
    
    return boat
"""
def solution(people, limit):
    people.sort()

    front = 0
    last = len(people)-1
    acc_weight = people[last]
    boat = 1

    while front == last:
    # for i in range(len(people)-1, -1, -1):
        if people[front] + people[last] >= limit:
            acc_weight += people[front]
            front += 1
        else:
            acc_weight = 0
            boat += 1
            last -= 1
    return print(boat)

solution([70, 50, 80, 50], 100)

def solution(people, limit):
    people.sort()

    if people[0] > (limit/2): #2명 이상 태울 수 없는 경우
        return len(people)
        
    # for i in range(0, len(people)-1):    
    i = 1
    total_weight = people[0] #누적 무게
    boat = 0
    while i == len(people):
        if (total_weight + (people[i])) <= limit: #보트에 더 태울 수 있는 경우
            total_weight += people[i]
            i += 1
        else:           #보트에 더 태울 수 없는 경우
            total_weight = 0
            boat += 1
            i += 1

    return print(boat)

solution([70, 50, 80, 50], 100)
"""