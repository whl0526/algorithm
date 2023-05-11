N = int(input())

def digit_sum(n):
    #각 자리수의 합 계산하는 함수 ex:216
    sum = 0
    while n > 0:
        sum += n % 10 #2+1+6 = 9
        n //= 10 
    return sum

result = 0

for i in range(1,N):
    if i + digit_sum(i) == N:
        result = i
        break
print(result)
        
    


        