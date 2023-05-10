while 1:
    a,b,c = map(int,input().split())
    
    if a == b == c == 0:
        break
    list = [a,b,c]
    if sum(list) - max(list) <= max(list):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")