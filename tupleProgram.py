class programTuple:

    def createTulple(self):
        '''
        Create a tuple
        '''
        myTuple = (int(item) for item in input("Enter the items(seprated by space) for create tuple: ").split())
        return tuple(myTuple)

def menu():
    '''
    Menu of programs
    '''
    print('''1.Create a tuple''')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.createTulple(),
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