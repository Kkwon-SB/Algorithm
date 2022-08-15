def solution(brown, yellow):
    y_list = []

    for a in range(1, yellow+1 ):
        if yellow % a == 0:
            y_list.append(a)

    if len(y_list) % 2 == 0: #짝수 
        return print(y_list[(len(y_list)//2)]+2, y_list[(len(y_list)//2)-1]+2)
    else:
        return print(y_list[(len(y_list)//2)]+2, y_list[(len(y_list)//2)]+2)

solution(18, 6)

# print(3 // 2)