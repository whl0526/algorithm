import sys
import heapq

input = sys.stdin.readline

n = int(input())
count = 1
time = [list(map(int, input().split())) for _ in range(n)]#[1,3] #[2,4]#[3,5]

time.sort(key=lambda x : x[0])

heap = [time[0][1]] #3

for i in range(1,n): #2차례
    if heap[0] <= time[i][0]: 
        heapq.heappop(heap)
        count -= 1
    heapq.heappush(heap,time[i][1])  
    count += 1
    
print(count)    

    

                   