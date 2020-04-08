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

    def charFrequency(self):
        '''
        Count the number of characters (character frequency) in a string
        '''
        string = input('Enter the String : ')
        frequency = {}
        for char in string:
            if char in frequency.keys():
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency

    def changeOccurChar(self):
        '''
        Get a string from a given string where all occurrences of its 
        first char have been changed to '$', except the first char itself.
        '''
        # Strings are unchangeable or immutable
        myString = input('Enter the String : ')
        firstChar = myString[0]
        myString = firstChar + myString[1:].replace(firstChar,'$')
        return myString        

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Calculate the length of a string
    2.Character frequency in a string
    3.Occurrences changed with $
    ''')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.lenOfStrings(),
        2 : lambda: obj.charFrequency(),
        3 : lambda: obj.changeOccurChar()
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