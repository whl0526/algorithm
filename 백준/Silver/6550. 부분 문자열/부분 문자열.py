def solution(s,t):
    value = 0
    for i in range(len(t)):
        if t[i] == s[value]:
            value += 1
            if value == len(s):
                return "Yes"
    return "No"
while True:
    try:
        s , t = input().split()
        answer = solution(s,t)
        print(answer)
    except:
        break
        