이것도 역시 + - 단순히 문제 이해와 수학적 풀이에서 비롯되는 실수를 잡는 것이 생명인 문제라 느꼈다.
i+1 번째에서 i 번째 뺐으니까 j번째에 더해주는 건지 빼는 건지 도댇체가 머리가 어질어질했다. 그리고 졸려 죽겠다.

내일의 나 화잇팅 🥊

N = int(input()) # N: 드래곤 커브의 개수
CURVES = [list(map(int, input().split())) for _ in range(N)]
'''
각 줄에는 드래곤 커브의 정보가 주어진다.
드래곤 커브의 정보는 (x,y): 드래곤 커브의 시작점 d: 시작 방향 g: 세대 로 이루어져 있다.

방향은 0,1,2,3 = 우,상,좌,하
* 입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다.
* 드래곤 커브는 서로 겹칠 수 있다.
'''
output = 0 # 크기가 1*1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수

'''
0세대 커브
1세대 커브
2세대 커브
3세대 커브
...

K세대 커브는 K-1세대 커브를 끝 점을 기준으로 90도 회전시킨 다음, 그것을 끝 점에 붙인 것이다.
'''

dy = [0,-1,0,1]
dx = [1,0,-1,0]

LINES = [[False]*101 for _ in range(101)]
격자는 0 ≤ x,y ≤ 100 을 포함한다.
따라서 가로 세로 101칸이어야 한다. 

이것때문에 INDEXERROR 두 번 떠서 넘 화났다 . . . .

for x,y,d,g in CURVES:
    n_line = [(y, x),(y+dy[d], x+dx[d])] # 0세대 line 저장

    for _ in range(g):
        # 90도 돌리기
        after_90 = [(y, x)]
        for i in range(len(n_line)-1):
            dif_y, dif_x = (n_line[i+1][0] - n_line[i][0]), (n_line[i+1][1] - n_line[i][1])

            if d == 0 or d == 2:
                if i % 2 == 0: # 0,2,4,,,
                    after_90.append((after_90[i][0]+dif_x, after_90[i][1]+dif_y))
                else:
                    after_90.append((after_90[i][0]-dif_x, after_90[i][1]-dif_y))
            else:
                if i % 2 == 0:
                    after_90.append((after_90[i][0]-dif_x, after_90[i][1]-dif_y))
                else:
                    after_90.append((after_90[i][0]+dif_x, after_90[i][1]+dif_y))

        # 끝점 연결하기
        dif_y = n_line[-1][0] - after_90[-1][0]
        dif_x = n_line[-1][1] - after_90[-1][1]

        for i in range(1, len(after_90)):
            ny, nx = after_90[-1-i][0] + dif_y, after_90[-1-i][1] + dif_x

            n_line.append((ny,nx))

    #print(n_line)

    for n in n_line:
        LINES[n[0]][n[1]] = True

for i in range(100): # 세로
    for j in range(100): # 가로
        if LINES[i][j] and LINES[i+1][j] and LINES[i][j+1] and LINES[i+1][j+1]:
            output += 1

print(output)
