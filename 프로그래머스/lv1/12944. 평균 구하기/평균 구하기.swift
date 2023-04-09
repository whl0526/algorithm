func solution(_ arr:[Int]) -> Double {
    var sum: Double = 0.0
    
    for index in 0..<arr.count {
        sum += Double(arr[index])
    }
    
    
    return sum / Double(arr.count)
}