"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${12:04  p.m}
   * package - ${PACKAGE_NAME}
   * Title - Write a Program to play a Cross Game or Tic-Tac-Toe Game. Player 1 is the Computer and the Player 2 is the user. Player 1 take Random Cell that is the Column and Row..
"""

import random

class tictactoe :

    # constructor for game board
    def __init__(self):
        self.board = {'7':' ','8':' ','9':' ',
                      '4':' ','5':' ','6':' ',
                      '1':' ','2':' ','3':' '}
        self.playerTurn = ''

    # print game board
    def printBoard(self):
        print(self.board['7']+ '|' +self.board['8'] + '|' +self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' +self.board['5'] + '|' +self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' +self.board['2'] + '|' +self.board['3'])

    # Toss function for who's turn is first
    def toss(self):
        self.playerTurn = random.randint(0,1)
        if self.playerTurn:
            self.playerTurn = 'X'
            print('Computer Win toss\nYou have O\nComputer have X')
        else:
            self.playerTurn = 'O'
            print('you win toss\nYou have O\nComputer have X')
        return self.playerTurn

    # logic tic-tac-toe program
    def gameStart(self):
        self.playerTurn = self.toss()
        self.playerTurnCount = 0

        while self.playerTurnCount < 9:
            self.printBoard()

            # who one is play computer or you
            if self.playerTurn == 'X' :
                print('its computer ' + self.playerTurn + ' Turn\nMove to which place?')
                computerMove = random.randint(1,9)
                move = str(computerMove)
            else:
                print('its your ' + self.playerTurn + ' Turn\nMove to which place?')
                move = input()

            # accepting value from computer or player and insert
            if self.board[move] == ' ':
                self.board[move] = self.playerTurn
                self.playerTurnCount += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # check wining condition
            if self.playerTurnCount >= 5:
                # across the top
                if self.board['7'] == self.board['8'] == self.board['9'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                # across the middle
                elif self.board['4'] == self.board['5'] == self.board['6'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                # across the bottom
                elif self.board['1'] == self.board['2'] == self.board['3'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                # down the left side
                elif self.board['1'] == self.board['4'] == self.board['7'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                # down the middle
                elif self.board['2'] == self.board['5'] == self.board['8'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                # down the right side
                elif self.board['3'] == self.board['6'] == self.board['9'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                # diagonal
                elif self.board['7'] == self.board['5'] == self.board['3'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break
                # diagonal
                elif self.board['1'] == self.board['5'] == self.board['9'] != ' ':
                    self.printBoard()
                    print("\nGame Over.\n")
                    print("**** " + self.playerTurn + " won. ****")
                    break

            # check game tie condition
            if self.playerTurnCount == 9:
                print("\nGame Over.\n")
                print("It's a Tie!!")
                self.printBoard()

            # change player turn
            if self.playerTurn == 'X':
                self.playerTurn = 'O'
            else:
                self.playerTurn = 'X'

# main method
if __name__ == '__main__' :
    # Exception Handling
    try :
        tictactoeObject = tictactoe()
        tictactoeObject.gameStart()
    except :
        print('Exception Raised.')