func solution(_ s:String) -> String {
    let splitedString = s.split(separator: " ")
    var numArr:[Int] = []
    
    for index in splitedString {
        guard let number = Int(index) else { return " "}
        numArr.append(number)
    }
    return "\(numArr.min()!) \(numArr.max()!)"
}