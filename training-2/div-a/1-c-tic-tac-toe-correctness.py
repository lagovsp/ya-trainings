def moves_numbers(lines: list[list[int]]) -> (int, int, int):
    crosses, noughts, empties = 0, 0, 0
    for line in lines:
        for cell in line:
            if cell == 1:
                crosses += 1
                continue
            if cell == 2:
                noughts += 1
                continue
            if cell == 0:
                empties += 1
    return crosses, noughts, empties


def wins_for_side(lines: list[list[int]], side: int) -> int:
    counter = 0
    if lines[0][0] == lines[1][1] == lines[2][2] == side:
        counter += 1
    if lines[0][2] == lines[1][1] == lines[2][0] == side:
        counter += 1
    for i in range(3):
        if lines[i][0] == lines[i][1] == lines[i][2] == side:
            counter += 1
    for j in range(3):
        if lines[0][j] == lines[1][j] == lines[2][j] == side:
            counter += 1
    return counter


def is_correct(lines: list[list[int]]) -> bool:
    crosses, noughts, empties = moves_numbers(lines)
    if crosses not in [noughts, noughts + 1]:
        return False
    wins = [wins_for_side(lines, 1), wins_for_side(lines, 2)]
    if 0 not in wins:
        return False
    if wins[0] > 2 or wins[1] > 1:
        return False
    if wins[1] == 1 and crosses > noughts:
        return False
    if wins[0] == 1 and crosses == noughts:
        return False
    return True


def main():
    lines = [list(map(int, input().split())) for _ in range(3)]
    print('YES' if is_correct(lines) else 'NO')


if __name__ == '__main__':
    main()
