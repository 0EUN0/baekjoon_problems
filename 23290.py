전체적으로 복잡한 형태의 문제 !!!

1) 문제의 이해가 가장 중요하다.
**2) 문제 풀이 방식 정립**
- **input, output을 확인한다.**
- **전체적인 문제의 흐름을 확인한다.**
- **각 순서에서 필요한 변수의 형태를 확인한다. (적합한)**
- **순서에 맞춰 코드를 작성한다.**
- **에러가 발생한 경우, 모든 스텝 뒤에 결과를 확인할 수 있는 print문을 붙인다.**
- **손코딩 결과와 print 결과를 확인하며 알맞게 작성된 코드까지 표시하고, 뒷 부분을 차례로 수정해나간다.**

from collections import deque

M, S = map(int, input().split())  # M:물고기의 수 S:상어가 마법을 연습한 횟수
FISH = [(map(int, input().split())) for _ in range(M)]
# (fx, fy, d) 물고기의 정보 * M
# (fx,fy): 물고기의 위치 d: 방향 (8자리 이하의 자연수이며, 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙)

sx, sy = map(int, input().split())  # (sx, sy) 상어의 위치

output = 0  # S번의 연습 마친 후 격자에 있는 물고기의 수

"""
격자는 4*4 크기이며, 가장 왼쪽 칸은 (1,1) 가장 오른쪽 아랫 칸은 (4,4) @
둘 이상의 물고기가 같은 칸에 있을 수 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다. @
"""

"""
상어의 마법연습 동작 순서 * S번 반복 @
1) 상어가 복제 마법을 실시하나, 5번에서 결과가 나타난다. @

2) 모든 물고기가 한 칸 이동한다. 이동할 수 있을 때까지 방향을 반시계 45도 회전하고, 이동한다. @
* 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다. @
* 이동할 수 있는 칸이 없으면 이동하지 않는다. @

3) 상어가 상하좌우 중 연속해서 3칸 이동한다. @
* 이동하는 중 물고기가 있는 칸으로 이동하면 물고기는 제거되고, 물고기 냄새를 남긴다. @
* 가능한 이동 방법 중 물고기 수가 가장 많은 방법으로 이동하고, @
* 가장 많이 제거하는 방법이 여러 개면, 사전 순으로 가장 앞서는 방법을 이용한다. @

* 사전 순: 상(1) 좌(2) 하(3) 우(4) 상하좌: 132 하우하: 343 따라서 상하좌가 앞서는 방법 @

4) 두 번 전 연습에서 생긴 물고기 냄새가 사라진다. @

5) 1번에서 실시한 복제 마법의 결과가 나타난다. @
"""

fish_d = {}
for fr, fc, d in FISH: # 물고기 위치 저장
    if (fr-1, fc-1) in fish_d.keys(): fish_d[(fr-1, fc-1)].append(d-1)
    else: fish_d[(fr-1, fc-1)] = [d-1]
처음에도 한 칸에 여러 개가 들어갈 수 있다는 사실을 간과하였다.

sr, sc = sx - 1, sy - 1  # 상어 위치 저장

fish_smell = {}  # 물고기 냄새 저장 key는 위치, value는 3 2 1 0 의 값

def out_of_range(check_y, check_x):
    if 0 <= check_y < 4 and 0 <= check_x < 4: return False  # 격자 내에 있다.
    else: return True

###############################################################

shark_possible_que = deque([])
li = [0, 1, 2, 3]
visited = [False for _ in range(4)]

def make_list(now):
        if len(now) == 3:
            shark_possible_que.append(list(now))
            return

        for i, value in enumerate(li):
            now.append(value)
            visited[i] = True
            make_list(now)

            now.pop()
            visited[i] = False

make_list(deque())

###############################################################

def move_fish():
    for i in range(8):
        nd = ((d - i) + 8) % 8
물고기의 방향은 반시계로 회전한다.

        nr, nc = r + fish_dy[nd], c + fish_dx[nd]

        if out_of_range(nr, nc):
            continue

        if (nr, nc) != (sr, sc) and (nr, nc) not in fish_smell.keys():
            if (nr, nc) in new_fish_d.keys(): new_fish_d[(nr, nc)].append(nd)
            else: new_fish_d[(nr, nc)] = [nd]

            return

    if (r, c) in new_fish_d.keys(): new_fish_d[(r, c)].append(d)
    else: new_fish_d[(r, c)] = [d]

    return

def move_shark(n_r, n_c):
    now_fish = 0
    now_copy_fish_d = new_fish_d.copy()

    for loc in now_way:
        nr, nc = n_r + shark_dy[loc], n_c + shark_dx[loc]

        if out_of_range(nr, nc):
            return -1
						return 0로 할 때는, outofrange로 인한 0와 실제 이동하였는데 0가 나온 경우를 구분할 수 없다. 
					따라서 모두 0이 나오면 무조건 상상상으로 이동하게 된다.

        n_r, n_c = nr, nc
        if (n_r, n_c) in now_copy_fish_d.keys():
            now_fish += len(now_copy_fish_d[(n_r, n_c)])
            now_copy_fish_d.pop((n_r, n_c), None)
						상어는 같은 곳으로 돌아올 수 있다. 
						이 때 물고기를 지워놓지 않으면 똑같은 물고기를 또 지우는 상황이 발생한다.

    return now_fish

###############################################################

fish_dy = [0, -1, -1, -1, 0, 1, 1, 1]  # 0부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ * 반시계 방향이라 음수를 더해줘야함
fish_dx = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_dy = [-1, 0, 1, 0]  # 상(1) 좌(2) 하(3) 우(4)
shark_dx = [0, -1, 0, 1]

for _ in range(S):
    ### (1)
    copy_fish_d = fish_d.copy()

    ### (2)
    new_fish_d = {}
    que = deque(fish_d.keys())

    while que:
        r, c = que.popleft()
        d_arr = deque(fish_d[(r, c)])

        while d_arr:
            d = d_arr.popleft()

            move_fish()

    ### (3)
    max_fish_n = 0
    max_way = [8,8,8]

    copy_shark_possible_que = shark_possible_que.copy()

    while copy_shark_possible_que:
        now_way = copy_shark_possible_que.popleft()
        r, c = sr, sc

        now_fish_n = move_shark(r, c)

        if now_fish_n > max_fish_n:
            max_fish_n = now_fish_n
            max_way = now_way

        elif now_fish_n == max_fish_n:
            m = (max_way[0] + 1) * 100 + (max_way[1] + 1) * 10 + (max_way[2] + 1) * 1
            n = (now_way[0] + 1) * 100 + (now_way[1] + 1) * 10 + (now_way[2] + 1) * 1

            if m > n:  # n이 사전순으로 앞서는 것
                max_way = now_way

    for x in max_way:
        sr, sc = sr + shark_dy[x], sc + shark_dx[x]

        if (sr, sc) in new_fish_d.keys():
            new_fish_d.pop((sr, sc), None)
            fish_smell[(sr, sc)] = 3
						해당 횟차에 무조건 1번 - 되기 때문에 2가 아닌 3으로 지정해주었다.

    ### (4)
    copy_fish_smell = fish_smell.copy()

    for key in fish_smell.keys():
        copy_fish_smell[key] -= 1

        if copy_fish_smell[key] == 0: copy_fish_smell.pop(key, None)

    fish_smell = copy_fish_smell

    ### (5)
    for key in copy_fish_d.keys():
        for val in copy_fish_d[key]: 
				for val in copy_fish_d.values()로 했을 때,
				val 은 list 형태가 되므로 append 하였을 때 다른 원소들과(int형) 다른 형태를 가진다.

            if key in new_fish_d.keys():
                new_fish_d[key].append(val)
            else:
                new_fish_d[key] = [val]

    fish_d = new_fish_d

for key in fish_d.keys():
    output += len(fish_d[key])

print(output)
