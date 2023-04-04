import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    //유저별 신고당한 횟수 [신고당한사람: 횟수]
    //user: 유저별 신고한 사람 [신고자: [신고당한사람]]
    var reported: [String: Int] = [:]
    var user: [String:[String]] = [:] 
    
    for index in Set(report) {
        let splited = index.split(separator: " ").map{String($0)}
      //  print(splited)
        user[splited[0]] = (user[splited[0]] ?? []) + [splited[1]]
       // print(user)
        reported[splited[1]] = (reported[splited[1]] ?? 0) + 1 
        //print(reported)
        
    }
    
    
    
    return id_list.map { id in 
                        return (user[id] ?? []).reduce(0){
                            $0 + ((reported[$1] ?? 0 )  >= k ? 1 : 0)
                        }
                    
                       }
}