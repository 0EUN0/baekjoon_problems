- 경우의 수 잘 확인하기
- deepcopy 사용 자제

from collections import deque
from copy import deepcopy
deepcopy 시간이 오래 걸려서 사용했을 때 시간 초과로 1%도 정답 인정 안됨
사용 안 할 수 있으면 왠만하면 안하기 추천

N,M = map(int, input().split())
STATE = [list(map(int, input().split())) for _ in range(N)]

output = 0

# 상 하 좌 우
dy = [-1,1,0,0]
dx = [0,0,-1,1]


def find_way(check_index):
    if check_index == 0: return [[0]*3,[2]*3]
    if check_index == 1: return [[3,1,2]]
    if check_index == 2: return [[1,1,3],[1,1,2],[2,2,1],[3,3,1],[0,0,2],[0,0,3],[3,3,0],[2,2,0]]
    if check_index == 3: return [[1,3,1],[1,2,1],[2,1,2],[3,1,3]]
    if check_index == 4: return [[3,3,2,1],[1,1,0,2],[2,2,3,0],[0,0,1,3]]


def OOR(y, x):
    if 0 <= y < N and 0 <= x < M: return False
    else: return True


def check(r, c, now):
    global output

    # print(r, c, end=' ')

    cnt = STATE[r][c]
    th = 0

    while True:
        if not now:
            break

        d = now.popleft()
        th += 1

        r, c = r + dy[d], c + dx[d]

        if OOR(r, c):
            return
        if index == 4 and th == 3: continue
				
				4번째 경우 중간에 다시 돌아오는 과정에서 cnt 하지 말아야 하기 때문에 STATE deepcopy해서 0로 만들어주는 방법을 사용했었는데, 
				그냥 index가 4번이고 _th 변수 새로 사용해 3번째에 해당한다면 cnt에 더해지지 않도록 하면 되는 건데 귀찮아서 않해가지고 시간초과 떴음 . . .
				내가 귀찮으면 사용자가 불편하다 무슨 브랜드 어쩌고에서 봤는데 아주 체감되는 경우

        cnt += STATE[r][c]
        # print(r, c, end = ' ')

    if cnt > output:
        # print('cnt:',cnt)
        # for X in STATE: print(X)

        output = cnt

    return


for index in range(5):
    way = find_way(index)
    # print(index)

    for i in range(N):
        for j in range(M):
            for now_way in way:
                # print(now_way)
                check(i, j, deque(now_way))

print(output)
