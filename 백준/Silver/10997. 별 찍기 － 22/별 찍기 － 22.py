def expand_space(star_output: list) -> list:
    """주어진 규칙에 맞게 2차원 리스트를 확장합니다."""
    # 가로축의 공간을 확장합니다.
    for x in range(len(star_output)):
        star_output[x].insert(0, " ")
        star_output[x].insert(0, "*")
        star_output[x].append(" ")
        star_output[x].append("*")
    # 세로축의 공간을 확장합니다.
    star_output.insert(0, ["*"] + [" "] * (len(star_output[0]) - 1))
    star_output.insert(0, ["*"] * len(star_output[0]))
    star_output.append(["*"] + [" "] * (len(star_output[0]) - 2) + ["*"])
    star_output.append(["*"] * len(star_output[0]))
    return star_output


def print_star(x: int) -> list:
    """규칙에 맞추어 x에 해당하는 2중 리스트를 리턴합니다."""
    # 2-1. N이 1 또는 2일때는 정해진 포맷의 별을 리턴합니다.
    if x == 1:
        return [["*"]]
    elif x == 2:
        return [
            ["*", "*", "*", "*", "*"],
            ["*", " ", " ", " ", " "],
            ["*", " ", "*", "*", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", "*", " ", "*"],
            ["*", " ", " ", " ", "*"],
            ["*", "*", "*", "*", "*"],
        ]
    # 2-2. N >= 3일 경우, print_star를 재귀적으로 호출합니다.
    # print_star(N - 1)을 호출하여 N - 1일때의 출력을 호출합니다.
    prev_star_output: list = print_star(x - 1)
    # N - 1일 때의 출력에 위아래 2, 양 옆 2만큼 공간 확장
    prev_star_output = expand_space(prev_star_output)
    prev_star_output[2][-2] = "*"
    return prev_star_output


def main():
    # 1. 입력으로 1 <= N <=의 값을 입력받는다.
    N = int(input())
    # 2. 해당 N에 맞는 별이 담긴 리스트를 변수에 저장한다.
    star_list = print_star(N)
    # 2중 리스트에 담겨있는 별을 출력한다.
    for line in map("".join, star_list):
        print(line.rstrip())


if __name__ == "__main__":
    main()