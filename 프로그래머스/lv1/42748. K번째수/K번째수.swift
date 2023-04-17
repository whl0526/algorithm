import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var ans = [Int]()
    for index in commands {
        let a = index[0]
        let b = index[1]
        let ab = array[a-1...b-1].sorted()
        //print(ab)
        ans.append(ab[index[2]-1])
        print(ans)
    }
    return ans
}