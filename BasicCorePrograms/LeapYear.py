"""
   * author - ${Vinayak Chavan}
   * date - ${22-03-2021}
   * time - ${11:42 a.m}
   * package - ${PACKAGE_NAME}
   * Title - Print the year is a Leap Year or not.

"""

class leapYear :


                def LeapYearfourdigit():
                    year = (input("Enter a 4 digit year to find leap year or not: "))
                    if len(year) == 4:  # it ensures given year is 4 digit number or not if yes enters loop
                        year = int(year)
                        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # checks the condition for leap year
                            print("Entered year is a leap year")
                        else:
                            print("Enterd year is not a leap year")
                    else:
                        print("Enter a 4 digit year")
                        LeapYearfourdigit()


                if __name__ == '__main__':
                    LeapYearfourdigit()  # function calls
