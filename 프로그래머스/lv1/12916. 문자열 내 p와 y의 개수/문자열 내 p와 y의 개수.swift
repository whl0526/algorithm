import Foundation

func solution(_ s:String) -> Bool
{
    var result = 0
    let pletter = Array("pP")
    let yletter = Array("yY")
    for c in s {
        if pletter.contains(c){
            result += 1
        }
        else if yletter.contains(c) {
            result -= 1
        }
    }
    return result == 0 ? true : false
}