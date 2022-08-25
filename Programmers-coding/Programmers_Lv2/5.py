##기능 개발


def solution(progresses, speeds):
    j = 0
    cnt = 0
    answer = []

    while j < len(progresses):
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        while progresses[j] >= 100:
            j += 1
            cnt += 1
            if j == len(progresses):
                break

        if cnt > 0:
            answer.append(cnt)
        cnt = 0

    return answer
