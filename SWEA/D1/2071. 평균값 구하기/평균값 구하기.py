t = int(input())

for case in range(1, t+1):
    numbers = list(map(int, input().split()))
    avg_num = round(sum(numbers) / 10)
    print("#{} {}".format(case, avg_num))
