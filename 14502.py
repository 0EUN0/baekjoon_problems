BFS, DFS, 백 트래킹 등 일정한 방법 외워두기

from collections import deque

N, M = map(int,input().split()) # N: 지도의 세로 M: 지도의 가로 크기
STATE = [list(map(int,input().split())) for _ in range(N)] # 지도의 모양

output = 0 # 안전 영역의 최대 크기

'''
0: 빈칸 1: 벽 2: 바이러스 위치

1. ** 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다. @
2. 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다.
3. 벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다.

안전 영역의 최대값을 구해라
'''
def OOR(y,x):
    if 0 <= y < N and 0 <= x < M: return False
    else: return True

dy = [-1,0,1,0]
dx = [0,-1,0,1]

VIRUS, CAN_WALL = [], []
for i in range(N):
    for j in range(M):
        if STATE[i][j] == 0: CAN_WALL.append((i,j))
        elif STATE[i][j] == 2: VIRUS.append((i,j))

WALL_SUBSETS = []
def make_subset(subset, depth): 조합을 만드는 DFS
    if len(subset) == 3:
        WALL_SUBSETS.append(list(subset))
        return
    elif depth == len(CAN_WALL):
        return

    subset.append(CAN_WALL[depth])
    make_subset(subset, depth + 1)

    subset.pop()
    make_subset(subset, depth + 1)

make_subset([],0)

def check_safety(COPY_STATE):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if COPY_STATE[i][j] == 0:
                cnt += 1

    return cnt

for WALL in WALL_SUBSETS:
    COPY_STATE = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if (i,j) in WALL: COPY_STATE[i][j] = 1
            else: COPY_STATE[i][j] = STATE[i][j]

    que = deque(VIRUS)

    while que: BFS
        r,c = que.popleft()

        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]

            if OOR(nr,nc): continue

            if COPY_STATE[nr][nc] == 0: # 빈 칸인 경우
                COPY_STATE[nr][nc] = 2
                que.append((nr,nc))

    cnt = check_safety(COPY_STATE)

    if output < cnt: output = cnt

print(output)
