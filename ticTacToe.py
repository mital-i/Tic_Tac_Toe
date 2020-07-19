# Tic Tac Toe
# Oh boy.

# All of the main functions of the game have been rearranged into objects
# As  a general summary: The BOARD class has functions involving the game board
# The PLAYER class has the parent class BOARD and contains the basic functions for making a move in tictactoe
# The COMPUTER class has the parent class PLAYER which contains specialized functions with the computer's ai

# Finally, there's the SETUP class, which is seperate and doesn't relate to the functions above.
# It just contains all the functions needed before and after the game to operate (choosing symbol, playing again, ect.)

# The code has been modified to ask the player if they would like to have one or two players.
# The project said "*allow* two players" so just to be on the safe side I put both two and one players

import random


class Board:
    def __init__(self, board):
        self.board = board

    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    def isFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True


class Player(Board):
    def __init__(self, board, letter):
        super().__init__(board)
        self.letter = letter

    def makeMove(self, move):
        self.board[move] = self.letter

    def isWinner(self):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much- is what I would say if I was sane.
        return ((self.board[7] == self.letter and self.board[8] == self.letter and self.board[9] == self.letter) or  # across the top
                (self.board[4] == self.letter and self.board[5] == self.letter and self.board[6] == self.letter) or  # across the middle
                (self.board[1] == self.letter and self.board[2] == self.letter and self.board[3] == self.letter) or  # across the bottom
                (self.board[7] == self.letter and self.board[4] == self.letter and self.board[1] == self.letter) or  # down the left side
                (self.board[8] == self.letter and self.board[5] == self.letter and self.board[2] == self.letter) or  # down the middle
                (self.board[9] == self.letter and self.board[6] == self.letter and self.board[3] == self.letter) or  # down the right side
                (self.board[7] == self.letter and self.board[5] == self.letter and self.board[3] == self.letter) or  # diagonal
                (self.board[9] == self.letter and self.board[5] == self.letter and self.board[1] == self.letter))  # diagonal

    def getPlayerMove(self, player):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(int(move)):
            print("What is " + player + "\'s next move? (1-9)")
            move = input()
        return int(move)

    # Get rid of?
    def getBoardCopy(self):
        # Make a duplicate of the board list and return it the duplicate.
        fakeBoard = []
        for i in self.board:
            fakeBoard.append(i)
        return fakeBoard


class Player_Two(Player):
    def __init__(self, board, letter):
        super().__init__(board, letter)

    # get rid of???
    def chooseRandomMoveFromList(self, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    # GET RID OF?
    def getComputerMove(self, player, boardObject):
        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next mov
        for i in range(1, 10):
            real = self.getBoardCopy()
            if self.isSpaceFree(i):
                self.makeMove(i)
                if self.isWinner():
                    return i
                else:
                    self.board = real
                    player.board = real
                    boardObject.board = real
        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            real = player.getBoardCopy()
            if player.isSpaceFree(i):
                player.makeMove(i)
                if player.isWinner():
                    return i
                else:
                    self.board = real
                    player.board = real
                    boardObject.board = real
        # Try to take one of the corners, if they are free.
        movee = self.chooseRandomMoveFromList([1, 3, 7, 9])
        if movee != None:
            print(player.board)
            print(self.board)
            return movee

        # Try to take the center, if it is free.
        if self.isSpaceFree(5):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList([2, 4, 6, 8])


class Setup:
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')


    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Will player 1 be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']


    def whoGoesFirst(self, thePlayers):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return thePlayers[0]
        else:
            return thePlayers[1]


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    mainBoard = Board(theBoard)
    game = Setup()
    whoPlay = input("Are 1 or 2 players playing?")
    playerLetter, otherLetter = game.inputPlayerLetter()
    if whoPlay == '1':
        turn = game.whoGoesFirst(['player',  'computer'])
        print('The ' + turn + ' will go first.')
        p1 = Player(theBoard, playerLetter)
        c1 = Player_Two(theBoard, otherLetter)
    else:
        turn = 'player 1'
        print('Player 1 will go first.')
        p1 = Player(theBoard, playerLetter)
        p2 = Player(theBoard, otherLetter)
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn.
            mainBoard.drawBoard()
            #move = getComputerMove(theBoard, computerLetter)
            move = p1.getPlayerMove('the player')
            p1.makeMove(move)

            if p1.isWinner():
                mainBoard.drawBoard()
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if mainBoard.isFull():
                    mainBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        elif turn == 'player 1':
            # Player's turn.
            mainBoard.drawBoard()
            #move = getComputerMove(theBoard, computerLetter)
            move = p1.getPlayerMove('player 1')
            p1.makeMove(move)

            if p1.isWinner():
                mainBoard.drawBoard()
                print('Hooray! Player 1 has won the game!')
                gameIsPlaying = False
            else:
                if mainBoard.isFull():
                    mainBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 2'
        elif turn == 'player 2':
            # Player's turn.
            mainBoard.drawBoard()
            # move = getComputerMove(theBoard, computerLetter)
            move = p2.getPlayerMove('player 2')
            p2.makeMove(move)

            if p2.isWinner():
                mainBoard.drawBoard()
                print('Hooray! Player 2 won the game!')
                gameIsPlaying = False
            else:
                if mainBoard.isFull():
                    mainBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 1'

        elif turn == 'computer':
            # Computer's turn.
            move = c1.getComputerMove(p1, mainBoard)
            c1.makeMove(move)

            if c1.isWinner():
                mainBoard.drawBoard()
                print('The computer has beaten you! You lose.')
                gameIsPlaying = False
            else:
                if mainBoard.isFull():
                    mainBoard.drawBoard()
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    if not game.playAgain():
        break



