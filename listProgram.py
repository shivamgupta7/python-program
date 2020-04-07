class programList:

    def sumItems(self):
        '''
        Sum all the items in a list
        '''
        sum_all = 0
        myList = [int(item) for item in input("Enter the items(seprated by space) for sum: ").split()]
        for ele in myList:
            sum_all += ele
        return sum_all

def menu():
    '''
    Menu of programs
    '''
    print('1.Sum all the items in list')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.sumItems(),
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    print(func())

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    obj = programList()
    switchToFunction(choice, obj)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()