func solution(_ n:Int, _ m:Int) -> [Int] {
    let g = gcd(n, m)
    let l = lcm(n, m)
    
    return [g, l]
}

func gcd(_ a: Int, _ b: Int) -> Int {
  let r = a % b
    
  if r != 0 {
    return gcd(b, r)
  } else {
    return b
  }
}

func lcm(_ a: Int, _ b: Int) -> Int {
  let r = a * b / gcd(a, b)

  return r
}