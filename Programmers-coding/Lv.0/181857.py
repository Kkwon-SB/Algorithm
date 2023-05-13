#https://school.programmers.co.kr/learn/courses/30/lessons/181857
#배열의 길이를 2의 거듭제곱으로 만들기

'''
놓친부분)
1. 2의 0제곱은 1이다.
2. arr의 길이가 1000이하로 설정되어 있는데 512길이가 넘어가면 1000이하의 2거듭제곱이 없기 때문에 temp마지막 요소를 512값을 넣고 result길이를 설정했다. 하지만 arr길이가 아닌 result길이는 제한된 조건이 없었다는 것, 그럼에도 result 길이는 최대 1024를 넘길 수 없다. arr길이가 최댓값인 1000이라 해도 다음에 오는 2거듭제곱은 1024이기 때문.  
'''
def solution(arr):
    #초기 temp = [2,4,8,16,32,64,128,256,512] => 실제 채점 과정에서 10개 정도 틀렸다고 나옴
    temp = [1,2,4,8,16,32,64,128,256,512,1024]
    
    for i in temp:
        if i - len(arr) >= 0:
            arr+= [0] * (i - len(arr))
            return arr