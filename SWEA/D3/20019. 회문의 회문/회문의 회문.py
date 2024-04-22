def is_palindrome(s):
    return s == s[::-1]

def is_double_palindrome(s):
    n = len(s)
    if n < 3:  # 주어진 문자열이 3글자 미만이라면 회문의 회문일 수 없음
        return False
    
    if not is_palindrome(s):  # 주어진 문자열이 회문이 아니라면 회문의 회문일 수 없음
        return False
    
    # 회문이 맞는 경우, 앞쪽 절반과 뒤쪽 절반을 각각 확인하여 회문의 회문인지 판별
    front_half = s[:n//2]
    back_half = s[(n+1)//2:]
    
    return is_palindrome(front_half) and is_palindrome(back_half)

# 입력 및 결과 출력
T = int(input())  # 테스트 케이스의 수
for i in range(T):
    S = input()  # 문자열 입력
    if is_double_palindrome(S):
        print(f"#{i+1} YES")
    else:
        print(f"#{i+1} NO")
