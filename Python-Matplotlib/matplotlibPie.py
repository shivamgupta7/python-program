import matplotlib.pyplot as plt
import pandas as pd

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

    def pieChartUsingCSV(self):
        '''
        create a pie chart of gold medal achievements of five most successful 
        countries in 2016 Summer Olympics. Read the data from a csv file.
        '''
        df = pd.read_csv('data/medal.csv')
        colors = ["r", "g", "y", "b", "m"]
        plt.pie(df['gold_medal'],labels=df['country'], colors=colors, autopct='%1.1f%%')
        plt.title("Five most successful countries in 2016 Summer Olympics")
        plt.savefig('data/3_2.gold_medal.png')
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Create a pie chart of the popularity of programming Languages
    2.Read the data from a csv file and create pie chart.
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.pie_chart,
            2 : obj.pieChartUsingCSV
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