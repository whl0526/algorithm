x,y = map(int,input().split())

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x,y):
    return x*y // gcd(x,y)

print(lcm(x,y))