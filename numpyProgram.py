import numpy as np

class programNumPy:

    def listToArray(self):
        '''
        Convert a list of numeric value into a one-dimensional NumPy array
        '''
        lst = [float(item) for item in input('\nEnter list elements separate by comma: ').split(',')]
        print("\nOriginal List is : ", lst)
        # function to convert list into NumPy array
        arr = np.array(lst)
        print("\n1D NumPy array : ", arr)

    def matrix3x3(self):
        '''
        3x3 matrix with values ranging from 2 to 10
        '''
        matrix = np.arange(2, 11).reshape(3, 3)
        print(matrix)
        return matrix

    def create_update(self):
        '''
        Create a null vector of size 10 and update sixth value to 11.
        '''
        size = int(input('Enter the null vector of size: '))
        vector = np.zeros(size)
        print("Null Vector : ", vector)
        index = int(input('Enter the position where you want to update: '))
        value = int(input('Enter the value: '))
        vector[index-1] = value 
        print("Update {} position value to {} : ".format(index,value), vector)
        return vector

    def reverse(self):
        '''
        Reverse an array (first element becomes last)
        '''
        arr = np.arange(12, 38)
        print("original : ", arr)
        # reverse array
        print("reverse : ", arr[::-1])

    def border1_inside0(self):
        '''
        Create a 2d array with 1 on the border and 0 inside
        '''
        size = int(input('\nEnter the size of 2-d array: '))
        arr = np.ones((size, size))
        print("\nOriginal array : ""\n", arr)
        print("\nArray with 1 on the border and 0 inside")
        # slicing on array
        arr[1:-1, 1:-1] = 0
        print(arr)

    def add_border(self):
        '''
        Add a border (filled with 0's) around an existing array
        '''
        size = int(input('\nEnter the size of 2-d array: '))
        arr = np.ones((size, size))
        print(arr)
        # add border filled with 0's around existing array
        arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
        print(arr)

    def checkerboard_pattern(self):
        '''
        8x8 matrix and fill it with a checkerboard pattern
        '''
        arr = np.zeros((8, 8), dtype=int)
        # fill checkerboard pattern with 1 at every 2 row , 2 col
        # arr[row, col]
        arr[1::2, ::2] = 1     # start wit 1st row 
        # fill checkerboard pattern with 1 at every 2 row, 2 col
        arr[::2, 1::2] = 1    # start with 0th row
        print(arr)

    def convertArray(self):
        '''
        Convert a list and tuple into arrays
        '''
        lst = [1, 2, 3, 4, 5, 6, 7, 8]
        print("List : ", lst)
        # convert any type of input data into array
        print("Array : ", np.asarray(lst))
        tup = ([8, 4, 6], [1, 2, 3])
        print("Tuple : ", tup)
        print("Array : ", np.asarray(tup))

    def appendArray(self):
        '''
        Append values to the end of an array
        '''
        arr = [10, 20, 30]
        print("Original array : ", arr)
        # append values at end of array
        arr = np.append(arr, [[40, 50, 60], [70, 80, 90]])
        print("After append : ", arr)

    def realImgPart(self):
        '''
        Find the real and imaginary parts of an array of complex numbers
        '''
        lst = [ 1.00000000 + 0.j + 0.70710678 + 0.70710678j ]
        arr = np.asarray(lst)
        print("Original array : ", arr)
        print("Real part : ", arr.real)
        print("Imaginary part : ", arr.imag)

    def find_arr_size_bytes(self):
        '''
        Find the number of elements of an array, length of one array element
        in bytes and total bytes consumed by the elements
        '''
        arr = np.array([10, 20, 30, 40, 50], dtype=float)
        # get size of element
        print("\nNumber of element : ", arr.size)
        # get length of element
        print("\nLength of 1 element : ", arr.itemsize)
        # get total bytes consumed by elements of array
        print("\nTotal bytes consumed by elements : ", arr.nbytes)

    def commonValue(self):
        '''
        Find common values between two arrays
        '''
        arr1 = np.array([10, 20, 30, 40, 50])
        print("\nArray 1: ", arr1)
        arr2 = np.array([15, 25, 10, 35, 30])
        print("\nArray 2: ", arr2)
        print("\nCommon values : ", np.intersect1d(arr1, arr2))

    def diffArray(self):
        '''
        Find the set difference of two arrays. The set difference will 
        return the sorted, unique values in array1 that are not in array2.
        '''
        arr1 = np.array([0, 10, 60, 40, 20, 80])
        print("\nArray 1: ", arr1)
        arr2 = np.array([10, 30, 40, 50, 70, 90])
        print("\nArray 2: ", arr2)
        # getting set difference between two arrays
        print("\nSet difference between two arrays: ", np.setdiff1d(arr1, arr2))

    def exclusiveOrArray(self):
        '''
        Find the set exclusive-or of two arrays. Set exclusive-or will return the sorted, 
        unique values that are in only one (not both) of the input arrays.
        '''
        arr1 = np.array([0, 10, 20, 40, 60, 80])
        print("\nArray 1: ", arr1)
        arr2 = np.array([10, 30, 40, 50, 70])
        print("\nArray 2: ", arr2)
        print("\nSet exclusive-or of two arrays : ", np.setxor1d(arr1, arr2))

    def compareArray(self):
        '''
        Compare two arrays using numpy
        '''
        arr1 = np.array([1, 2])
        print("Array 1: ", arr1)
        arr2 = np.array([3, 4])
        print("Array 2: ", arr2)
        print("Array 1 < Array 2   : ", np.less(arr1, arr2))
        print("Array 1 <= Array 2  : ", np.less_equal(arr1, arr2))
        print("Array 1 > Array 2   : ", np.greater(arr1, arr2))
        print("Array 1 >= Arrays 2 : ", np.greater_equal(arr1, arr2))

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Convert a list of numeric value into a one-dimensional NumPy array
    2.3x3 matrix with values ranging from 2 to 10
    3.Create a null vector of size 10 and update sixth value to 11
    4.Reverse an array (first element becomes last)
    5.Create a 2d array with 1 on the border and 0 inside
    6.Add a border (filled with 0's) around an existing array
    7.8x8 matrix and fill it with a checkerboard pattern
    8.Convert a list and tuple into arrays
    9.Append values to the end of an array
    10.Find the real and imaginary parts of an array of complex numbers
    11.Find the number of elements of an array, length of one array element
       in bytes and total bytes consumed by the elements.
    12.Find common values between two arrays
    13.Find the set difference of two arrays
    14.Find the set exclusive-or of two arrays
    15.Compare two arrays using numpy
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.listToArray,
            2 : obj.matrix3x3,
            3 : obj.create_update,
            4 : obj.reverse,
            5 : obj.border1_inside0,
            6 : obj.add_border,
            7 : obj.checkerboard_pattern,
            8 : obj.convertArray,
            9 : obj.appendArray,
            10 : obj.realImgPart,
            11 : obj.find_arr_size_bytes,
            12 : obj.commonValue,
            13 : obj.diffArray,
            14 : obj.exclusiveOrArray,
            15 : obj.compareArray,
            }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        func()
    except Exception as e:
        print("\n",e)

def main():
    obj = programNumPy()
    switchToFunction(obj)
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()