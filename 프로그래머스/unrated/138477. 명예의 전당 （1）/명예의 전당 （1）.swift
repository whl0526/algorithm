import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var points = score
    var glory = [Int]()
    var result = [Int]()
    for i in 0..<points.count {
        if glory.isEmpty {
            glory.append(points[i])
            result.append(points[i])
            continue
        }
        if glory.count < k {
            glory.append(points[i])
            result.append(glory.min()!)
        } else if glory.count >= k {
            var point = points[i]
            if glory.filter{ $0 < point}.count > 0 {
                var min = glory.min()!
                for j in 0..<glory.count {
                    if glory[j] == min {
                        glory[j] = point
                        break
                    }
                }
                result.append(glory.min()!)
            } else {
                result.append(glory.min()!)
            }
        }
    }
    return result
}