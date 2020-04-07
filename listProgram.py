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

    def count_string(self, words):
        '''
        count the number of strings where the string length is 2 or more and 
        the first and last character are same from a given list of strings.
        '''
        counts = 0
        for word in words:
            if len(word) > 1 and word[0] == word[-1]:
                counts += 1
        return counts

    def sort_listOfTuple(self, myList):
        '''
        Sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
        '''
        length = len(myList)
        for index in range(length):
            flag = 0
            for nextIndex in range(index+1, length):
                if (myList[index][1] > myList[nextIndex][1]):
                    myList[index], myList[nextIndex] = myList[nextIndex], myList[index]
                    flag = 1
            if flag == 0:
                break
        return myList

def menu():
    '''
    Menu of programs
    '''
    print('1.Sum all the items in list\n2.Multiply all the items in list\n3.Get smallest number\n4.Count string which first and last char are same')
    print('5.Sort list of tuple')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.sumItems(),
        2 : lambda: obj.mulItems(),
        3 : lambda: obj.smallestNumber([8,7,9,2,12,7,6]),
        4 : lambda: obj.count_string(['abc', 'xyz', 'aba', '1221']),
        5 : lambda: obj.sort_listOfTuple([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]),  
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