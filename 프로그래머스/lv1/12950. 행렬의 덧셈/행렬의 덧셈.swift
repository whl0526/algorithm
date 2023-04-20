func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    var sum = arr1
    
    for index in 0..<arr1.count {
        for index2 in 0..<arr1[index].count {
            sum[index][index2] += arr2[index][index2]
        }
    }
    return sum
}