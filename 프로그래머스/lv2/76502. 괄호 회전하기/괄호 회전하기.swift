func checkBrace(_ s: [Character]) -> Bool {
    
    var stack = [Character]()
    var d = [Character:Character]()
    d[")"] = "("
    d["}"] = "{"
    d["]"] = "["
    
    var s = s
    stack.append(s.first!)
    for i in 1..<s.count {
        
        if d.values.contains(s[i]) { stack.append(s[i]) } 
        else if stack.count != 0 && stack.last! == d[s[i]] { stack.removeLast() }
        else { stack.append(s[i]) }
    }
    
    return stack.count == 0 ? true : false
    
    
}

func solution(_ s:String) -> Int {
    
    var s = s.map({ $0 })
    var answer = 0
    for i in 0..<s.count {
        var first = s.removeFirst()
        s.append(first)
        if checkBrace(s) { answer += 1 }
    }
    return answer
}