#https://school.programmers.co.kr/learn/courses/30/lessons/181894
#2의 영역

def solution(arr):
    answer = []
    
    try:
        st = arr.index(2)
        arr.reverse()
        ed = len(arr) - arr.index(2)
        arr.reverse()
        return arr[st:ed] 
        
    except ValueError:
        return [-1] 
    
  '''case2
  def solution(arr):
  if 2 not in arr:
      return [-1]

  return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
  '''
