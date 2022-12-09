이게 뭘까 . . .

N = int(input())
STATE = list(map(int,input().split()))
B,C = map(int,input().split())

output = 0

'''
총감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 B명
부감독관은 한 시험장에서 감시할 수 있는 응시자의 수가 C명

각각의 시험장에 총감독관은 오직 1명만 있어야 하고, 부감독관은 여러 명 있어도 된다.

각 시험장마다 응시생들을 모두 감시해야 한다.

필요한 감독관 수의 최솟값을 구하라.
'''

for n in STATE:
    # print(n)

    now_cnt = 0

    n -= B
    now_cnt += 1

    if n > 0:
        if n % C == 0: now_cnt += (n//C)
        else: now_cnt += (n//C + 1)

    # print(now_cnt)
    output += now_cnt

print(output)
