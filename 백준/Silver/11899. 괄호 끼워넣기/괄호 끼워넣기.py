s = input().rstrip()
l = len(s)
while True:
    s = s.replace("()","")
    l -= 1 # '()'이 더 이상 없더라도 반복문이 돌 때마다 l은 1씩 줄어든다.
    if l == 0:
        print(len(s)) # 짝이 안 맞는 괄호 개수 출력하고 반복문 종료
        break