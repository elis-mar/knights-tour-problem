"""
Knights tour problem.
Move a knight on a m x n board so that it visits every square exactly once.
This solution applies Warnsdorf's rule and determines if a m x n board has a solution to the knights tour problem
"""

KNIGHT_MOVES = [
                (-2, -1), (-2, 1), (2, -1), (2, 1),
                (-1, -2), (-1, 2), (1, -2), (1, 2)
]

def generate_board(m: int, n: int) -> list[list[bool]]: return [[False for _ in range(n)] for _ in range(m)]

def find_next_moves(board: list[list[bool]], current_position: tuple[int, int]) -> list[tuple[int, int]]:
    m, n = len(board), len(board[0])
    row = current_position[0]
    column = current_position[1]
    next_moves = []
    for (r, c) in KNIGHT_MOVES:
        (row_move, column_move) = (row + r, column + c)
        if 0 <= row_move < m and 0 <= column_move < n and not board[row_move][column_move]:
            next_moves.append((row_move, column_move))
    return next_moves

def is_solved(board: list[list[bool]]) -> bool: return all(all(row) for row in board)

def solve_with_warnsdorfs_rule(board: list[list[bool]], current_position: tuple[int, int]) -> bool:
    (current_row, current_column) = current_position
    board[current_row][current_column] = True

    if is_solved(board):
        return True

    else:
        next_moves = find_next_moves(board, current_position)
        if next_moves:
            count_of_onward_moves = [len(find_next_moves(board, move)) for move in next_moves]
            next_moves_with_count_of_onward_moves = sorted(zip(next_moves, count_of_onward_moves), key=lambda x: x[1])
            for next_move in next_moves_with_count_of_onward_moves:
                if solve_with_warnsdorfs_rule(board, next_move[0]):
                    return True

        board[current_row][current_column] = False

    return False

def main():
    try:
        m, n = map(int, input("Enter two numbers for m and n seperated by space: ").split())
        if m <= 0 or n <= 0:
            print('m and n must be positive integers')
            return
        else:
            board = generate_board(m, n)
            if solve_with_warnsdorfs_rule(board, (0, 0)):
                print(f'{m} x {n} board has a solution.')
            else:
                print(f'{m} x {n} board does not have a solution.')
    except ValueError:
        print('Please insert two space seperated positive integers')

if __name__ == '__main__':
    main()
