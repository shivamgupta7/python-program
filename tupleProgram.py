from copy import deepcopy

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

    def colonOfTuple(self):
        '''
        Create the colon of a tuple
        '''
        #create a tuple
        myTuple = ("HELLO", 5, [], True) 
        print("Original tuple",myTuple)
        #make a copy of a tuple using deepcopy() function
        tuple_colon = deepcopy(myTuple)
        tuple_colon[2].append(50)
        print("Copy of original tuple with modified :",tuple_colon)

    def repeatedItems(self):
        '''
        Find the repeated items of a tuple
        '''
        myTuple = tuple(int(item) for item in input("Enter the items(seprated by space) for find repeated items: ").split())
        repeat_ele = [] # create a tuple for storing repeated items
        flag = False
        for ele in myTuple:
            # To check if Duplicate exist 
            if ele in repeat_ele:
                flag = True
                continue
            else:
                countRepeatedEle = 0
                for item in myTuple: 
                    if ele == item:
                        countRepeatedEle += 1
                # To print count if Duplicate of element exist
                if(countRepeatedEle > 1):  
                    print('{0} repeated {1} times.'.format(ele, countRepeatedEle)) 
                    repeat_ele.append(ele)
        if flag == False: 
            print("No Duplicates")
        return repeat_ele

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Create a tuple
    2.Create a tuple with different data types
    3.Unpack a tuple in several variables
    4.Create the colon of a tuple
    5.Find the repeated items of a tuple
    ''')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.createTulple(),
        2 : lambda: obj.tulpleDifferentDataType(([3,2], False, 3.2, 'Shivam')),
        3 : lambda: obj.unpackTuple(),
        4 : lambda: obj.colonOfTuple(),
        5 : lambda: obj.repeatedItems(),
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