N = int(input()) # N: 격자의 크기 | 홀수
SAND = [list(map(int, input().split())) for _ in range(N)] # 격자 각 칸에 있는 모래

output = 0 # 격자의 밖으로 나간 모래의 양

"""
* 가운데 칸에 있는 모래의 양은 0

동작 순서
(1) 격자의 가운데 칸부터 토네이도가 이동한다.
* 토네이도는 한 번에 한 칸 이동한다.

(2) 토네이도가 한 칸 이동할 때마다 모래는 주변 칸으로 일정한 비율로 흩날린다.

[0  0   2%  0   0]
[0  10% 7%  1%  0]
[5% a   y   x   0]
[0  10% 7%  1%  0]
[0  0   2%  0   0]

* 토네이도가 x에서 y로 이동할 때, 주변 칸으로 y 칸 모래의 *% 흩날림 (% 계산에서 소수점 아래는 버린다.)
* a로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다.
* 이동하는 모래는 기존 칸에 있던 모래에 더해진다.

* 다른 방향으로 이동하는 경우, 위 격자를 회전하면 된다.

(3) 토네이도는 격자의 가장 왼쪽 위로 이동한 뒤 소멸한다.
"""

direction, distance, move_count = 0, 1, 0
r = c = int(N//2) # 초기 토네이도 위치

def out_of_range(y,x):
    if 0 <= y < N and 0 <= x < N: return False
    else: return True

sand_process = [
    [(1,1,0.01),(-1,1,0.01),(-2,0,0.02),(2,0,0.02),(-1,-1,0.1),(1,-1,0.1),(-1,0,0.07),(1,0,0.07),(0,-2,0.05)],
    [(-1,1,0.01),(-1,-1,0.01),(0,2,0.02),(0,-2,0.02),(1,-1,0.1),(1,1,0.1),(0,-1,0.07),(0,1,0.07),(2,0,0.05)],
    [(-1,-1,0.01),(1,-1,0.01),(2,0,0.02),(-2,0,0.02),(1,1,0.1),(-1,1,0.1),(1,0,0.07),(-1,0,0.07),(0,2,0.05)],
    [(1,-1,0.01),(1,1,0.01),(0,-2,0.02),(0,2,0.02),(-1,1,0.1),(-1,-1,0.1),(0,1,0.07),(0,-1,0.07),(-2,0,0.05)]
]
direction 바뀔 때마다 Sand 이동하는 격자 모양이 바뀌는데 어떻게 표현해야 할지 몰라서 노가다로 다 적어줌 | 메모리 적게 잡아먹을 것 같긴 하지만 굉장히 바보 같은 방법인 것 같아서 자료 찾아봐야 겠다.
> 찾아보니까 다른 사람들도 이렇게 푼 듯 . . . . .

from math import trunc

def move():
    global direction, distance, move_count, r, c, sand_process, output, SAND

    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    move_count += 1

    for _ in range(distance):
        r, c = r + dy[direction], c + dx[direction]

        if out_of_range(r, c): return # 토네이도가 격자 벗어나면 끝

        alpha = SAND[r][c]
	
				# print(r,c, alpha)
				해당 print 문 통해서 토네이도가 제대로 된 경로로 이동하고 있는지, 
				그리고 손코딩 통해 얻은 현재 SAND[r][c] 값과 같은지 확인했다.

        for s_dy, s_dx, percentage in sand_process[direction]:
            nr, nc = r + s_dy, c + s_dx

            if out_of_range(nr,nc):
                output += int(trunc(SAND[r][c] * percentage))
                alpha -= int(trunc(SAND[r][c] * percentage))
            else:
                SAND[nr][nc] += int(trunc(SAND[r][c] * percentage))
                alpha -= int(trunc(SAND[r][c] * percentage))
						
						해당 부분에서 trunc(버림) 대신 round(반올림) 사용했을 때 결과 완전 달라짐.
						문제 그대로 코드 짜는 게 중요함. || 이해 제대로 하는 것도 !!


        if out_of_range(r + dy[direction], c + dx[direction]): output += alpha # alpha에 해당하는 위치 격자 확인
        else: SAND[r + dy[direction]][c + dx[direction]] += alpha

        SAND[r][c] = 0

    if move_count == 2: # direction 2번 바꾸면 distance 1 늘어나
        move_count = 0
        distance += 1

    direction = (direction + 1) % 4

    move()

move()

print(output)
