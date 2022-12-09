실수 한 번 하면 30분 금방 날라가니깐 처음부터 제대로 읽자 . . .

from collections import deque
from math import trunc

R,C,T = map(int, input().split()) # R: 방의 세로 C: 방의 세로 T: 진행 시간
STATE = [list(map(int, input().split())) for _ in range(R)]
# 방의 상태 -1: 공기청정기가 설치된 곳(두 칸을 차지) 나머지 값: 미세먼지의 양

output = 0 # T초가 지난 후 방에 남아 있는 미세먼지의 양

'''
* 공기청정기는 1열의 두 칸을 차지하며 움직이지 않는다.

1. 모든 칸의 미세먼지가 네 방향으로 확산된다.
   * 인접한 방향에 공기청정기가 있으면 or 방을 벗어나면 확산이 일어나지 않는다.
   - 확산되는 양은 현재 칸의 / 5이고, 소수점은 버린다.
   - 현재 칸에 남은 양은 (기존 양 - 확산된 양)이다.

2. 공기청정기에서 바람이 나온다.
   공기청정기의 위쪽 바람은 반시계 방향으로 순환
   공기청정기의 아래쪽 바람은 시계 방향으로 순환
   바람의 방향을 따라 미세먼지가 한 칸씩 이동한다.
   ** 공기청정기로 들어간 미세먼지는 모두 정화된다.
   ** 미세먼지가 공기청정기로 인해 밖으로 나가는 것은 아니다.
'''

# 공기청정기 위치 저장
cleaner = []
for r in range(R):
    if STATE[r][0] == -1: cleaner.append((r,0))

def OOR(y,x):
    if 0 <= y < R and 0 <= x < C: return False
    else: return True

dy = [-1,0,1,0]
dx = [0,-1,0,1]

for _ in range(T):
    # 미세먼지 확산 단계
    new_state = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if STATE[i][j] <= 0: continue

            VAL = STATE[i][j]
            val = trunc(VAL/5)
						
						new_state에 넣을 때마다 VAL / 5해서 넣어서 한 번 틀렸다.
						> 이렇게 할 경우 VAL의 값이 계속 작아져서 5보다 작아질 경우 값이 측정되지 않는다.
						따라서 미리 계산해두고 격자 내에 있을 때만 정해진 값을 VAL에서 빼도록 해야한다.

            for d in range(4):
                nr,nc = i + dy[d], j + dx[d]

                if OOR(nr,nc) or (nr,nc) in cleaner: continue

                new_state[nr][nc] += val
                VAL -= val

            new_state[i][j] += VAL

    STATE = new_state

    #for X in STATE:print(X)
    #print()

    # 공기청정기 청소 단계
    def upper_n_lower_side(start,Q):
        global STATE

        cleaner_r, cleaner_c = start

        if Q == 0:
            wind_dy = [0, -1, 0, 1]
            wind_dx = [1, 0, -1, 0]
        else:
            wind_dy = [0, 1, 0, -1]
            wind_dx = [1, 0, -1, 0]

        wind_d = 0
        wind_r, wind_c = cleaner_r + wind_dy[wind_d], cleaner_c + wind_dx[wind_d]
        save = deque([(STATE[wind_r][wind_c])])

        STATE[wind_r][wind_c] = 0

        while True:
            wind_nr, wind_nc = wind_r + wind_dy[wind_d], wind_c + wind_dx[wind_d]
						OOR이 아니라고 확신할 수 있을 때까지 wind_r을 대체하면 안된다.

            if (wind_nr, wind_nc) == (cleaner_r, cleaner_c): break

            if OOR(wind_nr, wind_nc):
                wind_d += 1
                wind_nr, wind_nc = wind_r + wind_dy[wind_d], wind_c + wind_dx[wind_d]

            wind_r, wind_c = wind_nr, wind_nc

            save.append((STATE[wind_r][wind_c])) # 지금 위치 값 저장
            STATE[wind_r][wind_c] = save.popleft() # 지금 위치 값 전 위치 값으로 변경

    upper_n_lower_side(cleaner[0], 0)
    upper_n_lower_side(cleaner[1], 1)

    #for X in STATE:print(X)

for i in range(R):
    for j in range(C):
        if STATE[i][j] > 0: output += STATE[i][j]

print(output)
