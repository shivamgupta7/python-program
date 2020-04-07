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

    def mulItems(self):
        '''
        Multiplies all the items in a list
        '''
        mul_all = 1
        myList = [int(item) for item in input("Enter the items(seprated by space) for multiply: ").split()]
        for ele in myList:
            mul_all *= ele
        return mul_all

    def smallestNumber(self, myList):
        '''
        Get the smallest number from a list
        '''
        small = myList[0]
        for ele in myList:
            if ele < small:
                small = ele
        return small

def menu():
    '''
    Menu of programs
    '''
    print('1.Sum all the items in list\n2.Multiply all the items in list\n3.Get smallest number')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.sumItems(),
        2 : lambda: obj.mulItems(),
        3 : lambda: obj.smallestNumber([8,7,9,2,12,7,6]),
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