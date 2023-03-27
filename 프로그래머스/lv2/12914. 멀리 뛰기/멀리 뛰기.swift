func solution(_ n:Int) -> Int {
  var a:Int = 1 
  var b:Int = 2
  var result: Int = 0
    
    if n < 4 {
      return n
  }
    for _ in 3...n{
        result = (a+b)%1234567
        a = b
        b = result 
    }
    return result 
    
}

