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

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Convert a list of numeric value into a one-dimensional NumPy array
    ''')
    choice = int(input('Enter which program you want to run: '))
    switcher = {
        1 : obj.listToArray
        }
    func = switcher.get(choice, 'Invalid choice please select correct options.')
    func()

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