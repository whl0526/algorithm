import Foundation

func resultCalculator(dot1: Int, dot2: Int, dot3: Int, dot4: Int, arr: [[Int]]) -> Int {
    var line1x = arr[dot1][0] - arr[dot2][0]
    var line1y = arr[dot1][1] - arr[dot2][1]
    var line2x = arr[dot3][0] - arr[dot4][0]
    var line2y = arr[dot3][1] - arr[dot4][1]
    if Double(line1y) / Double(line1x) == Double(line2y) / Double(line2x) {
        return 1
    }
    return 0
}
func solution(_ dots:[[Int]]) -> Int {
    guard resultCalculator(dot1: 0, dot2: 1, dot3: 2, dot4: 3, arr: dots) == 0 else { return 1 }
    guard resultCalculator(dot1: 0, dot2: 2, dot3: 1, dot4: 3, arr: dots) == 0 else { return 1 }
    guard resultCalculator(dot1: 0, dot2: 3, dot3: 1, dot4: 2, arr: dots) == 0 else { return 1 }
    return 0
}