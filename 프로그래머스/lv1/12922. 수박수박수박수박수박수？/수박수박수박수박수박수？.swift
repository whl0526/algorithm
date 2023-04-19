func solution(_ n:Int) -> String {
    var ans = ""
    
    for index in 0..<n {
         if index % 2 == 0 {
        ans += "수"
    }else{
        //홀수
        ans += "박"
    }
    }
    return ans
}