**범위가 많이 나오는 문제는 범위 지정 실수를 최대한 줄여야 시간을 절약할 수 있다.**

한 번 틀리면 정신 오락가락 해서 어디 틀렸는지도 모르니까 조심하기

from tabnanny import check


N, L = map(int, input().split()) # N: 가로 세로의 크기 L: 경사로의 길이
STATE = [list(map(int, input().split())) for _ in range(N)] # 각 칸의 높이

output = 0 # 지나갈 수 있는 길의 개수 # 길: 한 행 또는 한 열 전부 (끝에서 끝으로 지나가는 것) N*N 격자 내에 길은 2N개

'''
길을 지나갈 수 있으려면 길에 속한 모든 칸의 높이가 같아야 한다.

또는 경사로를 놓아서 지나갈 수 있는 길을 만들 수 있다. 
경사로의 높이는 1, 길이는 L이고 무한대로 사용가능하다.

- 낮은 칸과 높은 칸의 높이 차이는 1이어야 한다.
- 경사로는 낮은 칸에 놓으며, 
- 경사로를 놓을 낮은 칸의 높이는 모두 같아야 하고, 
- L개의 칸이 연속되어 있어야 한다.

- 경사로를 놓은 곳에 또 경사로를 놓을 수 없다.
'''

def OOR(val):
    if 0 <= val < N: return False
    else: return True

def check_possible(check_arr):
    visited = [False]*N

    for x in range(N-1):
        if check_arr[x] - check_arr[x+1] == 1:
            haveto = check_arr[x+1]

            for y in range(1,L+1):
                if OOR(x+y): return False

                if (check_arr[x+y] == haveto) and (visited[x+y] is False): continue
                else: return False           

            for y in range(1, L+1):
                visited[x+y] = True

        elif check_arr[x] - check_arr[x+1] == -1:
            haveto = check_arr[x]

            for y in range(0, L):
                if OOR(x-y): return False

                if (check_arr[x-y] == haveto) and (visited[x-y] is False): continue
                else: return False           

            for y in range(0, L):
                visited[x-y] = True

        elif check_arr[x] - check_arr[x+1] == 0:
            continue

        else:
            return False    
    
    # print(check_arr, visited) 손코딩 정답이랑 비교해서 코드 확인
    return True

for i in range(N):
    # print(i)

    ARR = [STATE[j][i] for j in range(N)]
    okay = check_possible(ARR)
    if okay: output += 1


    ARR = STATE[i][:]
    okay = check_possible(ARR)
    if okay: output += 1

print(output)
