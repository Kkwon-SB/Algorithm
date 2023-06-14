#https://school.programmers.co.kr/learn/courses/30/lessons/42888
#오픈 채팅방

def solution(record):
    members = {}
    answer = []

    for i in range(len(record)):            #아이디와 이름을 딕셔너리type으로 저장
        a = record[i].split()
        if len(a) == 2:                     #원래 이름과 이름을 변경하는 경우 catch
            pass
        else:
            members[a[1]] = a[2]


<<<<<<< HEAD

=======
>>>>>>> 4cd9a33060c7fdb6c7ee09fa0fb5c3866f4539a1
    for i in range(len(record)):            #원본의 record 데이터를 순차적으로 돌며, 저장된 id의 이름을 딕셔러니에서 가져온다
        member = record[i].split()
        if member[0] == 'Enter':
            answer.append(members[member[1]]+"님이 들어왔습니다.")

        elif member[0] == 'Leave':
            answer.append(members[member[1]]+"님이 나갔습니다.")
        else:
            pass
    

    return answer
