import math


class Triangle:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_triangle(a, b, c) -> bool:
        return a + b > c \
            and a + c > b \
            and b + c > a

    @staticmethod
    def _maximize_square(p: int) -> (bool, 'Triangle'):
        one_third = math.floor(p / 3)
        for a in range(one_third, p - one_third + 1):
            b = int((p - a) / 2)
            t = Triangle(a, b, p - a - b)
            if t.is_triangle(t.a, t.b, t.c):
                return True, t
        return False, None

    @staticmethod
    def _minimize_square(p: int) -> (bool, 'Triangle'):
        for a in range(1, math.ceil(p / 3) + 1):
            b = int((p - a) / 2)
            t = Triangle(a, b, p - a - b)
            if Triangle.is_triangle(t.a, t.b, t.c):
                return True, t
        return False, None

    @staticmethod
    def find_extreme_squares(p: int) -> (bool, 'Triangle', 'Triangle'):
        is_largest, largest = Triangle._maximize_square(p)
        is_smallest, smallest = Triangle._minimize_square(p)
        if not is_largest or not is_smallest:
            return False, None, None
        return True, smallest, largest


def main():
    p = int(input())
    status, min_triangle, max_triangle = Triangle.find_extreme_squares(p)

    if not status:
        print(-1)
        return

    print(max_triangle.a, max_triangle.b, max_triangle.c)
    print(min_triangle.a, min_triangle.b, min_triangle.c)


if __name__ == '__main__':
    main()
