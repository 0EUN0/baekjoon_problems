**y,x,d1,d2 범위를 정하는 게 까다로웠던 문제**

**전에 경험해보지 못한 형태의 문제라 당황했지만 ,,, 호랑이 굴에 들어가도 정신만 차리면 산다고 했다.**

**당황하지말고, 문제를 제대로 이해한 뒤 print 문 활용하며 코딩하면 쉽게 풀 수 있는 문제**

N = int(input())  # 재현시의 크기
POPULATION = [list(map(int, input().split())) for _ in range(N)]  # N*N의 정수값

output = []  # (인구가 가장 많은 선거구 - 가장 적은 선거구)의 최솟값

'''
선거구 획정 방법

N*N 격자를 다섯 개의 선거구로 나누어야 한다.
각 구역(격자 한 칸)은 다섯 선거구 중 하나에 무조건 포함되어야 한다.
선거구는 구역을 적어도 하나 포함해야 한다.
한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다.

선거구를 나누는 방법은 다음과 같다.
1) 기준점 (x, y)와 경계의 길이 d1, d2를 정한다.
    d1, d2 ≥ 1,
    1 ≤ x < x+d1+d2 ≤ N,
    1 ≤ y-d1 < y < y+d2 ≤ N
2) 경계선과 경계선 안에 포함되어 있는 곳은 5번 선거구이다.
3) 5번 선거구에 포함되지 않은 구역의 선거구 번호는 다음 기준을 따른다.
    1번 선거구: 1 ≤ r < x+d1, 1 ≤ c ≤ y
    2번 선거구: 1 ≤ r ≤ x+d2, y < c ≤ N
    3번 선거구: x+d1 ≤ r ≤ N, 1 ≤ c < y-d1+d2
    4번 선거구: x+d2 < r ≤ N, y-d1+d2 ≤ c ≤ N

선거구의 인구는 선거구에 포함된 구역의 인구를 모두 합한 값이다.
'''

from collections import deque


def pop_cnt(popu, s):
    y, x, d1, d2 = s

    n_cnt = [0 for _ in range(5)]
    visited = [[False] * N for _ in range(N)]

    # 선거구 5 경계선
    for i in range(d1 + 1):
        n_cnt[4] += popu[y - i][x + i]
        n_cnt[4] += popu[y + d2 - i][x + d2 + i]

        popu[y - i][x + i] = popu[y + d2 - i][x + d2 + i] = 0
        visited[y - i][x + i] = visited[y + d2 - i][x + d2 + i] = True

    for j in range(d2 + 1):
        n_cnt[4] += popu[y + j][x + j]
        n_cnt[4] += popu[y - d1 + j][x + d1 + j]

        popu[y + j][x + j] = popu[y - d1 + j][x + d1 + j] = 0
        visited[y + j][x + j] = visited[y - d1 + j][x + d1 + j] = True

    # 선거구 5 내부
    que = deque([(y, x + 1),(y-d1+d2, x+d1+d2-1)])

    while que:
        r, c = que.popleft()

        n_cnt[4] += popu[r][c]
        popu[r][c] = 0
        visited[r][c] = True

        for d_i in range(4):
            nr, nc = r + dy[d_i], c + dx[d_i]

            if visited[nr][nc]:
                continue

            n_cnt[4] += popu[nr][nc]
            popu[nr][nc] = 0
            que.append((nr, nc))
            visited[nr][nc] = True

    '''if set_ == (4,2,2,1):
        print(set_)

        for X in visited:
            print(X)''' 각 구획별로 visited 변하는 거 손코딩 정답이랑 비교하며 풀이

    # 선거구 1
    for i in range(y):
        for j in range(x + d1+1):
            n_cnt[0] += popu[i][j]
            popu[i][j] = 0
            visited[i][j] = True

    # 선거구 2
    for i in range(y, N):
        for j in range(x + d2):
            n_cnt[1] += popu[i][j]
            popu[i][j] = 0
            visited[i][j] = True

    # 선거구 3
    for i in range(y - d1 + d2 + 1):
        for j in range(x + d1, N):
            n_cnt[2] += popu[i][j]
            popu[i][j] = 0
            visited[i][j] = True

    # 선거구 4
    for i in range(y - d1 + d2, N):
        for j in range(x + d2, N):
            n_cnt[3] += popu[i][j]
            popu[i][j] = 0
            visited[i][j] = True

    return n_cnt


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

sets = deque([])

for x in range(1, N - 1):  # 1~N-2
    for d1 in range(1, N - x):
        for d2 in range(1, N - x - d1):
            for y in range(1 + d1, N - d2 + 1):
                sets.append((y - 1, x - 1, d1, d2))

for set_ in sets:
    population = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            population[i][j] = POPULATION[i][j]

    cnt = pop_cnt(population, set_)

    output.append(max(cnt) - min(cnt))

print(min(output))
