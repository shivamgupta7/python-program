class programTuple:

    def createTulple(self):
        '''
        Create a tuple
        '''
        myTuple = (int(item) for item in input("Enter the items(seprated by space) for create tuple: ").split())
        return tuple(myTuple)

    def tulpleDifferentDataType(self, data):
        '''
        Create a tuple with different data types
        '''
        myTuple = tuple(data)
        return myTuple

    def unpackTuple(self):
        '''
        Unpack a tuple in several variables
        '''
        myTuple = (int(item) for item in input("Enter the 3 integer(seprated by space) for create tuple: ").split())
        item1, item2, item3 = myTuple
        return item1, item2, item3

def menu():
    '''
    Menu of programs
    '''
    print('''1.Create a tuple\n2.Create a tuple with different data types\n3.Unpack a tuple in several variables''')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.createTulple(),
        2 : lambda: obj.tulpleDifferentDataType(([3,2], False, 3.2, 'Shivam')),
        3 : lambda: obj.unpackTuple(),
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    print(func())

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    obj = programTuple()
    switchToFunction(choice, obj)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()