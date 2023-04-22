import Foundation

func solution(_ number:[Int]) -> Int {
    var answer = 0
    
    // 서로 다른 3가지 수 구하기 
    for i in 0..<number.count {
        for j in i+1..<number.count {
            for k in j+1..<number.count {
                if number[i] + number[j] + number[k] == 0 { answer += 1 }
            }
        }
    }
    
    return answer
}