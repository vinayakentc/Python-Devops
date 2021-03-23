"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${11:40 a.m}
   * package - ${PACKAGE_NAME}
   * Title - Flip Coin and print percentage of Heads and Tails

"""
import random

heads = 0
tails = 0
heads_percent = 0
tails_percent = 0
n = int(input("Enter the times you want to Flip Coin: "))
if n >= 0:
    for i in range(n):  # run loop n times
        coin = random.random()  # assign a value to coin either 0 or 1
        if coin < 0.5:  # if coin value is assigned as 0
            heads += 1  # increment heads
        else:  # if coin value is assigned as 1
            tails += 1  # increment tails

        try:
            heads_percent = ((heads / (heads + tails)) * 100)
            tails_percent = ((tails / (heads + tails)) * 100)
        except ZeroDivisionError:
            print("Exception occured ", ZeroDivisionError)

    print("Heads percent: " + str(heads_percent))
    print("Tails percent: " + str(tails_percent))  # converting numbers to string using str()
else:
    print("Enter the positive Number:")