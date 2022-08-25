def solution(n, lost, reverse):
    reverse.sort()  # 정렬
    lost.sort()

    # No.1
    # for j in reverse:     #제한사항5번, lost와 reserve에 같은 값이 있으면 양쪽 다 제거
    #     if j in lost:
    #         reverse.remove(j)
    #         lost.remove(j)

    # No.2                   #제한사항5번, lost와 reserve에 같은 값이 있으면 양쪽 다 제거
    reverse2 = []
    lost2 = []

    for z in reverse:
        if z not in lost:
            reverse2.append(z)

    for x in lost:
        if x not in reverse:
            lost2.append(x)

    for i in reverse2:
        if (i - 1) in lost2:
            lost2.remove(i - 1)

        elif (i + 1) in lost2:
            lost2.remove(i + 1)

    return n - (len(lost2))
