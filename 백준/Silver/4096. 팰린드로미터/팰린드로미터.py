def is_palindrome(s: str) -> bool:
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


while True:
    s = input()
    if s == "0":
        break

    cnt = 0
    while not is_palindrome(s):
        length = len(s)
        int_s = int(s) + 1
        cnt += 1
        tmp_s = str(int_s)
        s = "0" * (length - len(tmp_s)) + tmp_s
    print(cnt)