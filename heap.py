#min heap
import heapq

def heapsort(array):
    h = []
    result = []

    for value in array:
        heapq.heappush(h, -value)
    
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])

print(result)
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


#max heap - 따로 방법이 없기 때문에 음수 전환 2번으로 대체
import heapq

def heapsort(array):
    h = []
    result = []

    for value in array:
        heapq.heappush(h, value)
    
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])

print(result)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

