func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
  var result:[Int] = []
  // return 할 결과값을 저장할 변수 선언
  
  for number in arr {
  // 1) divisor로 나누어 떨어지는 경우 찾기
    if number % divisor == 0 {
      result.append(number)
    }
  }
  
  // 2) result에 아무런 값이 없을 경우 -1을 result에 저장하기
  if result.isEmpty {
    result.append(-1)
  }
  
  // 3) 오름차순으로 정렬
  return result.sorted()
}

// 나누어 떨어지는 숫자 배열