# 509-week4
def flood_fill(input_board, old, new, x, y):
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str]): The input board
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    def fill(x, y):
        for s in input_board:
            if len(s) != len(input_board[0]):
                return("input boards length invalid")
        if (
            x < 0
            or x >= len(input_board)
            or y < 0
            or y >= len(input_board[0])
            or input_board[x][y] != old
        ):
            return

        input_board[x] = input_board[x][:y] + new + input_board[x][y + 1:]

        fill(x + 1, y)  # Fill down
        fill(x - 1, y)  # Fill up
        fill(x, y + 1)  # Fill right
        fill(x, y - 1)  # Fill left

    fill(x, y)
    return input_board

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......##......##......",
    ".......##....#######..",
    "....######.......###..",
    "....#..........####..",
    "....##############....",
]

modified_board = flood_fill(board, old=".", new="~", x=5, y=12)

for row in modified_board:
    print(row)

# Expected output:
# ......................
# ......##########......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#......
# ......#~~~~~~~~#####..
# ....###~~~~~~~~~~~~#..
# ....#~~~~~~~~~~~~###..
# ....##############....

# modified_board = flood_fill(board, old=".", new="~", x=1, y=1)

# for row in modified_board:
#     print(row)

# Expected output:
# ~~~~~~~~~~~~~~~~~~~~~~
# ~~~~~~##########~~~~~~
# ~~~~~~#........#~~~~~~
# ~~~~~~#........#~~~~~~
# ~~~~~~#........#####~~
# ~~~~~###............#~
# ~~~~~#............###~
# ~~~~~##############~~~~
