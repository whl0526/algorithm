func solution(_ n:Int) -> Int {
    var fibo:[Int]  = [0 , 1]
    
    for index in 2...n {
        fibo.append((fibo[index-2] + fibo[index-1]) % 1234567)
    }
    print(n)
    return fibo[n]
}