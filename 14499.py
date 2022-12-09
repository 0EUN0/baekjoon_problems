주사위의 변환 과정을 이해했다면 쉽게 풀 수 있는 문제

N, M, y, x, k = map(int, input().split())
# N: 지도의 세로 크기 M: 가로 크기 (x,y): 주사위 초기 위치 k: 명령의 개수
적절한 값이 입력되었을 경우에만 y,x에 그 값을 대입해주어야 한다.

STATE = [list(map(int, input().split())) for _ in range(N)]
# 지도에 쓰여 있는 수 | 주사위가 있는 칸은 항상 0
ORDER = list(map(int, input().split()))
# 이동하는 명령 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4

'''
이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다.

* 바깥으로 이동시키려고 하는 경우에는 명령을 무시해야 하며, 출력도 하면 안 된다.

* 초기 주사위는 지도 위에 윗면이 1이고, 동쪽을 바라보는 방향이 3인 상태로 놓여져 있다.

1) 주사위를 굴린다.
2) 주사위를 굴렸을 때, 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다.
   0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
'''


def OOR(r, c):
    if 0 <= r < N and 0 <= c < M: return False
    else: return True


dice = {}
for i in range(6): dice[i + 1] = 0


def dice_change(direction):
    global dice

    new_dice = {}

    if direction == 1:
        X = [4, 2, 1, 6, 5, 3]
    elif direction == 2:
        X = [3, 2, 6, 1, 5, 4]
    elif direction == 3:
        X = [5, 1, 3, 4, 6, 2]
    else:
        X = [2, 6, 3, 4, 1, 5]

    for j in range(6): new_dice[j + 1] = dice[X[j]]

    dice = new_dice


dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

for order in ORDER:
    ny, nx = y + dy[order - 1], x + dx[order - 1]
		적절한 값이 입력되었을 경우에만 y,x에 그 값을 대입해주어야 한다.

    if OOR(ny, nx): continue

    y, x = ny, nx
    #print(order, y, x)

    dice_change(order)

    if STATE[y][x] == 0:
        STATE[y][x] = dice[6]
    else:
        dice[6] = STATE[y][x]
        STATE[y][x] = 0

    print(dice[1])
