https://school.programmers.co.kr/learn/courses/30/lessons/42885
#구명보트 

def solution(people, limit):
    people.sort()

    front = 0
    last = len(people)-1
    boat = 0

    while (front < last) and (front != last):
        if people[front] + people[last] <= limit:
            front += 1
            last -= 1
            boat += 1
        else:
            boat += 1
            last -= 1
    if front == last:
        boat += 1
    
    return boat
