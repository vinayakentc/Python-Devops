
"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${11:42 a.m}
   * package - ${PACKAGE_NAME}
   * Title - This program takes a command-line argument N and prints a table of the powers of 2 that are less than or equal to 2^N.

"""

class powerOf2:

    # Check the range in between 0 <= Number < 31
    def checkUserNumber(self):
        while True:
            # accepting Number from User
            userNumber = int(input('Enter the value you want print table : '))
            if 0 <= userNumber < 31 :
                # Calling Method PowerTable
                self.powerTable(userNumber)
                break
            else:
                print('Overflows int / Out of range\nEnter again 0 to less than 31')

    # Print Power of 2 table
    def powerTable(self, userNumber):
        for i in range(userNumber+1):
            # pow(2,3) = (2*2*2) its power function
            power = pow(2,i)
            print(f'2^{i} =',power)


# Main Method
if __name__ == '__main__':
    while True:
        # Exception Handling
        try:
            # creating object and pass Parameter
            powerOf2Object = powerOf2()
            # Calling Method CheckUserNumber
            powerOf2Object.checkUserNumber()
            break
        except ValueError:
            print('You enter str must enter int value')