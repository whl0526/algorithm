import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var ans = 0
    for index in left...right {
        var count = 0
        for index2 in 1...index {
            if index % index2 == 0 {
                count += 1
            }
        }
        if count % 2 == 0{
            ans += index
        }else {
            ans -= index
        }

    }
    return ans
}