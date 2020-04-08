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

    def checkElementExists(self):
        '''
        Check whether an element exists within a tuple
        '''
        myTuple = tuple(int(item) for item in input("Enter the integer elements(seprated by space): ").split())
        element = int(input('Enter the integer which you want to check exists or not :'))
        if element in myTuple:
            return True
        return False

    def listToTuple(self):
        '''
        Convert a list to a tuple
        '''
        myList = [int(item) for item in input("Enter the list of integer elements(seprated by space) : ").split()]
        return tuple(myList)

    def removeItem(self):
        '''
        Remove an item from a tuple
        '''
        myTuple = tuple(int(item) for item in input("Enter the integer elements(seprated by space): ").split())
        element = int(input('Enter the integer which you want to check exists or not :'))
        lst = list(myTuple)    # convert tuple to list  bcz tuple is unchangeable or immutable
        if element in lst:
            lst.remove(element)
        else:
            print('Element not present in tuple')
        return tuple(lst)

    def sliceTuple(self):
        '''
        Slice a tuple
        '''
        myTuple = tuple(int(item) for item in input("Enter the integer elements(seprated by space): ").split())
        start = int(input('Enter the start index where you want to start for slicing :'))
        stop = int(input('Enter the last index where you want to stop for slicing :'))
        sliceList = []    # store the tuple element after slicing
        for index in range(start,stop):       # For tuple slicing also use myTuple[start:stop:step]
            sliceList.append(myTuple[index])
        return tuple(sliceList)

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
    6.Check whether an element exists within a tuple
    7.Convert a list to a tuple
    8.Remove an item from a tuple
    9.Slice a tuple
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
        6 : lambda: obj.checkElementExists(),
        7 : lambda: obj.listToTuple(),
        8 : lambda: obj.removeItem(),
        9 : lambda: obj.sliceTuple(),
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