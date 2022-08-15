##123나라의 숫자

#주어진 값을 3으로 나누어준다
#맞아떨어지면 몫 -1 ,나머지 있으면 그대로
#몫이 3보다 작아질 때 까지 계속 3으로 나누어 준다

#나머지 0 => 4, 1=>1, 2=>2


ans_list = ["4", "1", "2"]

def solution(n):
    answer = ""

    while n:
        n, rest = divmod(n, 3)
        answer += ans_list[rest]
        if rest == 0:
            n -= 1
    return(''.join(reversed(answer)))