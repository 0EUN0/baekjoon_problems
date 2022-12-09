N, M = map(int, input().split())  # N: 격자 한 변의 크기 M: 색상의 개수
Blocks = [list(map(int, input().split())) for _ in range(N)]  # Blocks: 블로 정보 저장 (-1,0,M이하의 자연수)로 이루어짐

output = 0  # 점수의 합

'''
정보
1) 초기 격자 내 모든 칸에 블록 하나씩 있다.
2) 블록은 검은색 블록(-1), 무지개 블록(0), 일반 블록(M 이하의 자연수 = 색상)이 있다.
3) 인접한 칸은 (r,c) 기준으로 네 방향의 칸을 의미한다.

4) 블록 그룹은 연결된 블록의 집합이며, 블록의 수는 2개 이상으로 구성되어야 한다. @
5) 그룹에는 일반 블록이 적어도 하나 있어야 하고 @ , 일반 블록의 색(값)은 모두 같아야 한다. @
6) 그룹에는 검은색 블록(-1)은 포함되지 않아야 하고 @, 무지개 블록(0)은 포함 가능하다. @
7) 그룹 내의 모든 블록은 하나로 연결가능해야 한다. (인접한 칸들로 이루어져야 함) @

8) 그룹 내의 기준 블록은 무지개 블록이 아닌 블록 중, 행, 열의 번호가 가장 작은 블록이다. @
'''
'''
동작 순서
1) 크기가 가장 큰 블록 그룹을 찾는다. @
    - 크기가 같으면, 무지개 블록 수가 가장 많은 그룹 @
    - 무지개 수가 같으면, 기준 블록의 행이 가장 큰 그룹 @
    - 행도 같으면, 열이 가장 큰 그룹 @
2) 블록 그룹 내의 블록을 모두 제거하고 @ output += 제거된 블록의 수 ** 2 @
3) 격자에 중력 작용
    - 검은색 블록을 제외한 모든 블록이 @ 행의 번호가 큰 칸으로 이동 @ (다른 블록 @ or 끝을 만나기 전까지 @)
4) 격자를 90도 반시계 방향으로 회전 @
5) 격자에 중력 재 작용 @
'''

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

from collections import deque

while True:
    General_blocks = deque([])
    for i in range(N):
        for j in range(N):
            if Blocks[i][j] >= 1:
                General_blocks.append((i, j))

    Group = []
    Rainbow = 0
    R, C = 0, 0

    while True:
        if len(General_blocks) == 0:
            break

        start_r, start_c = General_blocks.popleft()

        n_Group = [(start_r, start_c)]
        n_Rainbow = 0
        nR, nC = start_r, start_c

        que = deque([(start_r, start_c)])
        visited = [[False for _ in range(N)] for _ in range(N)]
        visited[start_r][start_c] = True

        while True:
            if len(que) == 0:
                break

            r, c = que.popleft()

            for d in range(4):
                nr, nc = r + dy[d], c + dx[d]

                if (0 <= nr <= (N - 1)) and (0 <= nc <= (N - 1)):
                    if (visited[nr][nc] is False) and (Blocks[nr][nc] in [Blocks[start_r][start_c], 0]):
                        visited[nr][nc] = True

                        que.append((nr, nc))
                        n_Group.append((nr, nc))

                        if Blocks[nr][nc] == 0:
                            n_Rainbow += 1
                        else:
                            if nr < nR:
                                nR, nC = nr, nc
                            elif nr == nR and nc < nC:
                                nR, nC = nr, nc

                        if General_blocks.count((nr, nc)) >= 1:
                            General_blocks.remove((nr, nc))

        if len(n_Group) > len(Group):
            Group, Rainbow, R, C = n_Group, n_Rainbow, nR, nC
        elif len(n_Group) == len(Group):
            if n_Rainbow > Rainbow:
                Group, Rainbow, R, C = n_Group, n_Rainbow, nR, nC
            elif n_Rainbow == Rainbow:
                if nR > R:
                    Group, Rainbow, R, C = n_Group, n_Rainbow, nR, nC
                elif nR == R:
                    if nC > C:
                        Group, Rainbow, R, C = n_Group, n_Rainbow, nR, nC

    if len(Group) < 2: break  # 종료 조건

    for y,x in Group: Blocks[y][x] = -1000
    output += (len(Group) ** 2)

    for i in range(2, N + 1):  # N-2 ~ 0
        for j in range(N):
            if (Blocks[N - i][j] >= 0) and (Blocks[N - i + 1][j] == -1000):
                num = 1

                while True:
                    if (N - 1 < N - i + num) or (Blocks[N - i + num][j] != -1000):
                        break
                    else:
                        num += 1

                Blocks[N - i + num - 1][j] = Blocks[N - i][j]
                Blocks[N - i][j] = -1000

    new = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new[(N - 1) - j][i] = Blocks[i][j]
    Blocks = new

    for i in range(2, N + 1):  # N-2 ~ 0
        for j in range(N):
            if (Blocks[N - i][j] >= 0) and (Blocks[N - i + 1][j] == -1000):
                num = 1

                while True:
                    if (N - 1 < N - i + num) or (Blocks[N - i + num][j] != -1000):
                        break
                    else:
                        num += 1

                Blocks[N - i + num - 1][j] = Blocks[N - i][j]
                Blocks[N - i][j] = -1000

print(output)




- 손으로 정리하는 것보다 코드 위에 주석처리해두고 해결할 때마다 해결 표시하는 것이 효율적
- 작동 단계 지날 때마다 출력, 테스트 케이스랑 비교해서 제대로 작동하는 지 확인하고 다음으로 넘어가기
- 사소한 실수 하지 않기 | 못 풀 이유가 없다.
