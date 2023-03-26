import Foundation

func solution(_ s:String) -> Bool
{
    var ans: Bool = true
    var cnt: Int = 0
    
    for index in s {
        if index == "(" {
            cnt += 1
        }else if cnt <= 0 && index == ")"{
            ans = false 
            break
        }else { //")" 인경우
            cnt -= 1
        }
    }
    


    return ans && cnt == 0 
}