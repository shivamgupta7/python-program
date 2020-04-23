import matplotlib.pyplot as plt
import pandas as pd

class programMatplotlib:

    def drawLine(self):
        '''
        Program to draw a line using given axis values with 
        suitable label in the x axis , y axis and a title
        '''
        x_axis = [0, 1, 2 , 3, 4 ,5]
        y_axis = [0, 1, 4, 9, 16, 25]
        plt.plot(x_axis, y_axis)
        # Set the x axis label of the current axis.
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title 
        plt.title('Sample draw line!')
        # save plot in .png
        plt.savefig('data/1.line_plot.png')
        # Display a figure.
        plt.show()

    def plotUsingTextFile(self):
        '''
        Draw a line using given axis values taken from a text file,
        with suitable label in the x axis, y axis and a title
        '''
        with open("data/test.txt") as txt:
            data = txt.read()
        data = data.split('\n')
        x_axis = [int(row.split(' ')[0]) for row in data]
        y_axis = [int(row.split(' ')[1]) for row in data]
        plt.plot(x_axis, y_axis)
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Sample draw line!')
        plt.savefig('data/2.line_plot_txt.png')
        plt.show()

    def plotUsingCSVFile(self):
        '''
        Draw line charts of the financial data(fdata.csv) of Alphabet Inc. 
        between October 3, 2016 to October 7, 2016.
        '''
        df = pd.read_csv('data/fdata.csv')
        df.plot()
        plt.savefig('data/3.line_plot_csv.png')
        plt.show()

    def addlegends(self):
        '''
        Plot two or more lines on same plot with suitable legends of each line
        '''
        line1_x = [0, 1, 2, 3, 4, 5] 
        line1_y = [0, 1, 4, 9, 16, 25]
        plt.plot(line1_x, line1_y, label = 'Squares')
        line2_x = [0, 1, 2, 3, 4, 5]
        line2_y = [0, 1, 8, 27, 64, 125]
        plt.plot(line2_x, line2_y, label = 'Cubes')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Draw Curve')
        plt.legend()
        plt.savefig('data/4.two_line_plot_legends.png')
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Draw a line using given axis values with suitable label in the x axis, y axis and a title
    2.Draw a line using given axis values taken from a text file
    3.Draw a line using given axis values taken from a CSV file
    4.Plot two or more lines on same plot with suitable legends of each line
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.drawLine,
            2 : obj.plotUsingTextFile,
            3 : obj.plotUsingCSVFile,
            4: obj.addlegends,
            }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        func()
    except Exception as e:
        print("\n",e)

def main():
    obj = programMatplotlib()
    switchToFunction(obj)
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()