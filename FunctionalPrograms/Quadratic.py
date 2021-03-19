from cmath import sqrt


# function for Quadratic equation
def Quadratic():
    a = float(input("Enter a value"))
    b = float(input("Enter b value"))
    c = float(input("Enter c value"))
    if a == 0 or (b == 0 and c == 0):
        print("1. a cant be zero or \n2. b and c cant be zero: enter num greater than 0")
        return Quadratic()
    # finding delta using formula
    delta = b * b - 4 * a * c

    # finding roots of the equation
    root1 = (-b + sqrt(delta)) / (2 * a)
    root2 = (-b - sqrt(delta)) / (2 * a)
    print(" root1:", root1, "\n", "root2:", root2)


# Driver program
if __name__ == '__main__':
    Quadratic()