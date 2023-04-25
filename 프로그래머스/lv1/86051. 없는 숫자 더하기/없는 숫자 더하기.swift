import Foundation


func solution(_ numbers:[Int]) -> Int {
    (1...9).filter {
        !numbers.contains($0)
    }.reduce(0,+)
}