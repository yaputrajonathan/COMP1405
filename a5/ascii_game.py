#Jonathan 101161272


def main():
    print("test")
    
    userReplay = 'y'
    while userReplay == 'y':
        totalMoves = 0
        for i in range(1,6):
            game = True
            moves = 0
            temp = readLevel(i)
            b = temp[:]
            while game == True:
                
                row = len(b) - 1
                col = len(b[-1]) - 1

                displayBoard(b)

                x = getUserAction(row,col)
                userSymbol = x[0]
                userRow  = x[1]
                userCol = x[2]
                targetSymbol = b[userRow][userCol]

                fill(b,targetSymbol,userSymbol,userRow,userCol)
                
                check = []
                for j in range(row):
                    check.append(b[0]==b[j])
                
                if False not in check:
                    game = False

                moves += 1

            totalMoves += moves

            print(f"Level {i} Completed in {moves} moves!")

        print(f"You Win! Thanks for playing!\n\
Total moves: {totalMoves}")

        userReplay = input("Would you like to play again? (y/n): ")

        if userReplay == 'n':
            break
        elif userReplay == 'y':
            continue
                  
        else:
            print("Please enter 'y' or 'n'")  



def readLevel(lvl):
    '''Opens the file of the desired level, and returns the 
    2D list of symbols.'''

    if lvl == 1:
        f = open("./ascii_levels/ascii_level1.txt","r")
    elif lvl == 2:
        f = open("./ascii_levels/ascii_level2.txt","r")
    elif lvl == 3:
        f = open("./ascii_levels/ascii_level3.txt","r")
    elif lvl == 4:
        f = open("./ascii_levels/ascii_level4.txt","r")
    elif lvl == 5:
        f = open("./ascii_levels/ascii_level5.txt","r")
    else:
        print(f"Sorry level {lvl} does not exist.")
    text = f.readlines()

    newText = []
    for i in range(len(text)):
        nestedText = []
        for j in range(len(text[i])):
            if text[i][j] == '\n':
                continue
            else:
                nestedText.append(text[i][j])
        newText.append(nestedText)

    f.close()

    return newText

    
def displayBoard(L):
    '''Builds the table for the symbols.'''

    # board = []
    # for i in range(len(L)):
    #     nestedBoard = []
    #     for j in range(len(L[i])):
    #         nestedBoard += L[i][j]
    #     board += nestedBoard

    board = L

    print(" "*2, end=' ')

    col = 0
    for i in range(len(board[0])):      #builds the column numbers
        if col >= 10:
            col = 0
            print(col, end= '')
            col += 1
        elif board[0][i] != '\n':
            print(col, end= '')
            col += 1
    print('\n'+' '*3+'-'*(len(board[0])-1))
    
    for i in range(len(board)):         #builds the row numbers
        if board[i][-1] == '\n':
            if i < 10:
                print(f"0{i}|{board[i][:-1]}")
            elif i >= 10:
                print(f"{i}|{board[i][:-1]}")
        else:
            if i < 10:
                print(f"0{i}|{board[i]}")
            elif i >= 10:
                print(f"{i}|{board[i]}")
        
def getUserAction(row, col):
    userActionList = []
    while True:
        userSymbol = input(f"Enter a symbol: ")
        if userSymbol not in ['#','&','%','@'] :
            print(f"Sorry, please select one of: # & % @")
        else:
            userActionList.append(userSymbol)
            break

    while True:
        userRow = int(input(f"Select a row [0-{row}]: "))
        if userRow > row:
            print(f"Oopsies, bad row. Enter a number from 0 to {row}")
        else:
            userActionList.append(userRow)
            break

    while True:
        userCol = int(input(f"Select a column [0-{col}]: "))
        if userCol > col:
            print(f"Oopsies, bad column. Enter a number from 0 to {col}")
        else:
            userActionList.append(userCol)
            break

    return userActionList    
    
def fill(board,targetSymbol,userSymbol,userRow,userCol):
    if (userRow < len(board) and userCol < len(board[0]) and userRow >= 0 and userCol >= 0 \
        and board[userRow][userCol] == targetSymbol and targetSymbol != userSymbol):
        
        board[userRow][userCol] = userSymbol
        fill(board,targetSymbol,userSymbol,userRow - 1,userCol)
        fill(board,targetSymbol,userSymbol,userRow + 1,userCol)                      
        fill(board,targetSymbol,userSymbol,userRow,userCol + 1)
        fill(board,targetSymbol,userSymbol,userRow,userCol - 1)

    else:
        pass