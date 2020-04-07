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
        myList = [int(item) for item in input("Enter the items(separated by space) for multiply: ").split()]
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

    def copyList(self, myList):
        '''
        Clone or copy a list
        '''
        new_list = myList.copy()
        return new_list

    def longerWords(self):
        '''
        Find the list of words that are longer than n from a given list of words
        '''
        string = input('Enter the string : ')
        number = int(input('Enter the number for find words larger then this number : '))
        wordsOfList = []
        text = string.split(" ")
        for word in text:
            if len(word) > number:
                wordsOfList.append(word)
        return wordsOfList

    def checkCommonDataInTwoList(self):
        '''
        Takes two lists and returns True if they have at least one common member
        '''
        result = False
        list1 = input('Enter list1 elements separate by space: ').split()
        list2 = input('Enter list2 elements separate by space: ').split()
        for ele1 in list1:
            for ele2 in list2:
                if ele1 == ele2:
                    result = True
        return result

    def removeDuplicates(self):
        '''
        Remove duplicates from a list
        '''
        myList = [int(item) for item in input("Enter the items(separated by space): ").split()]
        new_list = []
        for num in myList:
            if num not in new_list:
                new_list.append(num)
        return new_list

    def printSpecifiedList(self):
        '''
        Print a specified list after removing the 0th, 4th and 5th elements
        '''
        myList = input("Enter the items(separated by space): ").split()
        new_list = []
        for index,value in enumerate(myList):
            if index not in [0, 4, 5]:
                new_list.append(value)
        return new_list

def menu():
    '''
    Menu of programs
    '''
    print('1.Sum all the items in list\n2.Multiply all the items in list\n3.Get smallest number\n4.Count string which first and last char are same')
    print('5.Sort list of tuple\n6.Clone or copy a list\n7.Given list of words which longer then given number\n8.Check common members in two list')
    print('9.Remove duplicates from a list\n10.Removing the 0th, 4th and 5th elements')

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
        6 : lambda: obj.copyList([5,4,3,2,9]),
        7 : lambda: obj.longerWords(),
        8 : lambda: obj.checkCommonDataInTwoList(),
        9 : lambda: obj.removeDuplicates(),
        10 : lambda: obj.printSpecifiedList()
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