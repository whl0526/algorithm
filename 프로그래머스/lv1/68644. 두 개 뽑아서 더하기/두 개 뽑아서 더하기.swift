import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var resultArr = [Int]()
    
    print(numbers.sorted())
    for index in 0..<numbers.sorted().count {
        for index2 in index + 1..<numbers.sorted().count {
            
            if !resultArr.contains(numbers[index] + numbers[index2]){
                resultArr.append(numbers[index] + numbers[index2])
            }
        }
    }
    return resultArr.sorted()
}