t = int(input())  # 테스트 케이스의 개수 입력

for case in range(1, t + 1):  # 각 테스트 케이스에 대해 반복
    n = int(input())  # 압축된 문서의 알파벳과 숫자 쌍의 개수 입력
    uncompressed = ''  # 원본 문서를 저장할 변수 초기화
    
    # 각 줄마다 알파벳과 숫자를 입력 받아서 압축을 푼다.
    for _ in range(n):
        alpha, num = input().split()  # 알파벳과 숫자 쌍을 입력 받음
        uncompressed += alpha * int(num)  # 알파벳을 숫자만큼 반복하여 원본 문서에 추가
    
    # 10글자씩 끊어서 출력
    print("#{}".format(case))  # 결과 출력
    for i in range(0, len(uncompressed), 10):
        print(uncompressed[i:i+10])  # 10글자씩 출력
