class Space:
    def __init__(self):
        self.this = "N"
    
    def __repr__(self):
        return self.this

    def insert(self, color):
        if self.this != "N":
            return False
        self.this = color
        return True

board = [[Space() for i in range(7)] for i in range(6)]
def printBoard():
    for row in reversed(board):
        print(row)
win = False
def check_winner(board):
    rows = len(board)
    cols = len(board[0])

    # Directions: right, down, diag-down-right, diag-up-right
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for y in range(rows):
        for x in range(cols):
            color = board[y][x].this
            if color == "N":
                continue  # skip empty spaces

            # Check all 4 directions
            for dy, dx in directions:
                count = 1
                ny, nx = y, x

                for _ in range(3):  # need 3 more in the same direction
                    ny += dy
                    nx += dx
                    if 0 <= ny < rows and 0 <= nx < cols and board[ny][nx].this == color:
                        count += 1
                    else:
                        break

                if count == 4:
                    return color  # "B" or "R"

    return "N"  # no winner yet

while win == False:
    printBoard()
    entered = False
    while entered == False:
        x = int(input("B Enter x coordinates: "))
        y = int(input("B Enter y coordinates: "))
        if (y == 0 or board[y - 1][x].this != "N") and board[y][x].insert("B"):
            entered = True
        else:
            print('invalid index')
        
    printBoard()
    the_winner = check_winner(board)
    if the_winner != 'N':
        print("The winner is " + the_winner)
        win = True
        continue

    entered = False
    while entered == False:
        x = int(input("R Enter x coordinates: "))
        y = int(input("R Enter y coordinates: "))
        if (y == 0 or board[y - 1][x].this != "N") and board[y][x].insert("R"):
            entered = True
        else:
            print('invalid index')
    
    the_winner = check_winner(board)
    if the_winner != 'N':
        printBoard()
        print("The winner is " + the_winner)
        win = True

