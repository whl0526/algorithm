import Foundation

func solution(_ A:[Int], _ B:[Int]) -> Int
{
    var sum  = 0
    var arr1 = A.sorted()
    var arr2 = B.sorted()
    
    for _ in 0..<A.count {
        sum += arr1.removeFirst() * arr2.removeLast()
    }



    return sum
}