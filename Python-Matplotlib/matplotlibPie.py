import matplotlib.pyplot as plt

class programPiechart:

    def pie_chart(self):
        '''
        Create a pie chart of the popularity of programming Languages
        '''
        languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
        popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        colors = ["r", "g", "y", "b", "m", "c"]
        plt.pie(popuratity, labels=languages, colors=colors,autopct='%.1f%%')
        plt.title("Popularity of Programming Language")
        plt.savefig('data/3_1.pie_chart.png')
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Create a pie chart of the popularity of programming Languages
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.pie_chart,
            }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        func()
    except Exception as e:
        print("\n",e)

def main():
    obj = programPiechart()
    switchToFunction(obj)
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()