import random
def possible():
    #Adds all possible 4-in-a-row's to a list for the AI to watch for, 69 total
    #In: Nothing
    #Out: A list of dictionary(key: rows or columns depending on the direction
    #                          value: a list of lists of 4 tuples)
    #    List order: horizontal, vertical, diagonal-right, diagonal-left

    #Vertical
    v = {}
    #Iterate over the columns
    for x in range(0,7):     
        #Each column has 3 possibilities, determined by the starting row
        temp = [[],[],[]]
        #Iterate over the four consecutive cells, changing the starting row for each list
        for y in range(0,4):
            #Make a list of coordinates
            temp[0].append((x,y))
        for y in range(1,5):
            temp[1].append((x,y))
        for y in range(2,6):
            temp[2].append((x,y))
        #Add the three lists to the dictionary stored under the column
        v[x] = temp

    #Horizontal
    h = {}
    #Iterate over the rows
    for y in range(0,6):
        #Each row has four possibilities, determined by the starting column
        temp = [[],[],[],[]]
        for x in range(0,4):
            temp[0].append((x,y))
        for x in range(1,5):
            temp[1].append((x,y))
        for x in range(2,6):
            temp[2].append((x,y))
        for x in range(3,7):
            temp[3].append((x,y))
        #Keyed by row
        h[y] = temp

    #Diagonal-right
    dr = {}
    #Iterate over the bottom three rows
    for y in range (0,3):
        temp = [[],[],[],[]]
        
        for x in range(0,4):
            for n in range(0,4):
                temp[x].append((x+n,y+n))
        #Keyed by row
        dr[y] = temp

    #Diagonal-left
    dl = {}
    for y in range (0,3):
        temp = [[],[],[],[]]
        for x in range(3,7):
            for n in range(0,4):
                temp[x-3].append((x-n,y+n))
        dl[y] = temp
        
    return [h,v,dr,dl]

def print_rules():
    #Output Connect-4 rules
    #In: Nothing
    #Out: Nothing
    
    print "Play correctly please."

def print_board(board, whos_move= 'c'):
    #Output the current board
    #In: List of lists, Character to indicate who's move is being printed
    #                   defaulted to computer
    #Out: Nothing

    if whos_move == 'p':
        print "PLAYER'S MOVE:"
    elif whos_move == 'c':
        print "COMPUTER'S MOVE:"
    else:
        print ""
    
    print board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5]
    print board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4]
    print board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3]
    print board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2]
    print board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1]
    print board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0]
    print board[7][0],board[7][1],board[7][2],board[7][3],board[7][4],board[7][5],board[7][6]

def gravity(board, col, char):
    #Makes piece fall to first unoccupied row
    #In: List of lists, Int of index, Character to replace in indexed cell
    #Out: Updated list of lists, Int of cell row

    #Iterate through column cells until it finds an empty cell
    #Need to check before calling gravity if column is full
    i = 0
    while 1:
        if board[col][i] == '.':
            board[col][i] = char
            break
        else: i += 1
    return board, i

def player(board):
    #Get user move and put it into the board
    #In: List of lists
    #Out: Updated list of lists, tuple of coordinates

    while 1:
        #Get user move
        col = raw_input("Which column?(enter a number): ")
        #Check if user input is a number
        try:
            col = int(col)
        except ValueError: print "Please enter a number."
        else:
            #Check if user input is one of the available columns
            if (col > 0) and (col <= 7):
                #Account for index starting with 0
                col -= 1
                #Check if user input is in a full column
                if (board[col][-1] == 'o') or (board[col][-1] == 'x'):
                    print "Please choose a valid column"
                else:
                    break
            else: print "Please choose a valid column"

    #Put player piece into the board
    board, i = gravity(board, col, 'x')
    #Display the player move
    print_board(board, 'p')
    return board, (col,i)

def ai(board, p, pos):
    #Process board state and choose an appropriate move
    #In: List of lists, Tuple of last player move, List of dictionaries of connect-4's
    #Out: Updated list of lists, Updated list of dictionaries, Tuple of computer move
    
    def ai_gravity(board, col, row):
        #Check to see if first unoccupied row is the same as the desired row
        #In: List of lists, Int of column, Int of desired row
        #Out: Updated list of lists, Boolean

        #Same as gravity()
        i=0
        while 1:
            if board[col][i] == '.':break
            else:i += 1

        #Check if desired row is the same as the row that the piece will fall into
        if row == i:
            #Move computer piece into cell if the desired is the same as the actual
            board[col][row] = 'o'
            return board, True
        else:
            #AI needs to choose a different location
            return board, False

    def ai_blocked(direction, k, n):
        #Check if there's a tuple in a set of four cells
        #In: Dictionary keyed by row, Int of key, Int of index
        #Out: Boolean
        
        #Check to see if all locations in a connect-4 are filled
        for i in range(0,4):
            #If there's a tuple, the set of four is still in play
            if type(direction[k][n][i]) == tuple:
                return True
        #Set of four is filled
        return False

    def ai_helper(board, d):
        #
        #In: List of lists, Dictionary keyed by row
        #Out: Updated list of lists, Updated dictionary, Tuple of move coordinates or
        #false boolean

        #No block move to make, updated when a move is found
        move = False

        #Iterate over keys
        for k in d.iterkeys():
            #Iterate over list of possible 4 consecutive cells
            for n in range(len(d[k])):
                try:
                    #Check if last player move is in current possible 4, Error if not
                    i = d[k][n].index(p)
                    #Update list of possibilities
                    d[k][n][i]='x'
                    
                    #Exit for statement if computer move has already been taken this turn
                    if move != False:
                        raise ValueError

                    #Remove a filled set of four cells from the list of possibilities
                    #Remove current connect-4 and exit for statement if it is filled
                    if not(ai_blocked(d, k, n)):
                        d[k][n] = []
                        raise ValueError
                    
                    #Check for block that needs two moves
                    #Check for 3-in-a-row
                    if (i==1 or i==2):
                        if (d[k][n][1]=='x' and d[k][n][2]=='x'):
                            #Check if already blocked
                            if not(d[k][n][0]=='o' or d[k][n][3]=='o'):
                                #3-in-a-row
                                if d[k][n][0] == 'x':
                                    col = d[k][n][3][0]
                                    row = d[k][n][3][1]
                                    #Check if fourth place is active to play in,
                                    #place piece if it is
                                    board, boolean = ai_gravity(board, col, row)
                                    if boolean:
                                        #Connect-4 is full, remove it
                                        d[k][n] = []
                                        #AI has moved
                                        move = (col, row)

                                #3-in-a-row
                                elif d[k][n][3] == 'x':
                                    col = d[k][n][0][0]
                                    row = d[k][n][0][1]
                                    board, boolean = ai_gravity(board, col, row)
                                    if boolean:
                                        d[k][n] = []
                                        move = (col, row)

                                #Make first block
                                else:
                                    #Arbitrarily choose left side
                                    col = d[k][n][0][0]
                                    row = d[k][n][0][1]
                                    board, boolean = ai_gravity(board, col, row)
                                    if boolean:
                                        d[k][n] = []
                                        move = (col, row)
                                    else:
                                        #If left is not active try right
                                        col = d[k][n][3][0]
                                        row = d[k][n][3][1]
                                        board, boolean = ai_gravity(board, col, row)
                                        if boolean:
                                            d[k][n] = []
                                            move = (col, row)

                    #Check for 3 alternating columns trap
                    if d[k][n][1]=='x' and d[k][n][3]=='x':
                        #Check third column
                        if d[k][n-1][2]=='x':
                            #Move in between columns 2 and 3 to block
                            col = d[k][n][2][0]
                            row = d[k][n][2][1]
                            board, boolean = ai_gravity(board, col, row)
                            if boolean:
                                d[k][n] = []
                                move = (col, row)

                                
                    #Check for split 3-in-a-row
                    if (d[k][n][0]=='x' and d[k][n][1]=='x' and d[k][n][3]=='x'):
                        col = d[k][n][2][0]
                        row = d[k][n][2][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            d[k][n] = []
                            move = (col, row)
                    if (d[k][n][0]=='x' and d[k][n][2]=='x' and d[k][n][3]=='x'):
                        col = d[k][n][1][0]
                        row = d[k][n][1][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            d[k][n] = []
                            move = (col, row)

                #Stifle Errors
                #Player move is not the list, or statement exit point
                except ValueError: 1
                #Ignore empty list
                except IndexError: 1

        #If AI has made a move, print it
        if move != False:
            print_board(board)

        return board, d, move

    def ai_win (board, d):
        #Check for 3-in-a-row of computer pieces
        #In: List of lists, Dictionary of lists
        #Out: Updated list of lists, Tuple of move or Boolean

        #Iterate over keys
        for k in d.iterkeys():
            #Iterate over lists
            for n in range(len(d[k])):
                try:
                    #Check for 3 consecutive AI pieces ...o
                    if (d[k][n][0] == 'o') and (d[k][n][1] == 'o') and (d[k][n][2] == 'o'):
                        col = d[k][n][3][0]
                        row = d[k][n][3][1]
                        #Check if fourth place is active
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            #If AI has moved, print and return location
                            print_board(board)
                            return board, (col, row)
                    #..o.
                    elif (d[k][n][0] == 'o') and (d[k][n][1] == 'o') and (d[k][n][3] == 'o'):
                        col = d[k][n][2][0]
                        row = d[k][n][2][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            print_board(board)
                            return board, (col, row)
                    #.o..
                    elif (d[k][n][0] == 'o') and (d[k][n][2] == 'o') and (d[k][n][3] == 'o'):
                        col = d[k][n][1][0]
                        row = d[k][n][1][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            print_board(board)
                            return board, (col, row)
                    #o...
                    elif (d[k][n][1] == 'o') and (d[k][n][2] == 'o') and (d[k][n][3] == 'o'):
                        col = d[k][n][0][0]
                        row = d[k][n][0][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            print_board(board)
                            return board, (col, row)
                        
                #Ignore empty lists
                except IndexError: 1
                
        return board, False

    #Set directional variables
    [h,v,dr,dl] = pos    

    #Defensive Portion
    
    #Vertical
    #Different from other directions because of gravity
    for k in v.iterkeys():
        #Iterate over lists
        for n in range(len(v[k])):
            try:
                i = v[k][n].index(p)
                v[k][n][i] = 'x'

                if not(ai_blocked(v, k, n)):
                    v[k][n] = []
                    raise ValueError

                #Check for 3-in-a-row
                if (v[k][n][0]=='x' and v[k][n][1]=='x' and v[k][n][2]=='x'):
                    col = v[k][n][3][0]
                    board, row = gravity(board, col, 'o')
                    v[k][n] = []
                    print_board(board)
                    return board, pos, (col, row)

            #Possibility does not include the last player move
            except ValueError: 1

    #Horizontal
    board, h, loc = ai_helper(board, h)
    #AI has taken its move
    if type(loc) == tuple:
        return board, pos, loc

    #Right-to-Left Diagonal
    board, dr, loc = ai_helper(board, dr)
    if type(loc) == tuple:
        return board, pos, loc

    #Left-to-Right Diagonal
    board, dl, loc = ai_helper(board, dl)
    if type(loc) == tuple:
        return board, pos, loc


    #Check for Winning Play

    #Vertical Win
    for k in v.iterkeys():
        for n in range(len(v[k])):
            try:
                if (v[k][n][0] == 'o') and (v[k][n][1] == 'o') and (v[k][n][2] == 'o'):
                    col = v[k][n][3][0]
                    board, row = gravity(board, col, 'o')
                    print_board(board)
                    return board, pos, (col, row)
            except IndexError: 1

    #Horizontal Win
    board, loc = ai_win(board, h)
    if type(loc) == tuple:
        return board, pos, loc
    
    #Right-to-Left Diagonal Win
    board, loc = ai_win(board, dr)
    if type(loc) == tuple:
        return board, pos, loc

    #Left-to-Right Diagonal Win
    board, loc = ai_win(board, dl)
    if type(loc) == tuple:
        return board, pos, loc


    #Offensive  
    #Play on top of player's move, annoying but effective
    #makes diagonals difficult to set up and verticals impossible
    col = p[0]
    #If column is full, choose a random column
    if (board[col][-1] == 'o') or (board[col][-1] == 'x'):
        #Random Offensive
        while 1:
            col = random.randint(0,6)
            #If randomly chosen column is full, choose another
            if (board[col][-1] == 'o') or (board[col][-1] == 'x'):
                continue

            #Place piece in column
            board, row = gravity(board, col, 'o')
            print_board(board)
            return board, pos, (col, row)
        
    #Move in the same column the player did
    else:
        board, row = gravity(board, col, 'o')
        print_board(board)
        return board, pos, (col, row)
    
def ai_possible(pos, a):
    #Update the list of possibilities with the last move of the AI
    #In: List of dictionaries and AI coordinate tuple
    #Out: Updated list of dictionaries

    #Set directional variables
    [h,v,dr,dl] = pos

    #Vertical
    #Iterate over the keys
    for k in v.iterkeys():
        #Iterate over columns
        for n in range(len(v[k])):
            try:
                #Check if last move is in the list
                i = v[k][n].index(a)
                v[k][n][i] = 'o'
            #Move is not present
            except ValueError: 1
            
    #Horizontal
    for k in h.iterkeys():
        for n in range(len(h[k])):
            try:
                i = h[k][n].index(a)
                h[k][n][i] = 'o'
            except ValueError: 1

    #Diagonal-Right
    for k in dr.iterkeys():
        for n in range(len(dr[k])):
            try:
                i = dr[k][n].index(a)
                dr[k][n][i] = 'o'
            except ValueError: 1

    #Diagonal-Left
    for k in dl.iterkeys():
        for n in range(len(dl[k])):
            try:
                i = dl[k][n].index(a)
                dl[k][n][i] = 'o'
            except ValueError: 1

    return [h,v,dr,dl]
    
def check_win(board):
    #Check for 4-in-a-row from player or AI
    #In: List of lists
    #Out: Updated list of lists, Boolean, String of winner
    def helper(c, r, loc, l):
        #Move across board, in direction defined by passed integers
        #In: Int of column modification, Int of row mod, Tuple of last move, List of
        #all moves of either the player or the AI
        #Out: Boolean

        #Check 3 places from last move
        for i in range(3):
            #Move to consecutive cell in specified direction
            next_loc = (loc[0]+c, loc[1]+r)
            #Continue to next cell if it is the correct symbol
            if l.count(next_loc) == 1:
                loc = next_loc
            else:
                return False
        return True
        
    def replace_helper(c, r, loc, board, char):
        #Highlight the winning cells with capital letters
        #In: Int of column modification, Int of row mod, Tuple of last move, List of
        #lists, Character to replace with
        #Out: Updated list of lists

        #Go to each cell in the winning 4-in-a-row
        board[loc[0]][loc[1]] = char
        board[loc[0]+c][loc[1]+r] = char
        board[loc[0]+c+c][loc[1]+r+r] = char
        board[loc[0]+c+c+c][loc[1]+r+r+r] = char
        
        return board
    
    xs = []
    os = []
    full = False

    #Create list of all the player moves and all the AI moves
    for col in [0,1,2,3,4,5,6]:
        for cell in [0,1,2,3,4,5]:
            if (board[col][cell] == 'o'):
                os.append((col,cell))
            elif (board[col][cell] == 'x'):
                xs.append((col,cell))
            else:
                continue

    #Check for full board / tie game
    if (len(xs)+len(os))==42:
        full = True

    #Check each x for 3 more consecutive x's
    for index in (range(len(xs))):
        loc = xs.pop(0)
        #Vertical (0,1)
        if helper(0,1,loc,xs):
            board = replace_helper(0,1,loc,board,"X")
            return board, True, "Player"
        #Horizontal (1,0)
        elif helper(1,0,loc,xs):
            board = replace_helper(1,0,loc,board,"X")
            return board, True, "Player"
        #Diagonal-Right (1,1)
        elif helper(1,1,loc,xs):
            board = replace_helper(1,1,loc,board,"X")
            return board, True, "Player"
        #Diagonal-Left (1,-1)
        elif helper(1,-1,loc,xs):
            board = replace_helper(1,-1,loc,board,"X")
            return board, True, "Player"
        else:
            continue

    #Check each o for 3 more consecutive o's
    for index in (range(len(os))):
        loc = os.pop(0)
        #Vertical (0,1)
        if helper(0,1,loc,os):
            board = replace_helper(0,1,loc,board,"O")
            return board, True, "Computer"
        #Horizontal (1,0)
        elif helper(1,0,loc,os):
            board = replace_helper(1,0,loc,board,"O")
            return board, True, "Computer"
        #Diagonal-Right (1,1)
        elif helper(1,1,loc,os):
            board = replace_helper(1,1,loc,board,"O")
            return board, True, "Computer"
        #Diagonal-Left (1,-1)
        elif helper(1,-1,loc,os):
            board = replace_helper(1,-1,loc,board,"O")
            return board, True, "Computer"
        else:
            continue

    #Check for tie game
    if full:
        return board, True, "Neither"

    return board, False, ""

def setup():
    #Set a blank plaing board and a blank set of all possible winning combinations
    #In: Nothing
    #Out: List of lists, List of dictionaries

    #Connect-4 board has 7 columns and 6 rows
    c1=['.','.','.','.','.','.']
    c2=['.','.','.','.','.','.']
    c3=['.','.','.','.','.','.']
    c4=['.','.','.','.','.','.']
    c5=['.','.','.','.','.','.']
    c6=['.','.','.','.','.','.']
    c7=['.','.','.','.','.','.']
    labels=['1','2','3','4','5','6','7']
    board = [c1,c2,c3,c4,c5,c6,c7, labels]

    #Print blank board
    print_board(board, '')

    #Set list of possibilities for AI
    pos = possible()

    return board, pos    

def play():
    #Call functions to guide the course of the game
    #In: Nothing
    #Out: String describing who wins
    board, pos= setup()
    while 1:
        board, col = player(board)
        board, end, who = check_win(board)
        if end == True:
            print_board(board, '')
            print who + " Wins!"
            break
        board, pos, a = ai(board, col, pos)
        pos = ai_possible(pos, a)
        board, end, who = check_win(board)
        if end == True:
            print_board(board, '')
            print who + " Wins!"
            break
    return who

def sore_loser():
    #AI cheats if it gets too behind in play stats
    #In: Nothing
    #Out: String describing who won
    
    ##Could also cheat by marking player moves as o's

    #Same as play(), except doesn't let the player win count, turns into a computer win
    #Player win will still be highlighted
    board, pos = setup()
    while 1:
        board, col = player(board)
        board, end, who = check_win(board)
        if end == True:
            #Cheat if player will win, set a vertical computer win in the last column
            board[-2][0] = 'o'
            board[-2][1] = 'o'
            board[-2][2] = 'o'
            board[-2][3] = 'o'
        board, pos, a = ai(board, col, pos)
        pos = ai_possible(pos, a)
        board, end, who = check_win(board)
        if end == True:
            print_board(board, '')
            print who + " Wins!"
            break
    return who

#Win Count
human = 0
computer = 0
cheat = False
while 1:
    #AI will cheat and not allow the player to win
    if (human - computer) >= 3:
        cheat = True
        winner = sore_loser()
    #Run program
    else:
        winner = play()
    #Update play count
    if winner == "Computer":
        computer += 1
    elif winner == "Player":
        human += 1
    #Print play count
    print "The player  has  won ",human," times."
    print "The computer has won ",computer," times."
    #Keep playing additional games
    again = raw_input("Would you like to play again? (y/n): ")
    if again != 'y':
        break
        


