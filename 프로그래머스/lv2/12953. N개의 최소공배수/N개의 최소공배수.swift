
    //최소공배수 = n1 * n2 / gcd
    // gcd 구하기 
    //최소공배수 구하기
    // 유클리디안 호제법으로 최대공약수 구하기
func gcd(_ a:Int, _ b:Int) -> Int {
    let r = a % b 
    if r != 0 {
        return gcd(b,r)
    }else { //나머지가 0인경우 그게 최대공약수임
        return b 
    }
}
//gcd를 구하면 최소공배수

func lcm(_ a:Int,_ b:Int) -> Int {
    let r = (a * b) / gcd(a,b)
    return r
}

func solution(_ arr:[Int]) -> Int {
     return arr.reduce(1) { lcm($0, $1) }
    
}