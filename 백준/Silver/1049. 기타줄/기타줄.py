# 1 패키지는 6줄

# 남은 줄의 갯수가 6보다 크다면 낱개가격*6 중 가장작은것과 패키지가격중 가장작은 것을 비교해 더 작은것을 리턴하고 남은줄-6
# 남은 줄의 갯수가 6보다 작다면 낱개가격*남은줄개수 중 가장작은것과 패키지가격을 비교해서 더 작은것을 리턴

n, m = map(int, input().split())
package = []
single = []

for _ in range(m):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

min_package = min(package)

ans = 0
while n > 0:
    if n >= 6:
        min_single = min(single)*6
        n -= 6
    else:
        min_single = min(single)*n
        n -= n
    if min_single < min_package:
        ans += min_single
    else:
        ans += min_package

print(ans)