func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {

    var answer = 0
    
    // 더 받는 콜라 갯수를 answer에 저장하고 현재 콜라 갯수를 다시 함수에 넘겨
    // 재귀를 사용하여 해결
    func numCola (_ z:Int) -> Int {
        // 더 받는 콜라 갯수
        answer += b * (z/a)
        // 지금 콜라 갯수
        var cola = b * (z/a) + z % a
        if cola < a {
            return answer
        } else {
            return numCola(cola)
        }
    }
    return numCola(n)
}