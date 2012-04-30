import random
def possible():
    #Adds all possible 4-in-a-row's to a list for the AI to watch for
    #In: nothing
    #Out: A list of dictionary(key: rows or columns depending on the direction
    #                          value: a list of lists of 4 tuples)
    #    List order: horizontal, vertical, diagonal-right, diagonal-left

    #Vertical
    v = {}
    for x in range(0,7):
        temp = [[],[]]
        for y in range(0,4):
            temp[0].append((x,y))
        for y in range(1,5):
            temp[1].append((x,y))
        v[x] = temp

    #Horizontal
    h = {}
    for y in range(0,6):
        temp = [[],[],[],[]]
        for x in range(0,4):
            temp[0].append((x,y))
        for x in range(1,5):
            temp[1].append((x,y))
        for x in range(2,6):
            temp[2].append((x,y))
        for x in range(3,7):
            temp[3].append((x,y))
        h[y] = temp

    #Diagonal-right
    dr = {}
    for y in range (0,3):
        temp = [[],[],[],[]]
        for x in range(0,4):
            for n in range(0,4):
                temp[x].append((x+n,y+n))
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
    #In: nothing
    #Out: nothing
    
    print "Play correctly please."

def print_board(board, whos_move= 'c'):
    #
    #Takes a list of lists
    #Out: nothing

    if whos_move == 'p':
        print "PLAYER'S MOVE:"
    elif whos_move == 'c':
        print "COMPUTER'S MOVE:"
    else: 1
    
    print board[0][5],board[1][5],board[2][5],board[3][5],board[4][5],board[5][5],board[6][5]
    print board[0][4],board[1][4],board[2][4],board[3][4],board[4][4],board[5][4],board[6][4]
    print board[0][3],board[1][3],board[2][3],board[3][3],board[4][3],board[5][3],board[6][3]
    print board[0][2],board[1][2],board[2][2],board[3][2],board[4][2],board[5][2],board[6][2]
    print board[0][1],board[1][1],board[2][1],board[3][1],board[4][1],board[5][1],board[6][1]
    print board[0][0],board[1][0],board[2][0],board[3][0],board[4][0],board[5][0],board[6][0]
    print board[7][0],board[7][1],board[7][2],board[7][3],board[7][4],board[7][5],board[7][6]

def gravity(board, col, char):
    #
    #In:
    #Out:
    i = 0
    while 1:
        if board[col][i] == '.':
            board[col][i] = char
            break
        else: i += 1
    return board, i

def player(board):
    #
    #In:
    #Out:

    while 1:
        col = raw_input("Which column?(enter a number): ")
        try:
            col = int(col)
        except ValueError: print "Please enter a number"
        else:
            if (col > 0) and (col <= 7):
                col -= 1
                if (board[col][-1] == 'o') or (board[col][-1] == 'x'):
                    print "Please choose a valid column"
                else:
                    break
            else: print "Please choose a valid column"

    board, i = gravity(board, col, 'x')
    print_board(board, 'p')
    return board, (col,i)

def ai(board, p, pos):
    #
    #In:
    #Out:
    def ai_gravity(board, col, row):
        #
        #In:
        #Out:
        i=0
        while 1:
            if board[col][i] == '.':break
            else:i += 1
        if row == i:
            board, row = gravity(board, col, 'o')
            return board, True
        else:
            return board, False

    def ai_blocked(direction, k, n):
        #
        #In:
        #Out:
        b = False
        for i in range(0,4):
            if type(direction[k][n][i]) == tuple:
                return True
        if b == False:
            return False

    def ai_helper(board, d):
        #
        #In:
        #Out:
        move = False
        for k in d.iterkeys():
            for n in range(len(d[k])):
                try:
                    i = d[k][n].index(p)            
                    d[k][n][i]='x'
                    if move != False:
                        raise ValueError

                    if not(ai_blocked(d, k, n)):
                        d[k][n] = []
                        raise ValueError
                    
                    #Check for block that needs two moves
                    #Check for 3-in-a-row
                    if (i==1 or i==2):
                        if (d[k][n][1]=='x' and d[k][n][2]=='x'):
                            if not(d[k][n][0]=='o' or d[k][n][3]=='o'):
                                if d[k][n][0] == 'x':
                                    col = d[k][n][3][0]
                                    row = d[k][n][3][1]
                                    board, boolean = ai_gravity(board, col, row)
                                    if boolean:
                                        d[k][n] = []
                                        move = (col, row)

                                elif d[k][n][3] == 'x':
                                    col = d[k][n][0][0]
                                    row = d[k][n][0][1]
                                    board, boolean = ai_gravity(board, col, row)
                                    if boolean:
                                        d[k][n] = []
                                        move = (col, row)
                                        
                                else:
                                    #Arbitrarily choose left
                                    col = d[k][n][0][0]
                                    row = d[k][n][0][1]
                                    board, boolean = ai_gravity(board, col, row)
                                    if boolean:
                                        d[k][n] = []
                                        move = (col, row)
                                    else:
                                        #Try right
                                        col = d[k][n][3][0]
                                        row = d[k][n][3][1]
                                        board, boolean = ai_gravity(board, col, row)
                                        if boolean:
                                            d[k][n] = []
                                            move = (col, row)

                    #Check for alternating trap
                    if d[k][n][1]=='x' and d[k][n][3]=='x':
                        print d[k]
                        print d[k][n-1]
                        if d[k][n-1][2]=='x':
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
                except ValueError: 1
                except IndexError: 1
        if move != False:
            print_board(board)
        return board, d, move

    def ai_win (board, d):
        #
        #In:
        #Out:
        for k in d.iterkeys():
            for n in range(len(d[k])):
                try:
                    if (d[k][n][0] == 'o') and (d[k][n][1] == 'o') and (d[k][n][2] == 'o'):
                        col = d[k][n][3][0]
                        row = d[k][n][3][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            print_board(board)
                            return board, (col, row)
                    elif (d[k][n][0] == 'o') and (d[k][n][1] == 'o') and (d[k][n][3] == 'o'):
                        col = d[k][n][2][0]
                        row = d[k][n][2][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            print_board(board)
                            return board, (col, row)
                    elif (d[k][n][0] == 'o') and (d[k][n][2] == 'o') and (d[k][n][3] == 'o'):
                        col = d[k][n][1][0]
                        row = d[k][n][1][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            print_board(board)
                            return board, (col, row)
                    elif (d[k][n][1] == 'o') and (d[k][n][2] == 'o') and (d[k][n][3] == 'o'):
                        col = d[k][n][0][0]
                        row = d[k][n][0][1]
                        board, boolean = ai_gravity(board, col, row)
                        if boolean:
                            print_board(board)
                            return board, (col, row)
                except IndexError: 1
        return board, False


    [h,v,dr,dl] = pos    

    #Defensive Portion
    
    #Vertical (different from other directions because of gravity)
    for k in v.iterkeys():
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
            except ValueError: 1

    #Horizontal
    board, h, loc = ai_helper(board, h)
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
    #Play on top Offensive, annoying but effective
    col = p[0]
    if (board[col][-1] == 'o') or (board[col][-1] == 'x'):
        #Random Offensive
        while 1:
            col = random.randint(0,6)
            if (board[col][-1] == 'o') or (board[col][-1] == 'x'):
                continue
            board, row = gravity(board, col, 'o')
            print_board(board)
            return board, pos, (col, row)
    else:
        board, row = gravity(board, col, 'o')
        print_board(board)
        return board, pos, (col, row)
    
def ai_possible(pos, a):
    #
    #In: Possible dictionary and AI coordinate tuple
    #Out: Updated possible dictionary
    
    [h,v,dr,dl] = pos
    blargh = []
    blargh += pos
    for k in v.iterkeys():
        for n in range(len(v[k])):
            try:
                i = v[k][n].index(a)
                v[k][n][i] = 'o'
            except ValueError: 1
    for k in h.iterkeys():
        for n in range(len(h[k])):
            try:
                i = h[k][n].index(a)
                h[k][n][i] = 'o'
            except ValueError: 1
    for k in dr.iterkeys():
        for n in range(len(dr[k])):
            try:
                i = dr[k][n].index(a)
                dr[k][n][i] = 'o'
            except ValueError: 1
    for k in dl.iterkeys():
        for n in range(len(dl[k])):
            try:
                i = dl[k][n].index(a)
                dl[k][n][i] = 'o'
            except ValueError: 1

    return [h,v,dr,dl]
    
def check_win(board):
    #
    #In:
    #Out:
    def helper(c,r,loc,xs):
        #
        #In:
        #Out: Boolean, 
        for i in range(3):  
            next_loc = (loc[0]+c, loc[1]+r)
            if xs.count(next_loc) == 1:
                loc = next_loc
            else:
                return False
        return True
        
    def replace_helper(c,r,loc,board, char):
        #
        #In:
        #Out:
        board[loc[0]][loc[1]] = char
        board[loc[0]+c][loc[1]+r] = char
        board[loc[0]+c+c][loc[1]+r+r] = char
        board[loc[0]+c+c+c][loc[1]+r+r+r] = char
        return board
    
    xs = []
    os = []
    full = False

    for col in [0,1,2,3,4,5,6]:
        for cell in [0,1,2,3,4,5]:
            if (board[col][cell] == 'o'):
                os.append((col,cell))
            elif (board[col][cell] == 'x'):
                xs.append((col,cell))
            else:
                continue

    if (len(xs)+len(os))==42:
        full = True
    
    for index in (range(len(xs))):
        loc = xs.pop(0)
        #V (0,1)
        if helper(0,1,loc,xs):
            board = replace_helper(0,1,loc,board,"X")
            return board, True, "Player"
        #H (1,0)
        elif helper(1,0,loc,xs):
            board = replace_helper(1,0,loc,board,"X")
            return board, True, "Player"
        #D-R (1,1)
        elif helper(1,1,loc,xs):
            board = replace_helper(1,1,loc,board,"X")
            return board, True, "Player"
        #D-L (1,-1)
        elif helper(1,-1,loc,xs):
            board = replace_helper(1,-1,loc,board,"X")
            return board, True, "Player"
        else:
            continue

    for index in (range(len(os))):
        loc = os.pop(0)
        #V (0,1)
        if helper(0,1,loc,os):
            board = replace_helper(0,1,loc,board,"O")
            return board, True, "Computer"
        #H (1,0)
        elif helper(1,0,loc,os):
            board = replace_helper(1,0,loc,board,"O")
            return board, True, "Computer"
        #D-R (1,1)
        elif helper(1,1,loc,os):
            board = replace_helper(1,1,loc,board,"O")
            return board, True, "Computer"
        #D-L (1,-1)
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
    #
    #In: Nothing
    #Out: 
    
    c1=['.','.','.','.','.','.']
    c2=['.','.','.','.','.','.']
    c3=['.','.','.','.','.','.']
    c4=['.','.','.','.','.','.']
    c5=['.','.','.','.','.','.']
    c6=['.','.','.','.','.','.']
    c7=['.','.','.','.','.','.']
    labels=['1','2','3','4','5','6','7']
    board = [c1,c2,c3,c4,c5,c6,c7, labels]

    print_board(board, '')

    pos = possible()

    return board, pos    

def play():
    #
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
        


