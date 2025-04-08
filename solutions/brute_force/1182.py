import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

cnt = 0 # 부분수열의 개수

# 부분수열을 만들 수 있는 경우의 수는 NCr
for r in range(1, N+1):
    subseq_list = list(combinations(seq, r))
    
    # 부분수열의 합이 S이면 개수 카운트
    for subseq in subseq_list:
        sum_subseq = sum(subseq)
        if sum_subseq == S: cnt += 1

print(cnt)