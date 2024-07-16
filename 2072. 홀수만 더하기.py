T = int(input())
answer = []
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    sum = 0
    for i in num:
        if i%2 != 0 :
               sum += i
    answer.append(sum)
    print(f"#{test_case} {answer[test_case-1]}")
