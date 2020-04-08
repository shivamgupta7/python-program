class programStrings:

    def lenOfStrings(self):
        '''
        Calculate the length of a string
        '''
        string = input('Enter the String : ')
        counts = 0
        for _ in string:
            counts += 1
        return counts

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Calculate the length of a string
    ''')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.lenOfStrings(),
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    print(func())

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    obj = programStrings()
    switchToFunction(choice, obj)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()