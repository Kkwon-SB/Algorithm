# 1.길이만큼 a아스키 코드로 변환
# 2. 중간값, 13 넘어가면 전체 26에서 값 빼기
# 3. 시작 방향은 처음과 끝에서 a의 갯수가 작은쪽을 방향으로 움직이기

# 65~90이 대문자 영문

def solution(name):
    # cnt = 0
    # i = 0
    # # name = list(name)
    # set_name = [65] * len(name)
    num_name  = [ord(i) for i in name]
    
    # #비교해서 더 가까운거리로 이동

    
    result_list = [i for i, value in enumerate(num_name) if value == 65]

    # if 65 in num_name: #있을 경우, 
    #     for 
    # else:#없으면 문자열 길이만큼 더해주면 됨
    #     cnt += (len(name)-1)

    # num_name[i]
    #     i+=1
    # print(set_name)


    


    return print(result_list)

solution('BBAAABB')