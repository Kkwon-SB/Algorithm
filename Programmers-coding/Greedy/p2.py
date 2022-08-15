# 1.길이만큼 a아스키 코드로 변환
# 2. 중간값, 13 넘어가면 전체 26에서 값 빼기
# 3. 시작 방향은 처음과 끝에서 a의 갯수가 작은쪽을 방향으로 움직이기

# 65~90이 대문자 영문


"""
def solution(name):
    cnt = 0
    # name = list(name)
    num_name  = [ord(i) for i in name]


    for j in 

        for i in num_name:
            a =  abs(i - 65)

            if abs(i - 65) > 13:  #중간값이 넘어가는 경우
                cnt += (90-i+1)
                print(i,"=",90-i+1)

            else:                  #중간값이 넘아가지 않는 경우
                cnt += (i-65)
                print(i,"=",i-65)

    


    return print(cnt)

solution('JEROEA')
"""