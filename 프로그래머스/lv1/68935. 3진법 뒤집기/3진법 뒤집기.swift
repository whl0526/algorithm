import Foundation

func solution(_ n:Int) -> Int {
    let str1 = String(n, radix: 3)
    var str2 = ""
    for index in str1.reversed() {
        str2 += String(index)
    }

    return Int(str2, radix: 3)!
}