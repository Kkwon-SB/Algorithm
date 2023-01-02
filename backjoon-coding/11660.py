# 11590문제와 다른 점은 1차원에서 2차원으로 변경되었다는 점 -> 계산이 까다로워졌다

# 공식을 알면 크게 어렵지않은 문제라고 생각한다. 하지만 공식이 제공되지 않았다면 풀이에 어려움이 있었을 것이다.

box_size, q_num = map(int, input().split())

s = []

ori_d = [[0] * (box_size + 1)]
hap_d = [[0] * (box_size + 1) for _ in range(box_size + 1)]

for _ in range(box_size):
    a_row = [0] + [int(x) for x in input().split()]
    ori_d.append(a_row)

for i in range(1,box_size+1):
    for j in range(1,box_size+1):
        hap_d[i][j] = hap_d[i][j-1] + hap_d[i-1][j] - hap_d[i-1][j-1] + ori_d[i][j]

for _ in range(q_num):
    x1, y1, x2, y2 = list(map(int, input().split()))
    print(hap_d[x2][y2] - hap_d[x1-1][y2] - hap_d[x2][y1-1] + hap_d[x1-1][y1-1] )


