import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var size = sizes
    var x:[Int] = []
    var y:[Int] = []
    
    for index in 0..<size.count {
        size[index].sort()
        x.append(size[index][0])
        y.append(size[index][1])


    }
    return x.max()! * y.max()!
}


