#https://school.programmers.co.kr/learn/courses/30/lessons/181858
#무작위로 K개의 수 뽑기

def solution(arr, k):
    ans = []
    
    for i in arr:
        if i not in ans:
            ans.append(i)
    
    if len(ans) == k:
        return ans
    if len(ans) < k:
        return ans + ([-1] * (k - len(ans)))
    if len(ans) > k:
        return ans[:k]



#처음 작성한 코드, 테스트 과정은 통과됐지만, 실제 체점에서 전부 '실패' 결과가 나왔다. 곰곰히 생각해봐도 아직 이유를 찾지 못했다. 
'''
def solution(arr, k):
    arr = list(set(arr))
    arr.sorted(arr)
    
    if len(arr) >= k:
        return arr[:k]
    else:
        arr += [-1] * (k - len(arr))
        return arr
'''    
'''
def solution(arr, k):
    answer = []
    for num in arr:
        if len(answer) >= k:
            break
        if num not in answer:
            answer.append(num)
    if len(answer) < k: 
        answer.extend([-1]* (k - len(answer)))
    return answer
'''
