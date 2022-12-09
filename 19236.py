state = [list(map(int,input().split())) for _ in range(4)] 
# 물고기의 정보 ai(물고기 번호), bi(방향) 가 한 줄에 4개씩
# 물고기 번호는 1부터 16까지 존재
# 방향은 1부터 8까지 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 의미

output = 0 # 상어가 먹을 수 있는 물고기 번호의 최대

'''
상어의 초기 위치는 (0,0)이다.

0) 상어가 존재하는 칸의 물고기를 먹는다.
상어가 물고기를 먹으면, 상어의 방향은 해당 물고기의 방향과 같아진다.

1) 물고기가 이동한다.
** 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전한다.
** 물고기는 한 칸만을 이동한다.
이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸
이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸

물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

이동할 수 있는 칸이 없으면 이동을 하지 않는다. 

2) 상어가 이동한다.
** 상어는 현재 방향에 있는 칸으로 이동한다.
** 상어는 한 번에 여러 개의 칸을 이동할 수 있다.

상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.

물고기가 없는 칸으로는 이동할 수 없으며 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 
'''

def OOR(y,x):
  if 0 <= y < 4 and 0 <= x < 4: return False
  else: return True

STATE = [[0]*4 for _ in range(4)]
for i in range(4):
  for j in range(4):
    STATE[i][j] = ((state[i][2*j], state[i][2*j+1]-1))
    # STATE[i][j] = (물고기 번호, 방향)

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

def find_fish(n_state,index):
  for i in range(4):
    for j in range(4):
      if n_state[i][j][0] == index:
        return (i,j)
  
  return

def dfs(n_state,sr,sc,now_count): # 상어 위치, 현재 먹은 물고기 번호의 합
  global output
  
  eat_num = n_state[sr][sc][0] # 상어 현재 위치 물고기 번호 plus
  sd = n_state[sr][sc][1] # 상어 방향 변경
  
  n_state[sr][sc] = (0,0) # 상어가 먹은 위치 물고기 삭제

  #for X in n_state: print(X)
  #print()
  
  # 물고기 이동
  for fish in range(1,17):
    fish_index = find_fish(n_state, fish)
  
    if fish_index:
      fr, fc = fish_index
      fd = n_state[fr][fc][1]
      
      for d in range(8):
        nd = (fd + d) % 8
        nr, nc = fr + dy[nd], fc + dx[nd]
  
        if OOR(nr,nc) or (nr,nc) == (sr,sc): continue
        
        change_fish, change_d = n_state[nr][nc]
        n_state[nr][nc] = (fish, nd)
        n_state[fr][fc] = (change_fish, change_d)
  
        break

  #for X in n_state: print(X)
  #print()
    
  # 상어 이동 가능 좌표 찾기
  possible_route = []
  
  while True:
    sr, sc = sr + dy[sd], sc + dx[sd]
    
    if OOR(sr,sc): break
  
    if n_state[sr][sc] != (0,0):
      possible_route.append((sr,sc))

  if now_count + eat_num > output: output = now_count + eat_num

  #print(now_count, eat_num, now_count + eat_num)
  
  for y,x in possible_route:
    # 이동해서 먹고 방향 바꾸고
    # 물고기 이동
    # 상어 이동
  
    copy_state = [[0]*4 for _ in range(4)]
    for i in range(4):
      for j in range(4):
        copy_state[i][j] = n_state[i][j]
          
    dfs(copy_state,y,x,now_count + eat_num)

copy_state = [[0]*4 for _ in range(4)]
for i in range(4):
  for j in range(4):
    copy_state[i][j] = STATE[i][j]

'''for X in copy_state: print(X)
print()'''

dfs(copy_state,0,0,0)

print(output)
