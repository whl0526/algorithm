#문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.

import sys

while True:
    s = sys.stdin.readline().rstrip('\n')

    if not s:
        break
    
    small, capital, num, space = 0, 0, 0, 0

    for i in range(len(s)):

        if s[i].islower():
            small += 1

        elif s[i].isupper():
            capital += 1
        
        elif s[i].isdigit():
            num += 1

        else:
            space += 1

    print(small, capital, num, space)