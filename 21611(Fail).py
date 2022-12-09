# 시간초과로 실패지만 Test Case 는 다 맞으니까 걍 넘어가기 . . . 왜냠 시간 없어

N, M = map(int, input().split())  # N: 구슬 격자의 크기 M: 블리자드 연습 횟수
MARBLE = [list(map(int, input().split())) for _ in range(N)]  # 구슬의 정보
MAGIC = [list(map(int, input().split())) for _ in range(M)]  # 마법 관련 정보

first, second, third = 0, 0, 0  # output: 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)
'''
격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)
마법사 상어는 ((N+1)/2, (N+1)/2)에 있다.
칸과 칸 사이에는 벽이 세워져 있다.

MARBLE: 구슬이 없으면 0 상어가 있는 칸도 항상 0
상어가 있는 칸을 제외한 나머지 칸에는 구슬이 하나 들어갈 수 있다.
구슬은 1번 구슬, 2번 구슬, 3번 구슬이 있다.
같은 번호를 가진 구슬이 번호가 연속하는 칸에 있으면, 그 구슬을 연속하는 구슬이라고 한다.
'''

'''
MAGIC: (d,s) d: 마법의 방향 s: 거리
4가지 방향 ↑, ↓, ←, →가 있고, 정수 1, 2, 3, 4로 나타낸다.

1. 상어는 di 방향으로 거리가 si 이하인 모든 칸에 얼음 파편을 던져 그 칸에 있는 구슬을 모두 파괴한다.
2. 구슬이 파괴되면 그 칸은 구슬이 들어있지 않은 빈 칸이 된다.

3. 만약 어떤 칸 A의 번호보다 번호(격자마다 매겨져 있음)가 하나 작은 칸이 빈 칸이면,
A에 있는 구슬은 그 빈 칸으로 이동한다.
4. 이 이동은 더 이상 구슬이 이동하지 않을 때까지 반복된다.

5. 이제 4개 이상 연속하는 구슬이 폭발하는 단계이다.
6. 구슬이 폭발해 빈 칸이 생겼으니 다시 구슬이 이동한다.

7. 구슬이 이동한 후에는 다시 구슬이 폭발하는 단계
8. 이 과정은 더 이상 폭발하는 구슬이 없을때까지 반복

9. 이제 더 이상 폭발한 구슬이 없기 때문에, 구슬이 변화하는 단계
- 연속하는 구슬은 하나의 그룹
- 하나의 그룹은 두 개의 구슬 A와 B로 변한다.
- 구슬 A의 번호는 그룹에 들어있는 구슬의 개수 2
- B는 그룹을 이루고 있는 구슬의 번호 1
- 구슬은 다시 그룹의 순서대로 1번 칸부터 차례대로 A, B의 순서로 칸에 들어간다.
* 그룹 하나가 2개의 구슬이 된다. 1개도 2개 2개도 2개 3개도 2개 ---
- 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.
'''

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

m_dy = [0, 1, 0, -1]
m_dx = [-1, 0, 1, 0]


def out_of_range(y, x):
    if 0 <= y < N and 0 <= x < N: return False
    else: return True


def check(VALUE):
    global first, second, third

    if VALUE == 1: first += 1
    elif VALUE == 2: second += 1
    elif VALUE == 3: third += 1


def move_marble(m_direction, move_count, m_distance, move_marble_cnt):
    global m_r, m_c

    for z in range(m_distance):
        m_r, m_c = m_r + m_dy[m_direction], m_c + m_dx[m_direction]

        if out_of_range(m_r, m_c):
            if move_marble_cnt >= 1:
                return True
            else:
                return False

        if MARBLE[m_r][m_c] == 0:
            if z != (m_distance - 1):
                next_m_r, next_m_c = m_r + m_dy[m_direction], m_c + m_dx[m_direction]
            else:
                next_m_r, next_m_c = m_r + m_dy[(m_direction + 1) % 4], m_c + m_dx[(m_direction + 1) % 4]

            if out_of_range(next_m_r, next_m_c):
                if move_marble_cnt >= 1:
                    return True
                else:
                    return False

            if MARBLE[next_m_r][next_m_c] != 0:
                MARBLE[m_r][m_c] = MARBLE[next_m_r][next_m_c]
                MARBLE[next_m_r][next_m_c] = 0

                move_marble_cnt += 1

    m_direction = (m_direction + 1) % 4
    move_count += 1

    if move_count == 2:
        move_count = 0
        m_distance += 1

    TF = move_marble(m_direction, move_count, m_distance, move_marble_cnt)

    return TF


def burst_marble(m_direction, move_count, m_distance, burst_marble_cnt):
    global m_r, m_c, n_cnt, n_r_c

    for z in range(m_distance):
        m_r, m_c = m_r + m_dy[m_direction], m_c + m_dx[m_direction]

        if out_of_range(m_r, m_c):
            if burst_marble_cnt >= 1:
                return True
            else:
                return False

        if (m_r, m_c) not in n_r_c: n_r_c.append((m_r, m_c))

        if z != (m_distance - 1):
            next_m_r, next_m_c = m_r + m_dy[m_direction], m_c + m_dx[m_direction]
        else:
            next_m_r, next_m_c = m_r + m_dy[(m_direction + 1) % 4], m_c + m_dx[(m_direction + 1) % 4]

        if out_of_range(next_m_r, next_m_c):
            if burst_marble_cnt >= 1:
                return True
            else:
                return False

        if MARBLE[m_r][m_c] == MARBLE[next_m_r][next_m_c]:
            n_cnt += 1

            if (next_m_r, next_m_c) not in n_r_c:
                n_r_c.append((next_m_r, next_m_c))
        else:
            if n_cnt >= 3:
                for n_r, n_c in n_r_c:
                    check(MARBLE[n_r][n_c])

                    MARBLE[n_r][n_c] = 0

                burst_marble_cnt += 1

            n_cnt, n_r_c = 0, []

    m_direction = (m_direction + 1) % 4
    move_count += 1

    if move_count == 2:
        move_count = 0
        m_distance += 1

    TF = burst_marble(m_direction, move_count, m_distance, burst_marble_cnt)

    return TF


def new_marble(nr, nc, m_direction, move_count, m_distance, A, B):
    global new_MARBLE

    for z in range(m_distance):
        nr, nc = nr + m_dy[m_direction], nc + m_dx[m_direction]

        if out_of_range(nr, nc): return

        if new_MARBLE[nr][nc] == 0:
            new_MARBLE[nr][nc] = A

            if z != (m_distance - 1):
                next_nr, next_nc = nr + m_dy[m_direction], nc + m_dx[m_direction]
            else:
                next_nr, next_nc = nr + m_dy[(m_direction + 1) % 4], nc + m_dx[(m_direction + 1) % 4]

            if out_of_range(next_nr, next_nc): return

            new_MARBLE[next_nr][next_nc] = B
            return

    m_direction = (m_direction + 1) % 4
    move_count += 1

    if move_count == 2:
        move_count = 0
        m_distance += 1

    new_marble(nr, nc, m_direction, move_count, m_distance, A, B)
    return


def change_marble(m_direction, move_count, m_distance):
    global m_r, m_c, n_cnt, n_r_c

    for z in range(m_distance):
        m_r, m_c = m_r + m_dy[m_direction], m_c + m_dx[m_direction]

        if out_of_range(m_r, m_c): return

        if (m_r, m_c) not in n_r_c: n_r_c.append((m_r, m_c))

        if z != (m_distance - 1): next_m_r, next_m_c = m_r + m_dy[m_direction], m_c + m_dx[m_direction]
        else: next_m_r, next_m_c = m_r + m_dy[(m_direction + 1) % 4], m_c + m_dx[(m_direction + 1) % 4]

        if out_of_range(next_m_r, next_m_c): return

        if MARBLE[m_r][m_c] == MARBLE[next_m_r][next_m_c]:
            n_cnt += 1

            if (next_m_r, next_m_c) not in n_r_c:
                n_r_c.append((next_m_r, next_m_c))
        else:
            new_marble(int(N // 2), int(N // 2), 0, 0, 1, n_cnt, MARBLE[n_r_c[0][0]][n_r_c[0][1]])

            n_cnt, n_r_c = 1, []

    m_direction = (m_direction + 1) % 4
    move_count += 1

    if move_count == 2:
        move_count = 0
        m_distance += 1

    change_marble(m_direction, move_count, m_distance)
    return


for direction, distance in MAGIC:
    sr, sc = int(N // 2), int(N // 2)

    direction -= 1
		
    for _ in range(distance):
        sr, sc = sr + dy[direction], sc + dx[direction]
				1) 상어가 구슬을 파괴한다.

        if out_of_range(sr, sc): break

        MARBLE[sr][sc] = 0

    while True:
        m_r, m_c = int(N // 2), int(N // 2)
				2) 빈칸이 없도록 구슬을 이동시킨다.

        TF_check = move_marble(0, 0, 1, 0)

        if TF_check is False: break

    while True:
        m_r, m_c = int(N // 2), int(N // 2)
        n_cnt, n_r_c = 0, []
				3) 4개 이상 연결되어 있는 구슬은 폭파되고, 폭파 후 빈칸이 없도록 구슬을 이동시킨다. 
				이동 후, 또다시 4개 이상 연결되어 있는 구슬이 있을 경우 위 과정을 반복한다.

        B_TF_check = burst_marble(0, 0, 1, 0)

        while True:
            m_r, m_c = int(N // 2), int(N // 2)

            TF_check = move_marble(0, 0, 1, 0)

            if TF_check is False: break

        if B_TF_check is False: break

    new_MARBLE = [[0 for _ in range(N)] for _ in range(N)]
		4) 구슬 그룹에 대한 설명에 따라 그룹을 형성하고, 구슬을 변화시킨다.

    n_cnt, n_r_c = 1, []
    m_r, m_c = int(N // 2), int(N // 2)

    change_marble(0, 0, 1)
    MARBLE = new_MARBLE


print(first * 1 + second * 2 + third * 3)
