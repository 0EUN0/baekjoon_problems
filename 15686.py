N,M = map(int, input().split()) # N:도시의 크기 M:최대 치킨집의 개수
city = [list(map(int, input().split())) for _ in range(N)] # N*N 도시의 정보

output = 10000000000000 # 도시 내 치킨 거리의 최소값

"""
도시의 각 칸은 빈칸, 치킨집, 집 중 하나 # 0(빈 칸) 1<=1(집)<2N M<=2(치킨집)<=13
도시의 칸은 (r,c)로 나타내고, r과 c는 1부터 시작한다.

치킨거리는 집과 가장 가까운 치킨 집 사이의 거리이다.
각각의 집은 치킨 거리를 가지고 있다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.

도시의 치킨 집 중 M개를 고르고 나머지는 모두 폐업 시켜야 한다. @
가장 작은 도시의 치킨 거리를 구하라. @
"""

chicken, house = [],[]

for i in range(N):
    for j in range(N):
        if city[i][j] == 1: house.append((i,j))
        elif city[i][j] == 2: chicken.append((i,j))

chicken_subset = []

def make_subset(subset, depth):
    if len(subset) == M:
        chicken_subset.append(list(subset))
        return
    elif depth == len(chicken):
        return

    subset.append(chicken[depth])
    make_subset(subset, depth+1)

    subset.pop()
    make_subset(subset, depth+1)

make_subset([], 0)

for sub in chicken_subset:
    total_chicken_distance = 0

    for h in house:
        chicken_distance = 1000000000000000

        for s in sub:
            n_distance = abs(h[0] - s[0]) + abs(h[1] - s[1])

            if chicken_distance > n_distance:
                chicken_distance = n_distance

        total_chicken_distance += chicken_distance

    if total_chicken_distance < output:
        output = total_chicken_distance

print(output)
