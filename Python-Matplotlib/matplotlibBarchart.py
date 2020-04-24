import matplotlib.pyplot as plt
import numpy as np

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
        plt.bar(languages,popularity, color=['r','g','b','y','b','c'])
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_4.diff_color_bar_chart.png')
        plt.show()

    def addTextLabel(self):
        '''
        Display a bar chart of the popularity of programming Languages.
        Attach a text label above each bar displaying its popularity (float value)
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
        plt.bar(languages,popularity, color=['r','g','b','y','b','c'])
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        for index, value in enumerate(popularity):
            plt.text(languages[index], value + 0.5, str(value), color='blue', fontweight='bold')
        plt.ylim(0,30)
        plt.savefig('data/2_5.add_text_label.png')
        plt.show()

    def addEdgeColor(self):
        '''
        Display a bar chart of the popularity of programming Languages. 
        Make blue border to each bar.
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.bar(languages,popularity, color = 'r', edgecolor = 'b')
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_6.add_edge_color.png')
        plt.show()

    def barAtPosition(self):
        '''
        Display a bar chart of the popularity of programming Languages. 
        Specify the position of each bar plot.
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        languages_pos = [0,1,4,7,9,10]
        plt.bar(languages_pos,popularity)
        plt.xticks(languages_pos, languages)
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_7.add_specify_position.png')
        plt.show()

    def specify_width(self):
        '''
        Display a bar chart of the popularity of programming Languages. 
        Select the width of each bar and their positions
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        width = [0.6,0.8,0.5,0.3,0.2,0.1]
        languages_pos = [0,1,4,7,9,10]
        plt.bar(languages_pos,popularity, width=width)
        plt.xticks(languages_pos, languages)
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.savefig('data/2_8.add_specify_width.png')
        plt.show()

    def set_bottom_margin(self):
        '''
        Display a bar chart of the popularity of programming Languages. Increase bottom margin.
        '''
        languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
        popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
        plt.bar(languages,popularity)
        plt.xticks(languages, rotation = 90)
        plt.xlabel("Languages")
        plt.ylabel("Popularity")
        plt.title("Popularity of Programming Language")
        plt.grid()
        plt.subplots_adjust(bottom=0.2)       # plt.tight_layout() also work
        plt.savefig('data/2_9.increase_bottom_margin.png')
        plt.show()
        
    def group_bar_chart(self):
        '''
        Create bar plot of scores by group and gender. Use multiple X
        values on the same chart for men and women
        '''
        # set height of bar
        men_means = (22, 30, 33, 30, 26)
        women_means = (25, 32, 30, 35, 29)
        # Set position of bar on X axis
        index = np.arange(len(men_means))
        barWidth = 0.25
        # Make the plot
        plt.bar(index, men_means, color='r', width=barWidth, label='Men Means')
        plt.bar(index+barWidth, women_means, color='g', width=barWidth, label='Women Means')
        # Add xticks on the middle of the group bars
        plt.xlabel('groups', fontweight='bold')
        plt.ylabel('Means Value', fontweight='bold')
        plt.xticks(index + barWidth, ['G1', 'G2', 'G3', 'G4', 'G5'])
        # Create legend & Show graphic
        plt.legend()
        plt.savefig('data/2_10.group_bar_chart.png')
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
    5.Attach a text label above each bar displaying its popularity
    6.Display a bar chart make blue border to each bar.
    7.Specify the position of each bar plot
    8.Select the width of each bar and their positions
    9.Display a bar chart increase bottom margin.
    10. Use multiple X values on the same chart for men and women
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.bar_chart,
            2 : obj.horizontal_bar_chart,
            3 : obj.uniform_color_bar,
            4 : obj.diff_color_bar,
            5 : obj.addTextLabel,
            6 : obj.addEdgeColor,
            7 : obj.barAtPosition,
            8 : obj.specify_width,
            9 : obj.set_bottom_margin,
            10 : obj.group_bar_chart,
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