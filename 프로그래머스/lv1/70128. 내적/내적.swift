import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    var ans:Int = 0
    for index in 0..<a.count {
        ans += a[index] * b[index]
    }
    return ans
}