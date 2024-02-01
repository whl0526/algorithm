import sys
import heapq

input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key=lambda x : x[0])

heap = [time[0][1]]

for i in range(1,n):
    if heap[0] <= time[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,time[i][1])        
    
print(len(heap))    

    

                   