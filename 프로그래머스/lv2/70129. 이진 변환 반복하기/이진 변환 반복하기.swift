import Foundation

func solution(_ s:String) -> [Int] {
    var rotation: Int = 0
    var zeroCnt: Int = 0
     var s = s 
    
    while s != "1" {
        let deleteZero = s.filter { $0 == "1"}
        zeroCnt += s.count - deleteZero.count
         s = String(deleteZero.count, radix: 2)
        rotation += 1
    }
    return [rotation, zeroCnt]
}