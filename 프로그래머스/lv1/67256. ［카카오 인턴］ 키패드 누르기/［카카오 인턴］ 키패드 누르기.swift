import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    
    var leftPosition = (3,0)
    var rightPosition = (3,2)
    
    let keypad: [Int:(Int,Int)] = [
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        0:(3,1)
    ]
    var result = ""
    
    for index in numbers {
        if index == 1 || index == 4 || index == 7 {
            leftPosition = keypad[index]!
            result += "L"
        }else if index == 3 || index == 6 || index == 9 {
            rightPosition = keypad[index]!
            result += "R"
        }else {
            let leftDistance = abs(keypad[index]!.0 - leftPosition.0) + abs(keypad[index]!.1 - leftPosition.1)
            let rightDistance = abs(keypad[index]!.0 - rightPosition.0) + abs(keypad[index]!.1 - rightPosition.1)
             if leftDistance > rightDistance { //오른쪽 손가락이 더 가까운 경우
                    result += "R"
                 rightPosition = keypad[index]!
             }else if rightDistance > leftDistance { //왼쪽 손가락이 더 가까운 경우
                 result += "L"
                 leftPosition = keypad[index]!
             }else {//거리가 같은 경우
                 if hand == "left"{
                    result += "L"
                    leftPosition = keypad[index]!
                 }else {
                     result += "R"
                     rightPosition = keypad[index]!
                 }
             }
        }
    }//for
    return result
}