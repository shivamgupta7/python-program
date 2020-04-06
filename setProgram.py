class programSet:

    def create_set(self,data):
        '''
        Create a set
        '''
        self.new_set = set(data)
        return self.new_set

def menu():
    print('1.Create a set')

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    obj = programSet()
    if choice == 1:
        print(obj.create_set([1,2,3,4]))
    else:
        print('Please choose correct choice.')
    
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()