# 다리를 지을 수 있는 경우의 수를 계산하는 함수
def count_bridge_cases(N, M):
    # 동쪽과 서쪽에 있는 사이트의 개수에 따라 경우의 수를 계산
    # 다리를 지을 수 있는 경우의 수는 서쪽 사이트 개수(N)와 동쪽 사이트 개수(M)의 조합인 조합(combination)의 개수와 동일
    # 이때, 조합(combination)은 조합식 nCr로 표현되며, nCr = n! / (r! * (n-r)!)로 계산됨
    # 여기서 n은 동쪽 사이트 개수(M), r은 서쪽 사이트 개수(N)를 의미

    # 팩토리얼 계산 함수
    def factorial(num):
        if num > 1:
            return num * factorial(num - 1)
        return 1

    # 다리를 지을 수 있는 경우의 수 계산
    bridge_cases = factorial(M) // (factorial(N) * factorial(M - N))
    return bridge_cases


# 테스트 케이스의 개수 입력
T = int(input())

# 각 테스트 케이스에 대해 다리를 지을 수 있는 경우의 수 출력
for _ in range(T):
    N, M = map(int, input().split())
    bridge_cases = count_bridge_cases(N, M)
    print(bridge_cases)