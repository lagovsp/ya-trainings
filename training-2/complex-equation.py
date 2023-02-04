from enum import Enum


class SolutionType(Enum):
    NO = 1
    INF = 2
    REGULAR = 3


def solve_equation(a, b, c, d) -> (SolutionType, int):
    if a == 0:
        if b == 0:
            return SolutionType.INF, None
        return SolutionType.NO, None
    restriction = False if c == 0 else True
    not_x = int(-d / c) if restriction else None
    if b == 0:
        if restriction and not_x == 0:
            return SolutionType.NO, None
        return SolutionType.REGULAR, 0
    if not b % a == 0:
        return SolutionType.NO, None
    ans = int(-b / a)
    if restriction and not_x == ans:
        return SolutionType.NO, None
    return SolutionType.REGULAR, ans


def main():
    status, root = solve_equation(int(input()), int(input()), int(input()), int(input()))
    if status == SolutionType.NO:
        print('NO')
    elif status == SolutionType.INF:
        print('INF')
    else:
        print(f'{root}')


if __name__ == '__main__':
    main()
