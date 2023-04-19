func solution(_ s:String) -> String {
    var ans = ""
    if s.count % 2 == 0 {
        print(s.count)
        print("짝수")
        print(s[s.index(s.startIndex, offsetBy:s.count/2-1)...s.index(s.startIndex, offsetBy:s.count/2)])
        let even = s[s.index(s.startIndex, offsetBy:s.count/2-1)...s.index(s.startIndex, offsetBy:s.count/2)]
        ans.append(String(even))
    }else {
        print("홀수")
        print(s[s.index(s.startIndex, offsetBy:s.count/2)])
        let odd = s[s.index(s.startIndex, offsetBy:s.count/2)]
        ans.append(String(odd))
    }
    return ans
}