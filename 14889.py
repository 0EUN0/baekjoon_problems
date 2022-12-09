N = int(input()) # N: 참가인원의 수 (반으로 나누어 팀을 구성해야 함)
STATE = [list(map(int,input().split())) for _ in range(N)]

output = 100000000 # 스타트 팀과 링크 팀의 능력치 차이의 최솟값

'''
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

팀의 능력치는 팀에 속한 모든 쌍의 능력치의 합이다.

** Sij는 Sji와 다를 수도 있다.

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다.
'''

li = [i for i in range(N)]
comb = []

def dfs(que, depth):
    if len(que) == N // 2:
        comb.append(list(que))
        return
    elif depth == len(li):
        return

    que.append(li[depth])
    dfs(que, depth+1)

    que.pop()
    dfs(que, depth+1)

dfs([],0)

for S in comb:
    L = []

    for i in range(N):
        if i not in S: L.append(i)

    # print(S,L)

    start, link = 0,0

    for s1 in S:
        for s2 in S:
            start += STATE[s1][s2]

    for l1 in L:
        for l2 in L:
            link += STATE[l1][l2]

    if abs(start-link) < output: output = abs(start-link)

print(output)
