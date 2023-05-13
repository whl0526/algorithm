n,m = map(int,input().split())

a = set(list(map(int,input().split())))
b = set(list(map(int,input().split())))

differenceA_B = len(a-b)
differenceB_A = len(b-a)

print(differenceA_B + differenceB_A)