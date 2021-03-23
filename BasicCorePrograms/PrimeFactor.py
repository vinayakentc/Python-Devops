"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${11:42 a.m}
   * package - ${PACKAGE_NAME}
   * Title - Print the prime factors of number N.

"""

import math

class factors :

    # method for calculating prime factor
    def calculateFactor(self,userNumber) :
        # print the two and divide by two if remainder is zero
        while userNumber % 2 == 0:
            print ('2'),
            userNumber = userNumber / 2
        # find square root and increment by 2 in range of 3 to squareroot value
        for i in range(3, int(math.sqrt(userNumber)) + 1, 2):
            while userNumber % i == 0:
                print(i)
                userNumber = userNumber / i
        # some time prime factor remaining at last so tat will print
        if userNumber >2 :
            print(int(userNumber))


# main
if __name__ == '__main__' :
    # Exception Handling
    try:
        # accepting Number from User
        userNumber = int(input('Enter a number : '))
        # creating object and pass Parameter
        factorsObject = factors()
        # Calling Method CalculateFactor
        factorsObject.calculateFactor(userNumber)
    except :
        print('Exception Raised.')