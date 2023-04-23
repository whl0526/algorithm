func solution(_ strings:[String], _ n:Int) -> [String] {

    return strings.sorted { first, second in
        if first[first.index(first.startIndex, offsetBy: n)] != second[second.index(second.startIndex, offsetBy: n)] {
            return first[first.index(first.startIndex, offsetBy: n)] < second[second.index(second.startIndex, offsetBy: n)]
        }
        return first < second
    }
}