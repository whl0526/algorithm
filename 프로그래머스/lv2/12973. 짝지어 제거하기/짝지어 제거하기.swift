import Foundation

func solution(_ s:String) -> Int{

    var arr:[Character] = []
    
    for index in s {
        if !arr.isEmpty && arr.last! == index {
            arr.removeLast()
        }else {
            arr.append(index)
        }
    }
  

    return arr.isEmpty ? 1 : 0
}