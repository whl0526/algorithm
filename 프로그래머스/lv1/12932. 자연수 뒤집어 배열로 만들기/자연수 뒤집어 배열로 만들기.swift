func solution(_ n:Int64) -> [Int] {
	let arr = String(n).compactMap { Int(String($0)) }
	return arr.reversed()
}
