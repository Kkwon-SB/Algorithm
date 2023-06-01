#https://school.programmers.co.kr/learn/courses/30/lessons/42862
#체육복

'''
key)
1. 중복제거 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
2. 최적값을 구하기 위해 두 배열 정렬시켜야 함
'''

def solution(n, lost, reserve):
    cnt = 0
    
    #중복제거 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
    #set 과정에서 정렬이 되었기 때문에 가능했으나, 별로도 정렬해주어야 한다.
    overlap = set(lost) & set(reserve)
    lost = list(set(lost) - overlap)
    reserve = list(set(reserve) - overlap)
    
    
    # _reserve = [r for r in reserve if r not in lost]
    # _lost = [l for l in lost if l not in reserve]
    # _reserve.sort()
    # _lost.sort()
    
    for i in lost:

        if i-1 in reserve:
            reserve.remove(i-1)
            cnt += 1
            continue
        if i+1 in reserve:
            reserve.remove(i+1)
            cnt += 1
            continue         
            
        continue
            
    return n - len(lost) + cnt
    

'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    
    _lost.sort()
    _reserve.sort()
    
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''
