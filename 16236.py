**BFS**

현재 지점에서 visited = False(기준 필요)로 되어 있는 모든 칸을 가는 방법에 대해 알 수 있는 방법이다.

가장 가까운 지점부터 훑고 지나가기 때문에 최단 거리 측정에 효과적이다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c97d79b9-f452-42e5-8904-05346e9db059/Untitled.png)

from collections import deque

N = int(input())  # 공간의 크기
STATE = [list(map(int, input().split())) for _ in range(N)]  # 공간의 상태

output = 0  # 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
'''
STATE: 0 1 2 3 4 5 6 9 의 값
0: 빈 칸 1~6: 칸에 있는 물고기의 크기 9: 아기 상어의 위치
'''
'''
한 칸에는 물고기가 최대 1마리 존재 
가장 처음에 아기 상어의 크기는 2 

1) 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동
- 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다. 
- 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 
* 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다. 

2) 물고기를 먹는다.
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
* 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 
* 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.

>> 거리가 가장 가까운 물고기를 찾는 방법
	: BFS를 사용해 visited = False인 격자 공간 전체를 훑고, 
	  그 중 먹을 수 있는 물고기를 포함한 경로의 거리를 저장한다.

3) 물고기를 먹으면, 그 칸은 빈 칸이 된다.@
* 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 

4) 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
'''


def out_of_range(y, x):
    if 0 <= y < N and 0 <= x < N:
        return False
    else:
        return True


shark_size, shark_cnt = 2, 0

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

while True:
    destination = []
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if STATE[i][j] == 9:
                sr, sc = i, j
                visited[i][j] = True
            elif 1 <= STATE[i][j] < shark_size:
                destination.append((i, j))
            elif shark_size < STATE[i][j]:
                visited[i][j] = True

    #print(destination, visited)

    if not destination: break
		더 이상 먹을 수 있는 물고기 없으면 멈춤

    fist_que = deque([])
    fist_que.append((sr, sc))

    save = []
    distance = 0


    def bfs(que):
        global save, distance

        n_que = deque([])
        distance += 1
				distance를 더해주는 시점이 중요

        while que:
            r, c = que.popleft()

            for d_i in range(4):
                nr, nc = r + dy[d_i], c + dx[d_i]

                if out_of_range(nr, nc) or visited[nr][nc]: continue

                n_que.append((nr, nc))
                visited[nr][nc] = True

                if (nr, nc) in destination:
                    save.append((nr, nc, distance))

        #print(n_que)

        if n_que: bfs(n_que)
        else: return

    bfs(fist_que)
    #print(save)

    if save:
		1) save에 원소가 없다면 (현 위치에서 도달할 수 있는 물고기가 없다면) 동작을 멈춰야 한다.

        STATE[sr][sc] = 0

        S = sorted(save, key=lambda x: (x[2], x[0], x[1]))[0]

        #print(f'!!!! {S}')
				2) STATE 내의 상어 위치를 조절하고, 먹힌 물고기의 값을 적용해 주어야 한다.

        output += S[2]

        sr, sc = S[0], S[1]
        STATE[sr][sc] = 9

        shark_cnt += 1
        if shark_cnt == shark_size:
            shark_size += 1
            shark_cnt = 0

				#print(STATE)
				3) 물고기가 먹은 물고기 수가 현재 물고기 크기와 같다면 물고기의 크기는 1 증가한다.

        
    else:
        break

print(output)
