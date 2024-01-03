##CCW 알고리즘 
##x1 x2 x3 x4
##y1 y2 y3 y4
##(x1y2 + x2y3 + x3y4) - (x2y1 + x3y2 + x4y3)

box = []
for _ in range(3):
    box.append(list(map(int,input().split())))

def ccw(p1,p2,p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1]))

ans = ccw(box[0],box[1],box[2])

if ans > 0:
    print(1)
elif ans == 0:
    print(0)
else:
    print(-1)