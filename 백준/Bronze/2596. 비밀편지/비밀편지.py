alpha = {
    "000000" : "A",
    "001111" : "B",
    "010011" : "C",
    "011100" : "D",
    "100110" : "E",
    "101001" : "F",
    "110101" : "G",
    "111010" : "H"
}
length = int(input())
secret = input()
answer = ""
for i in range(length):
    parse = secret[6*i: 6*(i+1)]
    if alpha.get(parse):
        answer += alpha[parse]
    else:
        tmp = ""
        for a in alpha.keys():
            check = bin((int(a,2)^int(parse,2)))
            if check.count("1") == 1:
                tmp = alpha[a]
        if tmp :
            answer += tmp
        else:
            print(i+1)
            break
if len(answer) == length:
    print(answer)
                
            
            
            
