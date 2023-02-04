import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.is_vertical = True if p1.x == p2.x else False
        self.k = math.inf if self.is_vertical else (p2.y - p1.y) / (p2.x - p1.x)


def are_lines_parallel(l1: Line, l2: Line) -> bool:
    return l1.k == l2.k


def is_parallelogram(points: tuple[Point, Point, Point, Point]) -> bool:
    if not are_lines_parallel(Line(points[0], points[1]), Line(points[2], points[3])):
        return False
    if not are_lines_parallel(Line(points[0], points[3]), Line(points[1], points[2])):
        return False
    return True


def main():
    queries = int(input())

    for _ in range(queries):
        coordinates = list(map(int, input().split()))

        p1 = Point(coordinates[0], coordinates[1])
        p2 = Point(coordinates[2], coordinates[3])
        p3 = Point(coordinates[4], coordinates[5])
        p4 = Point(coordinates[6], coordinates[7])

        perms = [
            (p1, p2, p3, p4),
            (p1, p2, p4, p3),
            (p1, p3, p2, p4),
            (p1, p3, p4, p2),
        ]

        is_par = False
        for perm in perms:
            if is_parallelogram(perm):
                print('YES')
                is_par = True
                break
        if not is_par:
            print('NO')


if __name__ == '__main__':
    main()
