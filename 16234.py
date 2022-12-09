시간초과를 잡는 문제

N,L,R = map(int, input().split()) # N: 땅의 크기 (가로, 세로)
STATE = [list(map(int,input().split())) for _ in range(N)] # STATE: 각 나라의 인구수

output = 0

'''
인구 이동 방법
1) 인접한 국가의 인구 차이가 L 명 이상, R 명 이하라면 국경선을 연다.
2) 국경선이 열려 있어 인접한 칸만을 이용해 이동이 가능하면, 그 나라들을 연합이라고 한다.
3) 연합을 이루고 있는 나라의 인구수는 연합의 총 인구수 / 연합을 이루는 나라의 개수 이다. (소수점은 버린다)

** 종료 조건: 인구 이동이 없을 때까지
'''


def OOR(y, x):
    if 0 <= y < N and 0 <= x < N: return False
    else: return True


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(r, c):
    global comb, visited

    while que:
        r, c = que.pop()

        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]

            if OOR(nr, nc) or visited[nr][nc]: continue

            if L <= abs(STATE[r][c] - STATE[nr][nc]) <= R:
                que.append((nr, nc))
                save.append((nr, nc))

                visited[nr][nc] = True

            # print(que)


while True:
    visited = [[False] * N for _ in range(N)]
    comb = 0

    while True:
        for i in range(N):
            for j in range(N):
                if visited[i][j] is False:
                    que = [(i, j)]
                    save = [(i, j)]

                    visited[i][j] = True

                    bfs(i,j)
                    # print('save:', save)

                    total = 0
                    length = len(save)

                    for r, c in save:
                        total += STATE[r][c]

                    for r, c in save:
                        STATE[r][c] = total // length

                    comb += 1
        break

    if comb == N * N: break
		인구 이동이 없다

    output += 1

print(output)
