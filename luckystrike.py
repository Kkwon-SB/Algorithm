# 럭키스트라이크

n = list(map(int, list(input())))

half = len(n) // 2
left = sum(n[ : half])
right = sum(n[half : ])

if left == right:
    print('LUCKY')
else:
    print('READY')
