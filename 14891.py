처음으로 약 1시간 만에 풀었던 문제
쉬웠어서 그랬을 지도 모르지만 , , , 중간에 실수가 없었다면 1시간 내로 끊었을 지도 모른다 !!!!!!!
실수 없는 코딩 해보자 보자 보자 !! 해 낸다 낸다 낸다 !!!!!!!!!!!!!

from collections import deque

STATE = [deque(input()) for _ in range(4)]
# 1~4번 톱니바퀴의 상태 (0: N극 1: S극)
# 상태는 8자리로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다.

rotate_num = int(input()) # 회전 횟수
rotate_way = [map(int,input().split()) for _ in range(rotate_num)] # 회전 방법
# 방법은 두 개의 정수로 이루어져 있다. [회전시킨 톱니바퀴의 번호, 방향] 방향 1: 시계 -1: 반시계

output = 0 # 4개의 톱니바퀴의 점수의 합 | N번 톱니 12시 방향이 S극 + 2*(2^N-1)

'''
톱니바퀴는 일렬로 놓여져 있다.

톱니바퀴가 회전할 때 서로 맞닿은 극에 따라서 옆(양쪽)에 있는 톱니를 회전시킬 수도 아닐 수도 있다.
- 서로 맞닿은 톱니의 극이 다르면, B는 A의 회전 방향과 반대 방향으로 회전한다.
'''

def check_right(r_n, r_d):
    global RIGHT
    if r_n == 3: return

    if STATE[r_n][-1] != STATE[r_n + 1][3]:  # 옆의 것도 반대 방향으로 돌아가야 함
        RIGHT.append((r_n + 1,r_d * -1))
        check_right(r_n + 1, r_d * -1)  # 그 옆에 것도 체크해야 함
    else:
        return

def check_left(r_n, r_d):
    global LEFT
    if r_n == 0: return

    if STATE[r_n][3] != STATE[r_n - 1][-1]:  # 옆의 것도 반대 방향으로 돌아가야 함
        LEFT.append((r_n - 1,r_d * -1))
        check_left(r_n - 1, r_d * -1)  # 그 옆에 것도 체크해야 함
    else:
        return

for _ in range(3):
    for i in range(4):
        STATE[i].rotate(-1)

for R_N, R_D in rotate_way:
    R_N -= 1

    RIGHT, LEFT = [],[]
    check_right(R_N, R_D)
    check_left(R_N, R_D)

		분명히 테스트 케이스는 다 맞는데 0%도 안 올라가고 틀렸다고 나왔었다.
		
		돌아가는 행동은 과정 중간 중간이 아니라 돌아가야 한다는 확신이 생긴 후 한 번에 이루어져야 한다. 
		(그렇지 않으면 이전의 회전이 이후 톱니의 회전에 영향을 주기 때문에)
		
		문제를 풀기 전 문제 자체에 대한 꼼꼼한 이해가 필수적이다.

    STATE[R_N].rotate(R_D)

    for n,d in RIGHT: STATE[n].rotate(d)
    for n,d in LEFT: STATE[n].rotate(d)

# 점수 확인
for i, X in enumerate(STATE):
    if STATE[i][-3] == '1': output += 2*(2**(i-1))

print(int(output))
