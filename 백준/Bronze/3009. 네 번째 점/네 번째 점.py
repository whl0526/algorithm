

x = []
y = []

for _ in range(3):
    xx,yy = map(int,input().split())
    x.append(xx)
    y.append(yy)
for i in range(3):
    if x.count(x[i]) == 1:
        x4 = x[i]
    if y.count(y[i]) == 1:
        y4 = y[i]
print(x4,y4)        