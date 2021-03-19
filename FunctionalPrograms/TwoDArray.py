# functions for twod array for reading int, double and bool type
def TwoDArray(rows, cols):
    # created an array with row * col size
    Multi_Datatype_Array = [[0 for i in range(cols)] for j in range(rows)]

    # initialising array with int,double and bool type dynamically
    for i in range(rows):
        for j in range(cols):
            Multi_Datatype_Array[i][j] = float(input("Enter float value:"))
            j = j + 1
            Multi_Datatype_Array[i][j] = int(input("Enter int value"))
            j = j + 1
            Multi_Datatype_Array[i][j] = bool(input("Enter bool value"))
            break
    # prints the two dimensional array
    for i in range(rows):
        for j in range(cols):
            print(Multi_Datatype_Array[i][j],end=' ')
            # print(type(arr[i][j]))
        print()

if __name__ == '__main__':
    TwoDArray(3, 3)
