n = int(input())#4
roads = list(map(int,input().split()))#2 3 1
costs = list(map(int,input().split()))#5 2 4 1

res = roads[0] * costs[0]# 2 * 5
m = costs[0]# 2
distance = 0 

for i in range(1,n-1): #1,2,3
    if costs[i] < m: #5 < 2 (5보다 큰 costs는 없다)
        res +=  m*distance #
        distance = roads[i] #
        m = costs[i]
    else:
        distance += roads[i]
    if i == n-2: # 1 == 2 , 2 == 2
        res += m * distance
print(res)        
        
    
