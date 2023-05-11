N,M = map(int,input().split())
# 5 21
cards = list(map(int,input().split())) 
#5 6 7 8 9

result = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k] 
            if total <= M and total > result:
                result = total
print(result)                
        
    

