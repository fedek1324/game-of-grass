from collections import namedtuple, defaultdict
import time
from random import randint
from rules import *

# Cell = namedtuple('Cell', ['x', 'y', 'grow', 'color'], defaults=(1,) * 2)
rule = Rule()

class Cell:
    def __init__(self, x, y, grow = randint(1,4), color = randint(0,255)):
        self.x = x
        self.y = y
        self.grow = grow
        self.color = color


    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.__key() == other.__key()
        return NotImplemented


    def __key(self):
            return (self.x, self.y)

    def __hash__(self):
        return hash(self.__key())


def getNeighbours(cell):
    for x in range(cell.x - rule.radius, cell.x + 1 + rule.radius):                     # Перебираем значения в диапазоне x
        for y in range(cell.y - rule.radius, cell.y + 1 + rule.radius):                 # Перебираем значения в диапозоне y
            if (x, y) != (cell.x, cell.y):                      # Если эта другая клетка, сосед
                yield Cell(x, y)                                # Вернуть её


def getNeighbourCount(board):
    neighbour_counts = defaultdict(int)                         # Создаём словарь для сохранения количества соседей каждой клетки
    for cell in board:                                          # Перебираем все клетки на столе
        for neighbour in getNeighbours(cell):                   # Считываем соседей
            neighbour_counts[neighbour] += 1                    # Считаем их для каждой клетки
    return neighbour_counts


def advanceBoard(board):
    new_board = set()                                           # Создаём новое множество (расстановку)
    for cell, count in getNeighbourCount(board).items():        # Достаём из предшествующей расстановки
        if (count in rule.burn):
            cell.grow = 1
            new_board.add(cell)
        elif (cell in board and count in rule.surv):
            cell.grow += 1
            new_board.add(cell)

    return new_board


def generateBoard(desc : str) -> set():
    board = set()
    print("start")
    for row, line in enumerate(desc.split("\n")):               # Разбивает исходный тект на строки.
        for col, elem in enumerate(line):                       # Разбивает строку на символы
            if elem == 'X':                                    # Если это клетка
                board.add(Cell(x=int(col), y=int(row)))             # Добавить в множество её
    return board


def boardToString(board, pad=0):
    if not board:
        return "empty"
    board_str = ""
    xs = [x for (x, y) in board]
    ys = [y for (x, y) in board]
    for y in range(min(ys) - pad, max(ys) + 1 + pad):
        for x in range(min(xs) - pad, max(xs) + 1 + pad):
            board_str += 'X' if Cell(x, y) in board else '.'
        board_str += '\n'
    return board_str.strip()


if __name__ == '__main__':
    f = generateBoard("......X.\nXX......\n.X...XXX")
    for _ in range(10):
        f = advanceBoard(f)
        print("\033[2J\033[1;1H" + boardToString(f, 2))
        time.sleep(0.333)
