# Function to calculate power of 2 upto given range

n = int(input("Enter a number between 0 and 31: "))  # input

def PowerOf2(n):
    if n < 31 and n >= 0:
        for i in range(0, n + 1):  # iterates upto given num
            print(2 ** i)  # prints power upto given num
    else:
        print("Number must between 0 and 31")


if __name__ == '__main__':
    PowerOf2(n)  # Function call
