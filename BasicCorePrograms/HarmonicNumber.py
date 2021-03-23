
"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${11:42 a.m}
   * package - ${PACKAGE_NAME}
   * Title - Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

"""

class harmonicNumber :

    # constructor
    def __init__(self, userNumber):
        self.userNumber = userNumber

    # Harmonic Value Calculater
    def harmonicValue(self):
        sum = 0
        for i in range(1,(self.userNumber+1)):
            div = 1/i
            sum = sum + div
        print(sum)


# Main Method
if __name__ == '__main__' :
    # Exception Handling
    while True:
        try:
            # accepting Number from User
            while True:
                userNumber = int(input('Enter the number upto you want to print harmonic value :'))
                if userNumber > 0:
                    break
                else:
                    print('You enter value less than 0 ')
            # creating object and pass Parameter
            harmonicNumberObject = harmonicNumber(userNumber)
            # Calling Method HarmonicValue
            harmonicNumberObject.harmonicValue()
            break
        except ValueError:
            print('You enter str must enter int value')
