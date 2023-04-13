import Foundation

func solution(_ N:Int, _ road:[[Int]], _ K:Int) -> Int {
    var graph = [[Int]](repeating: [Int](repeating: 987654321, count: N + 1), count: N + 1)
    
    for i in 1...N {
        graph[i][i] = 0
    }
    
    for r in road {
        let a = r[0], b = r[1], c = r[2]
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
    }
    
    for k in 1...N {
        for i in 1...N {
            for j in 1...N {
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            }
        }
    }
    
    var count = 0
    for i in 1...N {
        if graph[1][i] <= K {
            count += 1
        }
    }
    
    return count
}
