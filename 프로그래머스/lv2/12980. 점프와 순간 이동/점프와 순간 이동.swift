import Foundation

func solution(_ n:Int) -> Int 
{
    var jumpCnt:Int = 0
    var N = n
    
    while N > 0 {
        jumpCnt += N % 2 
        N /= 2
    }

    return jumpCnt
}
