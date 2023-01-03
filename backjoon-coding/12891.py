#https://www.acmicpc.net/problem/12891
#DNA비밀번호


'''
import sys
input = sys.stdin.readline

num_case , std_size = map(int, input().split())
dna_list = list(input())
require_list = list(map(int, input().split()))
start_idx = -1
end_idx = std_size-1
cnt = 0

while end_idx <= len(dna_list):
    start_idx += 1
    end_idx += 1
    if dna_list[start_idx:end_idx].count('A') >= require_list[0] and dna_list[start_idx:end_idx].count('C') >= require_list[1] and dna_list[start_idx:end_idx].count('G') >= require_list[2] and dna_list[start_idx:end_idx].count('T') == require_list[3]:
        cnt += 1


print(cnt)
'''

'''
import sys
input = sys.stdin.readline

num_case , std_size = map(int, input().split())
dna_list = list(input())
require_list = list(map(int, input().split()))

dna_list.append(0)
cnt = 0
start_idx = 0
end_idx = std_size-1

check_list = [dna_list[:std_size].count('A'),dna_list[:std_size].count('C'),dna_list[:std_size].count('G'),dna_list[:std_size].count('T')]

while end_idx < len(dna_list)-1:

    torn = True
    for j in range(len(check_list)):
        if (check_list[j] - require_list[j]) < 0:
            torn = False
            break
    if torn == True:
        cnt += 1

    if dna_list[start_idx] == 'A':
        check_list[0] -= 1
    elif dna_list[start_idx] == 'C':
        check_list[1] -= 1
    elif dna_list[start_idx] == 'G':
        check_list[2] -= 1
    elif dna_list[start_idx] == 'T':
        check_list[3] -= 1
        
    start_idx += 1
    end_idx += 1
    if dna_list[end_idx] == 'A':
        check_list[0] += 1
    elif dna_list[end_idx] == 'C':
        check_list[1] += 1
    elif dna_list[end_idx] == 'G':
        check_list[2] += 1
    elif dna_list[end_idx] == 'T':
        check_list[3] += 1

print(cnt)

'''
