class programSet:

    def create_set(self,data):
        '''
        Create a set
        '''
        self.new_set = set(data)
        return self.new_set

    def iterate_set(self,set_data):
        '''
        Iteration over sets
        '''
        for item in set_data:
            print(item)

    def addNewMembers(self, mySet):
        '''
        Add member(s) in a set
        '''
        self.members = [int(item) for item in input("Enter the new members(one or more seprated by space) which you want to add: ").split()]
        mySet.update(self.members)
        return mySet

    def remove_items(self, mySet):
        '''
        Remove items from set
        '''
        print("My set is: ", mySet)
        times = int(input('How many items you want to remove? : '))
        for time in range(times):
            item = int(input('Enter {0} item which one you want to delete : '.format(time+1)))
            mySet.discard(item)        # If the item to remove does not exist, discard() will NOT raise an error.
        return mySet

    def intersectionOfSet(self, mySet):
        '''
        Create an intersection of sets
        '''
        print("My set is : ",mySet)
        mySet_copy = mySet.copy()
        times = int(input('How many set you want to intersect? : '))
        for time in range(times):
            input_set = set([int(item) for item in input("Enter the {0} set elements (one or more seprated by space): ".format(time+1)).split()])
            result = mySet_copy.intersection(input_set)
            mySet_copy = result
        return result

    def unionOfSet(self, mySet):
        '''
        Create a union of sets
        '''
        print("My set is : ",mySet)
        mySet_copy = mySet.copy()
        times = int(input('How many set you want to union? : '))
        for time in range(times):
            input_set = set([int(item) for item in input("Enter the {0} set elements (one or more seprated by space): ".format(time+1)).split()])
            result = mySet_copy.union(input_set)
            mySet_copy = result
        return result

    def differenceOfSets(self, mySet):
        '''
        Create set difference
        '''
        print("My set is : ",mySet)
        mySet_copy = mySet.copy()
        times = int(input('How many set you want to difference? : '))
        for time in range(times):
            input_set = set([int(item) for item in input("Enter the {0} set elements (one or more seprated by space): ".format(time+1)).split()])
            result = mySet_copy.difference(input_set)
            mySet_copy = result
        return result
        
    def symmentricDifferenceOfSets(self, mySet):
        '''
        Create a symmetric difference
        '''
        print("My set is : ",mySet)
        mySet_copy = mySet.copy()
        times = int(input('How many set you want to symmentric difference? : '))
        for time in range(times):
            input_set = set([int(item) for item in input("Enter the {0} set elements (one or more seprated by space): ".format(time+1)).split()])
            result = mySet_copy.symmetric_difference(input_set)
            mySet_copy = result
        return result

def menu():
    '''
    Menu of programs
    '''
    print('1.Create a set\n2.Iteration over sets\n3.Add new members\n4.Remove items from set\n5.Create an intersection of set')
    print ('6.Create a union of set\n7.Create set difference\n8.Create a symmetric difference')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.create_set([1,2,3,4]),
        2 : lambda: obj.iterate_set({2,7,6,8,3,5}),
        3 : lambda: obj.addNewMembers({2,7,6,8,3,5}),
        4 : lambda: obj.remove_items({2,5,3,9,7,15,1,8}),
        5 : lambda: obj.intersectionOfSet({2,7,6,8,3,5}),
        6 : lambda: obj.unionOfSet({2,7,6,8,3}),
        7 : lambda: obj.differenceOfSets({2,5,3,9,7,15,1,8}),
        8 : lambda: obj.symmentricDifferenceOfSets({2,5,3,9,7})
    }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    print(func())

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    obj = programSet()
    switchToFunction(choice, obj)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()