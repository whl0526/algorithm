func solution(_ num:Int) -> Int {
    var tempNum = num
    var count = 0
    
    while(tempNum > 1){
        if count == 500 {
            return -1
        }
        if tempNum % 2 == 0{
            tempNum = tempNum / 2
        } else {
            tempNum = tempNum * 3 + 1
        }
        count += 1
    }
    return count
}