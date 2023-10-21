import sys
input = sys.stdin.readline

def binarySearch(x):
   s, e = 1, x
   
   while 1:
       mid = (s+e) //2
       if ap(mid-1) < x <= ap(mid):
           return mid
       
       if ap(mid) < x:
           s = mid + 1
       else:
           e = mid - 1

def ap(x): # 등차수열 합공식
   return x * (2*a + (x -1) * d) // 2

Q = int(input())
for _ in range(Q):
   a, d, x = map(int, input().split())
   
   # 층 수 찾기
   layer = binarySearch(x)
   
   # layer 층의 블럭수
   block_count = (layer -1) * d + a

   # layer 층의 마지막 번호 : e
   e = ap(layer)

   # x 의 위치
   pos = block_count - (e - x)

   print(layer, pos)