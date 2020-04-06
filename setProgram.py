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

def menu():
    print('1.Create a set\n2.Iteration over sets\n3.Add new members\n4.Remove items from set')

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    obj = programSet()
    if choice == 1:
        print(obj.create_set([1,2,3,4]))
    elif choice == 2:
        obj.iterate_set({2,7,6,8,3,5})
    elif choice == 3:
        print(obj.addNewMembers({2,7,6,8,3,5}))
    elif choice == 4:
        print(obj.remove_items({2,5,3,9,7,15,1,8}))
    else:
        print('Please choose correct choice.')
    
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()