t = int(input())  # 테스트 케이스 개수 입력

# 테스트 케이스 반복
for case in range(1, t+1):
    N = int(input())  # 거슬러 줄 금액 입력

    # 각 돈의 종류 리스트와 거슬러줄 돈의 개수를 저장할 리스트 초기화
    money_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_counts = []

    # 돈의 종류별로 거슬러줄 돈의 개수 계산
    for money in money_types:
        count = N // money  # 해당 종류의 돈으로 거슬러 줄 수 있는 최대 개수
        money_counts.append(count)  # 개수를 리스트에 추가
        N -= count * money  # 거슬러 줄 금액에서 거슬러 준 돈의 총 금액을 빼줌

    # 출력
    print("#{}".format(case))  # 테스트 케이스 번호 출력
    print(*money_counts)  # 돈의 종류별 개수 출력
