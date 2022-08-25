def solution(id_list, report, k):

    report = list(set(report))

    answer1 = {}
    for i in id_list:
        answer1[i] = 0

    aa = {}
    pre_answer = {}
    for i in report:
        n, b = i.split(" ")
        if b not in aa.keys():
            aa[b] = 1
        else:
            aa[b] += 1

    aa = [key for key, v in aa.items() if int(v) >= k]  # 임계값 넘긴 아이디 추출

    for i in report:  # 신고한 아이디가 임계값 넘긴 아이디인지 확인
        a, c = i.split(" ")
        if c in aa:
            answer1[a] += 1

    answer = list(answer1.values())
    return answer


# 39min
