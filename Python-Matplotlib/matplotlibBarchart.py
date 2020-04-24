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

    def uniform_color_bar(self):
        '''
        Display a bar chart of the popularity of programming Languages. Use uniform color.
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.bar(languages,popularity, color=(0.1, 0.2, 0.3, 1.0))    # color = (r,g,b,transparency)
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_3.uniform_color_bar_chart.png')
        plt.show()

    def diff_color_bar(self):
        '''
        Display a bar chart of the popularity of programming Languages. 
        Use different color for each bar.
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.bar(languages,popularity, color=['r','g','b','y','b','c'])    # color = (r,g,b,transparency)
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_4.diff_color_bar_chart.png')
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Display a bar chart of the popularity of programming Languages
    2.Display a horizontal bar chart of the popularity of programming Languages
    3.Display a bar chart of the popularity of programming Languages. Use uniform color.
    4.Display a bar chart use different color for each bar.
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.bar_chart,
            2 : obj.horizontal_bar_chart,
            3 : obj.uniform_color_bar,
            4 : obj.diff_color_bar,
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