func solution(_ s:String) -> Bool {
    var bool: Bool = false
    if s.count == 4 || s.count == 6 {
        bool = (Int(s) == nil) ? false : true
    }
    return bool
}