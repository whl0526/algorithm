import Foundation

let n = Int(readLine()!)!
var stairs = [0] // 0번 인덱스를 비워두고 시작

for _ in 1...n {
    stairs.append(Int(readLine()!)!)
}

var dp = [Int](repeating: 0, count: n + 1)

dp[1] = stairs[1]
if n >= 2 {
    dp[2] = stairs[1] + stairs[2]
}

if n >= 3 {
    for i in 3...n {
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])
    }
}

print(dp[n])
