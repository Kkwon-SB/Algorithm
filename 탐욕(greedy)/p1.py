"""
def solution(n, lost, reverse):
    cnt = 0
    ori = len(lost)
    
    reverse.sort() #정렬
    lost.sort()  
    
    for j in reverse: #제한사항5번, lost와 reserve에 같은 값이 있으면 양쪽 다 제거
        if j in lost:
            reverse.remove(j)
            lost.remove(j)
            
    for i in lost:  #앞 뒤 경우
        if (i - 1) in reverse:
            reverse.remove(i - 1)
            cnt+=1
        elif (i + 1) in reverse:
            reverse.remove(i + 1)
            cnt+=1

    return (n - (len(lost) - cnt))
    
    
solution(5,    [2, 4],    [1, 3, 5])
"""


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)