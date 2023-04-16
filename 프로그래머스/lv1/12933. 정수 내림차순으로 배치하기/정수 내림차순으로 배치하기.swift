func solution(_ n:Int64) -> Int64 {
    let reversed = String(n).sorted(by: >).reduce("") {String($0) + String($1)}
    return Int64(reversed)!
}