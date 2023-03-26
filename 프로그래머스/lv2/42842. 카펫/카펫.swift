import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
   let sum = brown + yellow
   var bw = 0 
    var bh = 0
    
    for index in 1...sum {
        if sum % index == 0{
            bw = sum / index 
        bh = index 
        }
            if (bw - 2) * (bh - 2) == yellow {break}

    }
    
    
    return [bw, bh]
}