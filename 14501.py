맞았는데 왜 맞았는지 모르겠다 . . .
pypy로 하니까 메모리 초과 떠서 python으로 돌려봤는데 성공함 > 어이 업서 ..

import sys
sys.setrecursionlimit(10**9)
recursion 오류 떠서 recursion 가능 횟수를 키워주는 코드 추가 (삼성 코테에선 sys 사용 불가한데 어쩌지 .. .)

N = int(input()) # N: 남은 일수
ARR = [list(map(int,input().split())) for _ in range(N)]
# ARR: 각 줄에 T 와 P가 주어진다. T: 상담 필요 기간  P: 이익

output = 0 # 최대 이익

'''
상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다.
N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다. (6,7일 상담 기간 > 1,2일 경우)
'''

INFO = []
for i in range(len(ARR)):
    INFO.append((i, ARR[i][0], ARR[i][1]))

이 부분에 대한 복습이 필요하다.
comb = []

def dfs(que, nowday):
    if nowday >= N:
        if comb and set(que).issubset(set(comb[-1])): return
				set: issubset: 부분집합인지 판단해주는 python 내장 함수

        comb.append(list(que))
        return

    que.append(INFO[nowday])
    nowday += que[-1][1]

    if nowday > N:
        d, q, w = que.pop()
        dfs(que, d+1)
    else:
        dfs(que, nowday)

    if que:
        d, q, w = que.pop()
        dfs(que, d+1)
    else:
        return

dfs([],0)

#print(comb)

for C in comb:
    profit = 0

    for _,_,price in C:
        profit += price

    if profit > output: output = profit

print(output)

'''
3
1 5
3 1
1 1
Ans = 6 (반례였던 것)
'''
