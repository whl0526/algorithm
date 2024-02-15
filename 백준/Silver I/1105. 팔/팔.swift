import Foundation

// 표준 입력을 받는 함수 정의
func readLineAsStringArray() -> [String] {
    return readLine()!.split(separator: " ").map(String.init)
}

// l과 r을 입력 받음
let input = readLineAsStringArray()
let l = input[0]
let r = input[1]

var cnt = 0
if l.count == r.count {
    for (i, j) in zip(l, r) {
        if i == "8" && j == "8" {
            cnt += 1
        } else if i != j {
            break
        }
    }
}
print(cnt)
