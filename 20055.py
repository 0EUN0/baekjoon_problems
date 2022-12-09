
from collections import deque

N, K = map(int, input().split())
inner = deque(list(map(int, input().split())))
robot = deque([False for _ in range(N)])

X = 0


def down():
    if robot[N - 1]: robot[N - 1] = False


while True:
    # step 1
    inner.rotate(1)
    robot.rotate(1)
    down()

    # step 2 # 해당 부분 Count 안 써서 시간초과 오류 있었음 !! + Pypi로 제출
    if robot.count(True) > 0:
        for i in range(0, N - 1):
            if robot[N - 2 - i] is True and (robot[N - 2 - i + 1] is False and inner[N - 2 - i + 1] >= 1):
                robot[N - 2 - i + 1] = True
                inner[N - 2 - i + 1] -= 1

                robot[N - 2 - i] = False

                down()

    # step 3
    if inner[0] >= 1 and robot[0] is False:
        robot[0] = True
        inner[0] -= 1

    # step 4
    X += 1

    if inner.count(0) >= K:
        print(X)
        break
