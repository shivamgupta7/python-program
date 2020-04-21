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
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.listToArray,
            2 : obj.matrix3x3,
            3 : obj.create_update,
            4 : obj.reverse,
            5 : obj.border1_inside0,
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