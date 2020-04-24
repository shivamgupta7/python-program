import matplotlib.pyplot as plt

class programBarchart:

    def bar_chart(self):
        '''
        Display a bar chart of the popularity of programming Languages
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.bar(languages,popularity)
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_1.Popularity of Programming Language.png')
        plt.show()

    def horizontal_bar_chart(self):
        '''
        Display a horizontal bar chart of the popularity of programming Languages
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.barh(languages,popularity)
        plt.ylabel("Languages")
        plt.xlabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_2.Popularity of Programming Language.png')
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Display a bar chart of the popularity of programming Languages
    2.Display a horizontal bar chart of the popularity of programming Languages
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.bar_chart,
            2 : obj.horizontal_bar_chart,
            }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        func()
    except Exception as e:
        print("\n",e)

def main():
    obj = programBarchart()
    switchToFunction(obj)
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()