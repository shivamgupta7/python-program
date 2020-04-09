from listProgram import programList
import textwrap

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

    def changeString(self):
        '''
        Add 'ing' at the end of a given string (length should be at least 3). 
        If the given string already ends with 'ing' then add 'ly' instead. 
        If the string length of the given string is less than 3, leave it unchanged.
        '''
        string = input('Enter the String : ')
        if len(string) > 2:
            if string[-3:] == 'ing':
                string += 'ly'
            else:
                string += 'ing'
        return string

    def findLongestWord(self):
        '''
        Takes a list of words and returns the length of the longest one.
        '''
        wordsList = input('Enter words separated by space : ').split()
        word_len = []       # store length and words for each word
        for word in wordsList:
            word_len.append((len(word), word))     # store tuple of list
        word_len = programList.bubbleSort(word_len)
        return word_len[-1][1]

    def changeUpperAndLowerCase(self):
        '''
        Takes input from the user and displays that input back in upper and lower cases
        '''
        string = input('Enter words for convert to upper and lower case : ')
        upperCase = string.upper()
        lowerCase = string.lower()
        return upperCase, lowerCase

    def findUniqueWords(self):
        '''
        Accepts a comma separated sequence of words as input and 
        prints the unique words in sorted form (alphanumerically)
        '''
        words = tuple(input('Enter words separated by comma : ').split(','))
        uniqueWords = []     # store all unique words in list
        for word in words:
            if word not in uniqueWords:
                uniqueWords.append(word)
        uniqueWords = programList.bubbleSort(uniqueWords)
        return uniqueWords

    def formattedText(self):
        '''
        Display formatted text (width=50) as output
        '''
        string = input('Enter the String : ')
        formatingString = textwrap.fill(string, width=50)
        return formatingString

    def reverseString(self):
        '''
        Reverse a string
        ''' 
        string = input('Enter the String : ')
        reverse_str = "" 
        for char in string: 
            reverse_str = char + reverse_str
        return reverse_str

    def first_n_charLower(self):
        '''
        Lowercase first n characters in a string
        '''
        string = input('Enter the string : ')
        num = int(input('Enter how many first n characters in lower case : '))
        lower_str = ""
        for index in range(num):
            lower_str += string[index].lower()
        new_string = lower_str + string[num:]
        return new_string

    def occurSubstring(self):
        '''
        Count occurrences of a substring in a string
        '''
        string = input('Enter the string : ')
        pattern = input('Enter the substring for counting : ')
        str_len = len(string)
        pat_len = len(pattern)
        counts = 0
        #  A loop to slide pat[] one by one
        for index in range(str_len - pat_len + 1):
            # For current index, check for pattern match
            pindex = 0    # pattern index
            for pindex in range(pat_len):
                if (string[index + pindex] != pattern[pindex]):
                    break
            if (pindex == pat_len-1):      # check index of pattern is equal to length of pattern -1
                counts += 1
                pindex = 0
        return counts

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Calculate the length of a string
    2.Character frequency in a string
    3.Occurrences changed with $
    4.Add 'ing' or 'ly' at the end 
    5.Returns the longest word in list
    6.Convert string to upper and lower cases
    7.Find unique words in sorted order
    8.Display formatted text (width=50) as output
    9.Reverse a string
    10.Lowercase first n characters in a string
    11.Count occurrences of a substring in a string
    ''')

def switchToFunction(case, obj):
    '''
    Create switch function to move perticular program
    '''
    switcher = {
        1 : lambda: obj.lenOfStrings(),
        2 : lambda: obj.charFrequency(),
        3 : lambda: obj.changeOccurChar(),
        4 : lambda: obj.changeString(),
        5 : lambda: obj.findLongestWord(),
        6 : lambda: obj.changeUpperAndLowerCase(),
        7 : lambda: obj.findUniqueWords(),
        8 : lambda: obj.formattedText(),
        9 : lambda: obj.reverseString(),
        10 : lambda : obj.first_n_charLower(),
        11 : lambda : obj.occurSubstring()
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