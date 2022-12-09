'''변수를 어떻게 저장해야 할 지만 결정하면 풀이는 기본적인, 쉬운 문제였다 :)'''

N = int(input()) # N: 보드의 크기
K = int(input()) # K: 사과의 개수
apple = [tuple(map(int,input().split())) for _ in range(K)]
APPLE = []
for y,x in apple: APPLE.append((y-1,x-1))
# APPLE: 사과의 위치 1 <= (y,x) <= N # 사용 시 y-1, x-1 해야함

L = int(input()) # L: 뱀의 방향 변환 횟수
ORDER = []
for _ in range(L):
    X, D = input().split()
    ORDER.append((int(X), D))
# ORDER: 뱀의 방향 변환 정보 (X,D)
# 게임 시작 시간으로부터 X초가 끝난 뒤에 C = 왼쪽(L) 또는 오른쪽(D)로 90도 방향을 회전시킨다.

output = 0 # 게임이 끝나는 시간 (초)

'''
게임이 시작할때 뱀은 *맨위 맨좌측에 위치하고 *뱀의 길이는 1 이다. *뱀은 처음에 오른쪽을 향한다.

뱀은 매 초마다 이동한다.
1) 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
2-1) 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
2-2) 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
   * 즉, 몸길이가 변하지 않는다.

** 종료 조건: 뱀이 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
'''


def OOR(r, c):
    if 0 <= r < N and 0 <= c < N: return False
    else: return True


from collections import deque

dy = [0,1,0,-1]
dx = [1,0,-1,0]

snake = deque([(0,0)])
snake_d = 0

while True:
    snake_r, snake_c = snake[-1]
    snake_nr, snake_nc = snake_r + dy[snake_d], snake_c + dx[snake_d]
    #print(snake_nr, snake_nc)

    if OOR(snake_nr, snake_nc) or (snake_nr, snake_nc) in snake: break

    snake.append((snake_nr, snake_nc))
    #print(snake)

    def find_apple(r, c):
        global APPLE

        for i, (apple_y, apple_x) in enumerate(APPLE):
            if (apple_y, apple_x) == (r, c):
                del APPLE[i]
                return True

        return False

    TF = find_apple(snake_nr, snake_nc)

    if not TF: snake.popleft()

    output += 1

    for X,C in ORDER:
        if output == X and C == 'L': snake_d = (snake_d + 3) % 4
        elif output == X and C == 'D': snake_d = (snake_d + 1) % 4

    #print(snake_d)

print(output+1)
마지막에 OOR or snake에 이미 존재하는지 확인하는 과정또한 시간에 포함되는 것이기 때문에 output += 1 해주어야 함
