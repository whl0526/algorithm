n = int(input())
cnt = 0
nSix = 666

while 1:
    if '666' in str(nSix):
        cnt += 1
    if cnt == n:
        print(nSix)
        break
    nSix += 1