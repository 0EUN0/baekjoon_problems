단계가 적어 쉬운 문제

N = int(input()) # N: 수의 개수
NUMBER = list(map(int,input().split())) # N개의 수
plus, minus, multi, divide = map(int,input().split()) # + - * / 의 갯수 (합치면 N-1)

max_out, min_out = (10**10)*(-1), (10**10)

'''
수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다.
* 주어진 수의 순서를 바꾸면 안 된다.

* 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.

* 나눗셈은 정수 나눗셈으로 몫만 취한다.
* 음수를 양수로 나눌 때는, 양수로 바꾼 뒤 몫을 취하고 그 몫을 음수로 바꾼 것과 같다.
'''

# 연산자의 순서를 정한다.
OPERATIONS = ['+']*plus + ['-']*minus + ['*']*multi + ['/']*divide

PERM = []
visited = [False]*len(OPERATIONS)

def dfs(que):
    if len(que) == len(OPERATIONS):
        string = ''
        for s in que:string += s

        PERM.append(string)
        return

    for i, val in enumerate(OPERATIONS):
        if visited[i]: continue

        que.append(val)
        visited[i] = True
        dfs(que)

        que.pop()
        visited[i] = False

dfs([])
PERM = list(set(PERM))
python 내장 함수 set 인자로 [[]] list list는 사용 불가하다. 따라서 list안에 들어가는 원소들은 str으로 구성했다.

# 앞에서부터 순차적으로 계산 한다. (연산자가 /일 경우를 유의)
for operation in PERM:
    operation = list(operation)

    n_out = NUMBER[0]

    for i in range(len(NUMBER)-1):
        n_str = str(n_out)

        if operation[i] != '/': 
						몫만 구하기 위해 ‘//’으로 표현해버리면, 
						/ / 각각 하나의 문자로 인식하여 오류가 나타나므로 
						하나의 문자 ‘/’로 표현해두고 따로 계산해주는 것이 효율적이다.

            n_str += operation[i]
            n_str += str(NUMBER[i+1])

            n_out = eval(n_str)
        else:
            if int(n_str) < 0:
                n_out = (int(n_str)*(-1) // NUMBER[i+1])*(-1)
            elif int(n_str) >= 0:
                n_out = int(n_str) // NUMBER[i + 1]

    if n_out > max_out: max_out = n_out
    if n_out < min_out: min_out = n_out

print(max_out)
print(min_out)
