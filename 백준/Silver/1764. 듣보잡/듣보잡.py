n,m = map(int,input().split())
h = set([str(input()) for _ in range(n)])
l = set([str(input()) for _ in range(m)])

result = sorted(list(h & l))
print(len(result))
for i in result:
    print(i)







    
    