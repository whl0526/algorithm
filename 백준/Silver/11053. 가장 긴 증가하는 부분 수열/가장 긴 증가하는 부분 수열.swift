import Foundation

let n = Int(readLine()!)!
let a = readLine()!.split(separator: " ").map{Int(String($0))!}

var dp = Array(repeating: 1, count: n + 1)

for i in 1..<a.count {
    for j in 0..<i {
        if a[i] > a[j]{
            dp[i] = max(dp[i], dp[j] + 1)
        }
    }
}

print(dp.max()!)
