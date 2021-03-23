"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${11:49 a.m}
   * package - ${PACKAGE_NAME}
   * Title - Write a program WindChill that takes two double command-line arguments t and v and prints the wind chill.Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the National Weather Service defines the effective temperature (the wind chill)
"""

def WindChill():
    t = float(input("Enter temperature less than 50F"))
    v = float(input("Enter velocity between 3 and 120"))
    # checks the condition weather it is in range or not
    if t > 50 or v > 120 or v < 3:
        print("Formula not valid for this conditions pls enter t<50 and v between 3 and 120")
        return WindChill()
    else:
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
        print("Windchill:", w)


# Driver program
if __name__ == '__main__':
    WindChill()