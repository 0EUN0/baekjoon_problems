'''
1번부터 5번까지의 CCTV는 서로 다른 방향을 가지고 있다.

이를 90도 회전시켜 가질 수 있는 방법들도 서로 다르다.

이를 잘 조합해 사각지대를 최소화시키는 최적의 방법을 찾아야한다.

- **실행시키며 조합을 완성하는 방법 > 청소년 상어 문제 풀며 방법 고안**
- 다양한 조합을 완성시켜 놓고 하나씩 실행해 찾는 방법 > 생각하고, 구현하기 더 쉬우나 시간이 더 오래걸림
'''

############# python idea 01 ############
N,M = map(int,input().split()) # N: 세로 M: 가로
STATE = [list(map(int,input().split())) for _ in range(N)]
# 0: 빈칸 6: 벽 1~5: CCTV

'''
- 1번 CCTV는 한 쪽 방향만 감시할 수 있다. (상 하 좌 우)
2번과 3번은 두 방향을 감시할 수 있다.
- 2번은 감시하는 방향이 서로 반대방향, (상하 좌우)
- 3번은 직각 방향 (상우 우하 하좌 좌상)
- 4번은 세 방향 (상우하 우하좌 하좌상 좌상우)
- 5번은 네 방향을 감시할 수 있다. (상하좌우)

* CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다.
* CCTV는 벽을 통과할 수 없다.
* CCTV는 CCTV를 통과할 수 있다.
'''

output = 10**5 # 사각지대의 최소 크기

'''
CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 한다.
'''
from collections import deque
from copy import deepcopy

cctvs, walls = deque([]), []

for i in range(N):
    for j in range(M):
        if 1 <= STATE[i][j] <= 5: cctvs.append((STATE[i][j], i, j))
        elif STATE[i][j] == 6: walls.append((i,j))


# 0: 상 1: 우 2: 하 3: 좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]


def find_ways(index):
    if index == 1:
        return [[0],[1],[2],[3]]
    elif index == 2:
        return [(0,2),(1,3)]
    elif index == 3:
        return [(0,1),(1,2),(2,3),(3,0)]
    elif index == 4:
        return [(0,1,2),(1,2,3),(2,3,0),(3,0,1)]
    elif index == 5:
        return [(0,1,2,3)]


def cnt_hidden(arr):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] is False and STATE[i][j] == 0: cnt += 1

    return cnt


def OOR(y, x):
    if 0 <= y < N and 0 <= x < M: return False
    else: return True


def dfs(check, cctv):
    global output

    if cctv:
        n_cc = cctv.popleft()
    else:
        now_cnt = cnt_hidden(check)

        # for X in check: print(X)
        # print(now_cnt)

        if now_cnt < output:
            output = now_cnt
        return

    cc_index = n_cc[0] # cctv 번호 1~5 사이 값
    cc_ways = find_ways(cc_index)

    for way in cc_ways:
        now_check = deepcopy(check) # check 보관 now_check에 변화 줌

        for w in way:
            cc_r, cc_c = n_cc[1:]
						CCTV의 위치는 고정된 상태에서 상하좌우로 체크하는 위치만 변화해야한다.

            while True:
                nr, nc = cc_r + dy[w], cc_c + dx[w]

                if OOR(nr,nc) or ((nr,nc) in walls): break

                cc_r, cc_c = nr,nc
                now_check[cc_r][cc_c] = True

        '''
				print('now')
        for X in now_check: print(X)
        print('check')
        for X in check: print(X)
				'''

        dfs(deepcopy(now_check), deepcopy(cctv))


checked = [[False]*M for _ in range(N)]
dfs(deepcopy(checked), deepcopy(cctvs))

print(output)

############# python idea 02 ############
'''2: [(1,1)(3,4)] 

(1,1,0)(3,4,0)
(1,1,0)(3,4,1)
(1,1,1)(3,4,0)
(1,1,1)(3,4,1)

2: (1,1)
  checked (1,1,0)

  (1,1) 없다 생각하고 남은 cctv listup
  2: (3,4)
    checked (3,4,0)
    뒤에 더 없음 > checked False check output                   update

    checked (3,4,1)

  checked (1,1,1)

  2: (3,4)
      checked (3,4,0)
      checked (3,4,1)
'''

list = [(1,1,2,0), (1,1,2,1), (3,4,2,0), (3,4,2,1)]
comb = []

def dfs(que, depth):
  if len(que) == 2:
    print(que)
    comb.append(que)
    return
  elif depth == len(list):
    return

  check = False
  for r,c,index,i in que:
    if (list[depth][0], list[depth][1]) == (r,c):
      check = True
      break

  if not check:
    que.append((list[depth]))
    dfs(que, depth + 1)
  else:
    dfs(que, depth + 1)
  
  if que: que.pop()
  dfs(que, depth+1)
  
dfs([],0)

print(comb)
