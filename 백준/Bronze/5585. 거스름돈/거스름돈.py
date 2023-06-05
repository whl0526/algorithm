amount = int(input())

change = 1000 - amount #잔돈계산
coins = [500,100,50,10,5,1] #잔돈 종류
count = 0

for coin in coins:
    count += change // coin
    change %= coin
    
print(count)    