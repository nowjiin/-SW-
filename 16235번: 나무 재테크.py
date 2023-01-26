/*
부동산 투자로 억대의 돈을 번 상도는 최근 N×N 크기의 땅을 구매했다. 상도는 손쉬운 땅 관리를 위해 땅을 1×1 크기의 칸으로 나누어 놓았다. 각각의 칸은 (r, c)로 나타내며, r은 가장 위에서부터 떨어진 칸의 개수, c는 가장 왼쪽으로부터 떨어진 칸의 개수이다. r과 c는 1부터 시작한다.
상도는 전자통신공학과 출신답게 땅의 양분을 조사하는 로봇 S2D2를 만들었다. S2D2는 1×1 크기의 칸에 들어있는 양분을 조사해 상도에게 전송하고, 모든 칸에 대해서 조사를 한다. 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
매일 매일 넓은 땅을 보면서 뿌듯한 하루를 보내고 있던 어느 날 이런 생각이 들었다.

나무 재테크를 하자!

나무 재테크란 작은 묘목을 구매해 어느정도 키운 후 팔아서 수익을 얻는 재테크이다. 상도는 나무 재테크로 더 큰 돈을 벌기 위해 M개의 나무를 구매해 땅에 심었다. 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
이 나무는 사계절을 보내며, 아래와 같은 과정을 반복한다.
봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다. 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다. 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.
*/

"""
* 문제에서 제시된 N은 최대 10이므로, 최대 10 X 10 크기의 맵이 될 것이다.
* 문제에서 요구하는 내용을 그대로 구현해야 하는 [시뮬레이션 유형]의 문제다.
* 인접한 위치는 8개로 간주한다.
    1. (r-1, c-1)
    2. (r-1, c)
    3. (r-1, c+1)
    4. (r, c-1)
    5. (r, c+1)
    6. (r+1, c-1)
    7. (r+1, c)
    8. (r+1, c+1) 
"""

n, m, k = map(int, input().split())

# 현재 양분 정보로, 처음에는 5씩 들어있다.
energy = [[5] * n for _ in range(n)]
# 겨울에 각 위치에 추가할 양분 정보 입력
arr = []
for _ in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
# N X N 크기의 격자에 각각 나무(tree)를 리스트로 표현
trees = [[[] for j in range(n)] for i in range(n)]
for _ in range(m):
    # 각 나무의 (x, y) 좌표와 나이(age) 정보 입력
    x, y, age = map(int, input().split())
    # 배열의 인덱스는 0부터 출발하므로 1씩 빼서 넣기
    trees[x - 1][y - 1].append(age)

# 인접한 8가지 방향
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

# N X N 크기의 격자에 각각 죽은 나무(tree)를 리스트로 표현
died = [[[] for j in range(n)] for i in range(n)]


def spring(): # 봄일 때
    for i in range(n):
        for j in range(n):
            trees[i][j].sort()  # 오름차순 정렬
            # 해당 위치의 나무들의 나이를 하나씩 확인
            for k in range(len(trees[i][j])):
                # 양분이 충분하다면 나이만큼 양분 먹기
                if trees[i][j][k] <= energy[i][j]:
                    energy[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                # 양분이 부족하다면 나이 많은 나무들은 죽고, 반복문 탈출
                else:
                    for age in trees[i][j][k:]:
                        died[i][j].append(age)
                    trees[i][j] = trees[i][j][:k]
                    break


def summer():
    for i in range(n):
        for j in range(n):
            for age in died[i][j]:
                energy[i][j] += (age // 2)
            died[i][j] = []


def autumn():
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                # 나이가 5의 배수인 경우
                if age % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= n:
                            continue
                        trees[nx][ny].append(1)


def winter():
    for i in range(n):
        for j in range(n):
            energy[i][j] += arr[i][j]


for _ in range(k):
    spring()
    summer()
    autumn()
    winter()

result = 0
for i in range(n):
    for j in range(n):
        result += len(trees[i][j])
print(result)
