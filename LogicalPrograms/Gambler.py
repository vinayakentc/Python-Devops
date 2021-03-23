"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${12:04  p.m}
   * package - ${PACKAGE_NAME}
   * Title - Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of times he/she wins and the number of bets he/she makes. Run the experiment N times, averages the results, and prints them out.
"""

import random

class gambler:
    # Accept Value from user
    def acceptValue(self):
        while True:
            stack = int(input('Enter Stack Money : '))
            if stack > 0:
                break
            else:
                print('You Enter below 0 Value')
        while True:
            goal = int(input('Enter goal : '))
            if goal > 0 and goal > stack:
                break
            else:
                print('You enter value less than 0 or less than stack')
        return stack, goal

    # Check You win or loss
    def reachtheGoalorNot (self):
        value = self.acceptValue()
        stack = value[0]
        goal = value[1]
        numberOfTime = 0
        winCount = 0
        lossCount = 0
        while(stack < goal and stack > 0):
            numberOfTime = numberOfTime + 1
            win = random.randint(0,1)
            if win == 0:
                stack = stack + 1
                winCount = winCount + 1
            else:
                stack = stack - 1
                lossCount = lossCount + 1
            if stack == goal:
                win = 0
            else:
                win = 1
        return win, winCount, lossCount, numberOfTime

    # calculate persentage of win and loss
    def calculatePersentage(self):
        value = self.reachtheGoalorNot()
        win = value[0]
        winCount = value[1]
        lossCount = value[2]
        numberOfTime = value[3]
        winPersentage = winCount / numberOfTime * 100
        lossPersentage = lossCount / numberOfTime * 100
        if win == 0:
            return 'You Reached Goal',winPersentage, lossPersentage
        else:
            return'You Broke', winPersentage, lossPersentage

# main method
if __name__ == '__main__':
    # Exception Handling
    try:
        # creating object
        gamblerObject = gambler()
        # Accepting values from function calculatePersentage
        values = gamblerObject.calculatePersentage()
        massageWinorLoss = values[0]
        winPersentage = values[1]
        lossPersentage = values[2]
        # print result
        print(f'{massageWinorLoss}\nWinning Persentage : {winPersentage}\nloss Persentage : {lossPersentage}')
    except:
        print('Exception Raised.')