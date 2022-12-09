########### 정답 코드 ##############

N, M = map(int,input().split())
State = [list(map(int,input().split())) for _ in range(N)]

output = 10000000000000

'''
0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치이다. 

가장 처음에 모든 바이러스는 비활성 상태
연구소의 바이러스 중 M개를 활성 상태로 변경 @ 

활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다.

활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

연구소의 모든 빈 칸(0)에 바이러스가 있게 되는 최소 시간을 출력한다.
바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.
'''

viruses = []
num = 0

for i in range(N):
    for j in range(N):
        if State[i][j] == 2: viruses.append((i,j))
        elif State[i][j] == 0: num += 1

virus_subset = []

from collections import deque
from xml.etree.ElementTree import QName

def make_subset(subset, depth):
    if len(subset) == M:
        virus_subset.append(list(subset))
        return
    elif depth == len(viruses):
        return
    
    subset.append(viruses[depth])
    make_subset(subset, depth + 1)

    subset.pop()
    make_subset(subset, depth + 1)

make_subset(deque(), 0)

dy = [-1,0,1,0]
dx = [0,-1,0,1]

def out_of_range(y,x):
    if 0 <= y <= N-1 and 0 <= x <= N-1: return False
    else: return True
  

for vi_sub in virus_subset:
    Q = deque(vi_sub)

    S, NU = [[0 for _ in range(N)] for _ in range(N)], num

    for i in range(N):
        for j in range(N):
            if (i,j) in vi_sub: S[i][j] = 1
            else: S[i][j] = State[i][j]

    CNT = 0

    while True:
        NEW_Q = deque()

        while True:
            if len(Q) == 0 or NU == 0:
                Q = NEW_Q.copy()
                CNT += 1
                break

            r,c = Q.popleft()

            for d in range(4):
                nr, nc = r + dy[d], c + dx[d]

                if out_of_range(nr,nc): continue
                
                if S[nr][nc] == 0 or S[nr][nc] == 2: 
                    if S[nr][nc] == 0: NU -= 1

                    S[nr][nc] = 1
                    NEW_Q.append((nr,nc))

        if NU == 0:
            break
        else: 
            if len(NEW_Q) == 0:
                CNT = 10000000000000
                break

    if CNT < output: output = CNT

if output == 10000000000000: print(-1)
elif num == 0: print(0)
else: print(output)

########### 틀린 코드 (채점 중 94%에서) ##############

N, M = map(int, input().split())
state = [list(map(int, input().split())) for _ in range(N)]

output = 10000000

'''
# N:연구소의 크기 M:바이러스의 개수
# state: 연구소의 상태 | 0(빈칸) 1(벽) 2(바이러스 놓을 수 있는 위치) > 최소 M개 최대 10개
# 연구소 내 모든 빈칸에 바이러스 있게 되는 최소 시간 출력 
  | 어떻게 해도 모든 칸에 못 놓으면 -1 출력
'''

'''
바이러스는 활성 상태와 비활성 상태가 있다.
가장 처음에 모든 바이러스는 비활성 상태이다. > 연구소의 바이러스 M개를 활성 상태로 변경한다. @
활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 
활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.

모든 빈 칸에 활성 바이러스를 퍼뜨리는 최소 시간을 구해보자.
'''
from collections import deque

virus = []

for i in range(N):
    for j in range(N):
        if state[i][j] == 2: virus.append((i, j))

virus_subset = []


def make_subset(subset, depth):
    if len(subset) == M:
        virus_subset.append(list(subset))
        return
    elif depth == len(virus):
        return

    subset.append(virus[depth])
    make_subset(subset, depth + 1)

    subset.pop()
    make_subset(subset, depth + 1)


make_subset(deque(), 0)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def check_virus(now_visited, now_state, now_que, num):
    while True:
        if len(now_que) == 0 or num == 0:

            maxi = 0

            for i in range(N):
                for j in range(N):
                    if (maxi < now_state[i][j]) and (now_state[i][j] != 10000):
                        maxi = max(now_state[i])

            return maxi

        r, c = now_que.popleft()
        now_visited[r][c] = True

        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]

            if (0 <= nr <= N - 1) and (0 <= nc <= N - 1):
                if (now_visited[nr][nc] is False) and now_state[nr][nc] > now_state[r][c] + 1:
                    if now_state[nr][nc] != 10000: 
                        num -= 1

                    now_state[nr][nc] = now_state[r][c] + 1
                    now_que.append((nr, nc))


for s in virus_subset:
    que, num = deque(s), 0

    lab_visited = [[False for _ in range(N)] for _ in range(N)]
    lab_state = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if state[i][j] == 0:  # 빈칸
                lab_state[i][j], lab_visited[i][j] = 10000000, False
                num += 1
            if state[i][j] == 1:  # 벽
                lab_state[i][j], lab_visited[i][j] = -10000000, True
            elif state[i][j] == 2:  # 바이러스
                lab_state[i][j], lab_visited[i][j] = 0, True
                if (i, j) not in s: lab_state[i][j], lab_visited[i][j] = 10000, False

    MAX = check_virus(lab_visited, lab_state, que, num)
    if MAX < output: output = MAX

if output == 10000000: print(-1)
else: print(output)
