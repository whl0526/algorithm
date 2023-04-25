func solution(_ n:Int) -> Int {
    
    var result: Int = Int()
    
    if n > 0 {
        for i in 1...n {
            if n % i == 0 {
                result += i
            }
        }
        return result
    }
    return 0
}