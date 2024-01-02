def longest_common_substring(A, B):
    len_A, len_B = len(A), len(B)
    dp = [0] * (len_B + 1)
    max_length = 0

    for i in range(1, len_A + 1):
        prev = 0
        for j in range(1, len_B + 1):
            temp = dp[j]
            if A[i-1] == B[j-1]:
                dp[j] = prev + 1
                max_length = max(max_length, dp[j])
            else:
                dp[j] = 0
            prev = temp

    return max_length

# 예시 사용
A = input().strip()
B = input().strip()
print(longest_common_substring(A, B))
