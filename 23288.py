from collections import deque

N, M, K = map(int, input().split())
# 지도의 세로 크기 N, 가로 크기 M (2 ≤ N, M ≤ 20), 그리고 이동하는 횟수 K (1 ≤ K ≤ 1,000)
STATE = [list(map(int, input().split())) for _ in range(N)]
# N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. (< 10)

output = 0  # 각 이동에서 획득하는 점수의 합

'''
가장 왼쪽 위에 있는 칸의 좌표는 (1, 1)이고, 가장 오른쪽 아래에 있는 칸의 좌표는 (N, M)

** 주사위 전개도 **
  2
4 1 3
  5
  6

주사위가 초기 놓여져 있는 좌표는 (1,1)이다.
가장 처음에 주사위의 이동 방향은 동쪽이다.

주사위의 이동 한 번은 다음과 같은 방식으로 이루어진다.

1. 주사위가 이동 방향으로 한 칸 굴러간다.
** 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한 다음 한 칸 굴러간다.

2. 주사위가 도착한 칸 (x, y)에 대한 점수를 획득한다.
** 점수는 B X C
** (x, y)에 있는 정수를 B
** (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C를 모두 구한다. 이때 이동할 수 있는 칸에는 모두 정수 B가 있어야 한다. **

3. 주사위의 아랫면에 있는 정수 A와 주사위가 있는 칸 (x, y)에 있는 정수 B를 비교해 다음 이동 방향을 결정한다.
** A > B인 경우 이동 방향을 90도 시계 방향으로 회전시킨다.
** A < B인 경우 이동 방향을 90도 반시계 방향으로 회전시킨다.
** A = B인 경우 이동 방향에 변화는 없다.

'''


def OOR(y, x):
    if 0 <= y < N and 0 <= x < M:
        return False
    else:
        return True

def roll_dice(n_state, n_dir):  # n_dir : 상우하좌
    if n_dir == 0: return [n_state[1], n_state[2], n_state[3], n_state[0], n_state[4], n_state[5]]
    if n_dir == 1: return [n_state[0], n_state[4], n_state[2], n_state[5], n_state[3], n_state[1]]
    if n_dir == 2: return [n_state[3], n_state[0], n_state[1], n_state[2], n_state[4], n_state[5]]
    if n_dir == 3: return [n_state[0], n_state[5], n_state[2], n_state[4], n_state[1], n_state[3]]

def sel_dir(nA, nB, n_d):
    if nA > nB:
        return (n_d + 1) % 4
    elif nA < nB:
        return (n_d + 3) % 4
    elif nA == nB:
        return n_d

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 초기 조건
now_dice = [2, 1, 5, 6, 4, 3]
nr, nc, nd = 0, 0, 1

for _ in range(K):
    if OOR(nr + dy[nd], nc + dx[nd]): nd = (nd + 2) % 4
    # print(nd)

    nr, nc = nr + dy[nd], nc + dx[nd]
    now_dice = roll_dice(now_dice, nd)

    A = now_dice[3]
    B = STATE[nr][nc]
    C = 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    que = deque([(nr,nc)])
    
    # 성공 코드
    while True: 
        if not que: break

        r,c = que.popleft()
        visited[r][c] = True

        for d in range(4):
            tr, tc = r + dy[d], c + dx[d]

            if OOR(tr, tc) or visited[tr][tc] or STATE[tr][tc] != B: continue

            visited[tr][tc] = True
            que.append((tr,tc))

            C += 1
    
    # 실패 코드
    ''' 
    def check_continuity(que, now_c):
    global visited, B, C

    if not que: return

    r, c = que.popleft()
    visited[r][c] = True

    for d in range(4):
        if OOR(r + dy[d], c + dx[d]) or visited[r + dy[d]][c + dx[d]]: continue

        visited[r + dy[d]][c + dx[d]] = True

        if STATE[r + dy[d]][c + dx[d]] == B:
            now_c += 1
            que.append((r + dy[d], c + dx[d]))

            # print(f'd:{d} ({r + dy[d]} {c + dx[d]}), #{now_c}')

            check_continuity(que, now_c)

        else:
            if now_c > C: C = now_c
            visited[r + dy[d]][c + dx[d]] = False

            check_continuity(que, now_c)

    check_continuity(que, now_c)
    '''

    # check_continuity(deque([(nr, nc)]), C)

    output += (B * C)
    nd = sel_dir(A, B, nd)

    # print(A, B, C, nd)

print(output)
