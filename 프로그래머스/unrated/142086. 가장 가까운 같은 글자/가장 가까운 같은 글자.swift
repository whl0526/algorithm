import Foundation

func solution(_ s:String) -> [Int] {
    var dic = [String:Int]()
    var answer = [Int]()
    
    for (a,i) in s.enumerated() {

        if dic[String(i)] != nil {
            answer.append(a - dic[String(i)]!)
            dic[String(i)] = a
        }else {
            answer.append(-1)
            dic[String(i)] = a
        }
    }
    return answer
}