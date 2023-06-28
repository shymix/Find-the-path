from typing import List, Type


class Point:

    def __init__(self, a: int = -1, b: int = -1):
        self.x: int = a
        self.y: int = b

    def move(self, x, y):
        self.x = x
        self.y = y


def print_visited(arr: list[bool]):
    print("Visited numbers:\n")

    for i, k in enumerate(arr):
        if k:
            print(i + 1, end=' ')

    print("\n")


def is_done(arr: list[bool]) -> bool:
    for i in arr:
        if not i:
            return False

    return True


def print_labyrinth(lab: int, size: int, path: list[Point], depth: int) -> object:
    for y in range(size):
        for x in range(size):
            f: bool = False

            for d in range(depth):
                if path[d].x == x and path[d].y == y:
                    f = True
                    break

            if f:
                print(".", end='')
            else:
                print("o", end='')

        print("\n")


def main():
    LEN: int = 8
    NUMBERS_AMOUNT: int = 33

    labyrinth = [
        [1, 16, 5, 20, 25, 9, 21, 1],
        [18, 10, 27, 26, 11, 17, 12, 32],
        [32, 11, 15, 29, 8, 6, 27, 20],
        [17, 4, 13, 24, 30, 28, 31, 2],
        [25, 10, 2, 26, 4, 28, 22, 13],
        [5, 14, 30, 8, 15, 31, 19, 6],
        [23, 7, 24, 16, 29, 22, 18, 19],
        [3, 12, 9, 3, 7, 14, 23, 33]
    ]

    cur_pos = Point(0, 0)
    depth: int = 0
    visited_numbers: list[bool] = [False] * NUMBERS_AMOUNT
    checked: list[list[bool]] = [[False for y in range(4)] for x in range(NUMBERS_AMOUNT)]
    path: list[Type[Point]] = [Point] * NUMBERS_AMOUNT

    while True:
        if depth < 0:
            print("Reached 0. No solution. \n")
            break

        visited_numbers[labyrinth[cur_pos.y][cur_pos.x] - 1] = True
        path[depth] = Point(cur_pos.x, cur_pos.y)

        if is_done(visited_numbers) and path[depth].x == 7 and path[depth].y == 7:
            print("Done.\n\n")

            print_labyrinth(labyrinth, LEN, path, depth)

            print("\nPath:\n")
            for i in range(depth):
                if i != 0:
                    print(" -> ")

                print("(", path[i].x + 1, ", ", path[i].y + 1, ")")

            print("\n\n")
            print_visited(visited_numbers)

            break

        if cur_pos.y + 1 < LEN and not checked[depth][0] and not visited_numbers[
            labyrinth[cur_pos.y + 1][cur_pos.x] - 1]:
            checked[depth][0] = True
            depth += 1
            cur_pos.y += 1

        elif cur_pos.x + 1 < LEN and not checked[depth][1] and not visited_numbers[
            labyrinth[cur_pos.y][cur_pos.x + 1] - 1]:
            checked[depth][1] = True
            depth += 1
            cur_pos.x += 1

        elif cur_pos.y - 1 >= 0 and not checked[depth][2] and not visited_numbers[
            labyrinth[cur_pos.y - 1][cur_pos.x] - 1]:
            checked[depth][2] = True
            depth += 1
            cur_pos.y -= 1

        elif cur_pos.x - 1 >= 0 and not checked[depth][3] and not visited_numbers[
            labyrinth[cur_pos.y][cur_pos.x - 1] - 1]:
            checked[depth][3] = True
            depth += 1
            cur_pos.x -= 1

        else:
            visited_numbers[labyrinth[cur_pos.y][cur_pos.x] - 1] = False

            for k in range(4):
                checked[depth][k] = False

            cur_pos = Point(path[depth - 1].x, path[depth - 1].y)
            depth -= 1


if __name__ == '__main__':
    main()
