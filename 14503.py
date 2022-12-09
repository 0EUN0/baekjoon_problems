N, M = map(int, input().split())
r, c, d = map(int, input().split())
if d == 1 or d == 3: d = (d + 2) % 4  # 1 > 3, 3 > 1                           
# 진짜 미친놈이 . . . d == 1 or 3이라고 적어놔서 두 시간 버렸다. (예제 2번 답 54로 나옴) 왜냠 모든 기준 d가 +=2 해서 나왔기 때문 . . .
																																								
# input 먼저 확인하기
room = [list(map(int, input().split())) for _ in range(N)]
clean = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if room[i][j] == 1: clean[i][j] = True

from collections import deque
que = deque([(r, c)])  # 시작 점 지정

output = 0

# 위 왼 아래 오
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def for_(d_, r_, c_):
    for m in range(1, 5):
        nd = (d_ + m) % 4
        nr, nc = r_ + dy[nd], c_ + dx[nd]

        if clean[nr][nc] is False:
            que.append((nr, nc))

            return nd # return으로 해야 완벽 벗어나기
        else:
            if m == 4:
                if room[r_ + dy[(nd + 2) % 4]][c_ + dx[(nd + 2) % 4]] == 0:
                    que.append((r_ + dy[(nd + 2) % 4], c_ + dx[(nd + 2) % 4]))

                    return nd
                else:
                    return


while que:  # que 비어 있으면 끝 | 종료조건 정하기
    r, c = que.popleft()

    if clean[r][c] is False:
        output = output + 1
        clean[r][c] = output

    d = for_(d, r, c)

print(output)
