# Drawing the board
def draw_board(arr):
    for i in range(0,3):
        for j in range(0,3):
            
            if (j==0):
                if (i==2):
                    print(arr[i][j] + "  " +  "|", end='' )

                else:
                    print(arr[i][j] + "__" +  "|" , end='' )

            elif (j==1):
                if (i==2):
                    print(arr[i][j] + "  " +  "|", end='' )

                else:
                    print(arr[i][j] + "__" +  "|" , end='' )
                
            elif (j==2):
                if (i==2):
                    print(arr[i][j] + "  ", end='' )

                else: 
                    print(arr[i][j] + "__", end='' )

        print('')


# Asks Player 1 what piece they want, and returns that to Player1's piece variable
def player1_piece():
    piece = input("Player 1, Enter your piece, 'X' or 'O': ").upper()
    return piece

# Win Condition
def win(arr):
    if (((arr[0][0]=='X' and arr[0][1]=='X' and arr[0][2]=='X') or (arr[0][0]=='O' and arr[0][1]=='O' and arr[0][2]=='O')) or
        ((arr[1][0]=='X' and arr[1][1]=='X' and arr[1][2]=='X') or (arr[1][0]=='O' and arr[1][1]=='O' and arr[1][2]=='O')) or 
        ((arr[2][0]=='X' and arr[2][1]=='X' and arr[2][2]=='X') or (arr[2][0]=='O' and arr[2][1]=='O' and arr[2][2]=='O'))
        or
        ((arr[0][0]=='X' and arr[1][0]=='X' and arr[2][0]=='X') or (arr[0][0]=='O' and arr[1][0]=='O' and arr[2][0]=='O')) or
        ((arr[0][1]=='X' and arr[1][1]=='X' and arr[2][1]=='X') or (arr[0][1]=='O' and arr[1][1]=='O' and arr[2][1]=='O')) or
        ((arr[0][2]=='X' and arr[1][2]=='X' and arr[2][2]=='X') or (arr[0][2]=='O' and arr[1][2]=='O' and arr[2][2]=='O'))
        or
        ((arr[0][0]=='X' and arr[1][1]=='X' and arr[2][2]=='X') or (arr[0][0]=='O' and arr[1][1]=='O' and arr[2][2]=='O')) or
        ((arr[0][2]=='X' and arr[1][1]=='X' and arr[2][0]=='X') or (arr[0][2]=='O' and arr[1][1]=='O' and arr[2][0]=='O'))
    ):
        return True

    else:
        return False


#*** Main ***#
def main():

    theBoard = [['1', '2', '3'],['4', '5', '6'],['7', '8', '9']]

    player1 = player1_piece()

    if (player1 == 'X'):
        player2 = 'O'

    else:
        player2 = 'X'

    print("These are the Positions of the board: ")
    draw_board(theBoard)

    theBoard = [[' ', ' ', ' '],[' ', ' ', ' '],[' ', ' ', ' ']]

    # Turn represents which players turn, Slots_left represents amount of board left
    turn=1; slots_left=9

    # Position represents where you wanna write your thing
    position=0

    while True:

        #print(slots_left)
        
        if (turn==1):

            row=0; col=0

            tac = int(input(f"Which Position Does player {turn} want to draw: "))

            while (tac>3):
                tac-=3
                row+=1
            
            col = tac-1

            while(theBoard[row][col] != " "):
                row = 0; col = 0

                tac = int(input("That Position already has something drawn. Re-enter Position: "))

                while (tac>3):
                    tac-=3
                    row+=1
                    
                col = tac-1

            theBoard[row][col] = player1

            draw_board(theBoard)

            if (win(theBoard)==True):
                print(f"Player {turn} Wins!")
                return

            turn=2; slots_left-=1

        #print(slots_left)

        if (slots_left==0):
            print("Game is a Draw!")
            return

        if (turn==2):

            row=0; col=0

            tac = int(input(f"Which Position Does player {turn} want to draw: "))

            while (tac>3):
                tac-=3
                row+=1
            
            col = tac-1

            while(theBoard[row][col] != " "):
                row = 0; col = 0

                tac = int(input("That Position already has something drawn. Re-enter Position: "))

                while (tac>3):
                    tac-=3
                    row+=1

                col = tac-1

            theBoard[row][col] = player2

            draw_board(theBoard)

            if (win(theBoard)==True):
                print(f"Player {turn} Wins!")
                return

            turn=1; slots_left-=1

        if (slots_left==0):
            print("Game is a Draw!")
            return

main() 

    