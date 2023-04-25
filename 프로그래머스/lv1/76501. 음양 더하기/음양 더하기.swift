
import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var sum = 0
    for i in 0 ..< absolutes.count {
        let sign = signs[i] == true ? 1 : -1
        sum += absolutes[i] * sign
    }
    return sum
}