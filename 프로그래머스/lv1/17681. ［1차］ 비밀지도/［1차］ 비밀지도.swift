func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    
    var answer: [String] = []
    var radixArr1: [String] = []
    var radixArr2: [String] = []
    
    for index in 0..<arr1.count {
        var zero = ""
        radixArr1.append(String(arr1[index],radix: 2 ))
        
        if radixArr1[index].count != n {
            //n - radixArr1.count 만큼 앞에 "0"을 추가해준다.
            for _ in 1...n - radixArr1[index].count {
                zero += "0"
            }
            zero += radixArr1[index]
            radixArr1.removeLast()
            radixArr1.append(zero)
        }
        
    }
    
    
    for index2 in 0..<arr2.count {
         var zero = ""

        radixArr2.append(String(arr2[index2],radix: 2 ))
        if radixArr2[index2].count != n {
            //n - radixArr2.count 만큼 앞에 "0"을 추가해준다.
            for _ in 1...n - radixArr2[index2].count {
                zero += "0"
            }
            zero += radixArr2[index2]
            radixArr2.removeLast()
            radixArr2.append(zero)
        }
        
    }
    
    for index3 in 0..<radixArr1.count {
        var compare = ""

        var mapArr1 = radixArr1[index3].map{
            String($0)
        }
        var mapArr2 = radixArr2[index3].map{
            String($0)
        }
        
        
        for index4 in 0..<mapArr1.count {
            if mapArr1[index4] == "1" || mapArr2[index4] == "1" {
                compare += "#"
            }else {        
                compare += " "
            }
        }
         answer.append(compare)
    }
    
    
    
    
    return answer
}
