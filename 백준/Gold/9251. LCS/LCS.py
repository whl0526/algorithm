def LCS_length(str1, str2):
    m = len(str1)
    n = len(str2)

    # LCS를 구하기 위한 DP 테이블 생성
    dp = [[0] * (n+1) for _ in range(m+1)]

    # LCS 길이 계산
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# 입력 처리
str1 = input()  # 첫 번째 문자열 입력
str2 = input()  # 두 번째 문자열 입력

# LCS의 길이 계산 및 출력
lcs_length = LCS_length(str1, str2)
print(lcs_length)