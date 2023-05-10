list = sorted(map(int,input().split()))

print(list[0] + list[1] + min(list[2], (list[0]+list[1]-1) ))

