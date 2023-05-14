a, b = map(int, input().split())  # 첫 번째 분수의 분자와 분모
c, d = map(int, input().split())  # 두 번째 분수의 분자와 분모

# 분자와 분모의 합
numerator = a * d + b * c
denominator = b * d

# 최대공약수 계산
def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

g = gcd(numerator, denominator)

# 기약분수로 출력
print(numerator // g, denominator // g)
