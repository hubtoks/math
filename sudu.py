def solve_sudoku(grid):
    """
    解数独问题
    :param grid: 数独问题
    :return: 解决方案
    """
    # 寻找一个空位置
    row, col = find_empty_location(grid)

    # 如果没有空位置，则返回 True，表示问题已经解决
    if row == -1:
        return True

    # 尝试填充数字
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            # 递归调用 solve_sudoku() 解决下一个位置
            if solve_sudoku(grid):
                return True

            # 如果下一个位置无解，则撤回当前数字
            grid[row][col] = 0

    # 如果所有数字都不能填充，则返回 False，表示问题无解
    return False


def find_empty_location(grid):
    """
    寻找一个空位置
    :param grid: 数独问题
    :return: 空位置的行和列，如果没有空位置则返回 (-1, -1)
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return -1, -1


def is_valid_move(grid, row, col, num):
    """
    判断一个数字是否可以填充到给定位置
    :param grid: 数独问题
    :param row: 行
    :param col: 列
    :param num: 数字
    :return: 如果可以填充，则返回 True，否则返回 False
    """
    # 检查行和列是否有相同的数字
    for i in range(9):
        if grid[row][i] == num:
            return False
        if grid[i][col] == num:
            return False

    # 检查所在的九宫格是否有相同的数字
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row+i][start_col+j] == num:
                return False

    # 如果以上条件都不满足，则可以填充该数字
    return True


# 读取数独问题
grid = []
print("请输入数独问题，每一行用逗号隔开，空位置用 0 表示：")
for i in range(9):
    row = input("第 {} 行：".format(i+1)).strip().split(",")
    row = [int(x) for x in row]
    grid.append(row)

# 调用函数解决问题
solve_sudoku(grid)

import random

def generate_sudoku():
    """
    生成一个数独问题
    :return: 数独问题
    """
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(grid)
    remove_cells(grid)
    return grid

def remove_cells(grid):
    """
    从已解决的数独问题中删除部分单元格，生成一个游戏
    :param grid: 已解决的数独问题
    """
    for row in range(9):
        for col in range(9):
            if random.random() < 0.5:
                grid[row][col] = 0

# 生成数独游戏
game = generate_sudoku()

# 打印数独游戏
print("数独游戏：")
for row in game:
    print(row)


# 打印解决方案
print("解决方案：")
for row in grid:
    print(row)

