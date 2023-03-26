import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
    var round = 0
    var A = a
    var B = b
    
    while true {
        if A % 2 == 0{
            A /= 2
        }else {
            A = (A+1) / 2
        }
        
        if B % 2 == 0 {
            B /= 2
        }else {
            B = (B+1) / 2
        }
        round += 1
        if A == B {break}
    }
    

    return round
}