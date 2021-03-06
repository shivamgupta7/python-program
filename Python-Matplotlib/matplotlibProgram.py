import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime as dt

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

    def diffColorWidth(self):
        '''
        Plot two or more lines with legends, different widths and colors
        '''
        line1_x = [0, 1, 2, 3, 4, 5] 
        line1_y = [0, 1, 4, 9, 16, 25]
        line2_x = [0, 1, 2, 3, 4, 5]
        line2_y = [0, 1, 8, 27, 64, 125]
        plt.title('Two or more lines with different widths and colors with suitable legends ')
        # Display the figure.
        plt.plot(line1_x, line1_y, color='blue', linewidth = 3,  label = 'Squares-width-3')
        plt.plot(line2_x, line2_y, color='red', linewidth = 5,  label = 'Cube-width-5')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()
        plt.savefig('data/5.two_line_diff_width.png')
        plt.show()

    def diffStyle(self):
        '''
        Plot two or more lines with different styles
        '''
        line1_x = [0, 1, 2, 3, 4, 5] 
        line1_y = [0, 1, 4, 9, 16, 25]
        line2_x = [0, 1, 2, 3, 4, 5]
        line2_y = [0, 1, 8, 27, 64, 125]
        plt.title('Two or more lines with different widths and colors with suitable legends ')
        # Display the figure.
        plt.plot(line1_x, line1_y, linestyle = '--',  label = 'Squares-width-3')
        plt.plot(line2_x, line2_y, linestyle = ':',  label = 'Cube-width-5')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()
        plt.savefig('data/6.two_line_diff_style.png')
        plt.show()

    def setmarker(self):
        '''
        Plot two or more lines and set the line markers
        '''
        line1_x = [0, 1, 2, 3, 4, 5] 
        line1_y = [0, 1, 4, 9, 16, 25]
        line2_x = [0, 1, 2, 3, 4, 5]
        line2_y = [0, 1, 8, 27, 64, 125]
        plt.title('Two or more lines with different widths and colors with suitable legends ')
        # Display the figure.
        plt.plot(line1_x, line1_y, marker = '*',  label = 'Squares-width-3')
        plt.plot(line2_x, line2_y, marker = 'o',  label = 'Cube-width-5')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend()
        plt.savefig('data/7.two_line_diff_marker.png')
        plt.show()

    def setaxis(self):
        '''
        Display the current axis limits values and set new axis values
        '''
        x_axis = [0, 1, 2 , 3, 4 ,5]
        y_axis = [0, 1, 4, 9, 16, 25]
        plt.plot(x_axis, y_axis, label = 'Squares')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Sample draw line!')
        plt.savefig('data/8.line_plot_set_axis.png')
        plt.axis([0,10,0,40])
        plt.legend()
        plt.show()

    def quantitiesPlot(self):
        '''
        Plot quantities which have an x and y position
        '''
        line1_x = [0, 1, 2, 3, 4, 5] 
        line1_y = [0, 1, 4, 9, 16, 25]
        line2_x = [0, 1, 2, 3, 4, 5]
        line2_y = [0, 1, 8, 27, 64, 125]
        plt.title('Draw Curve')
        # Display the figure.
        plt.plot(line1_x,line1_y, 'g^', line2_x, line2_y, 'rs')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.legend(['Squres', 'Cubes'])
        plt.savefig('data/9.two_line_diff_quantities.png')
        plt.show()

    def allDiffStyleLine(self):
        '''
        Plot several lines with different format styles in one command using arrays
        '''
        point = np.arange(0., 5., 0.2)
        # green dashes, blue squares and red triangles
        plt.plot(point, point, 'g--', point, point**2, 'bs', point, point**3, 'r^')
        plt.xlabel('x - axis')
        plt.ylabel('y - axis')
        plt.title('Draw Curve')
        plt.legend(['Straight line', 'Squres', 'Cubes'])
        plt.savefig('data/10.lines_diff_styles.png')
        plt.show()

    def plotChart(self):
        '''
        Create multiple types of charts (a simple curve and plot some quantities) 
        on a single set of axes
        '''
        data = [(dt.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (dt.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (dt.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (dt.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (dt.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]
        x_axis = [date for (date, value) in data]
        y_axis = [value for (date, value) in data]
        _ ,ax = plt.subplots(figsize=(15,7))
        # Plot the data as a red line with round markers
        plt.plot(x_axis,y_axis,'r-o')
        # Set the xtick locations
        ax.set_xticks(x_axis)
        plt.savefig('data/11.chat_plot.png')
        plt.show()

    def plotGridChart(self):
        '''
        Display grid and draw line charts of the closing value of Alphabet Inc. between October 3,
        2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue
        '''
        data = [(dt.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
        (dt.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
        (dt.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
        (dt.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
        (dt.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]
        x_axis = [date for (date, value) in data]
        y_axis = [value for (date, value) in data]
        _ ,ax = plt.subplots(figsize=(15,7))
        # Plot the data as a red line with round markers
        plt.plot(x_axis,y_axis,'r-o')
        # Set the xtick locations
        ax.set_xticks(x_axis)
        plt.savefig('data/12.grid_chart_plot.png')
        plt.grid(linestyle='-', linewidth='0.5', color='blue')
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
    5.Plot two or more lines with legends, different widths and colors
    6.Plot two or more lines with different styles
    7.Plot two or more lines and set the line markers
    8.Display the current axis limits values and set new axis values
    9.Plot quantities which have an x and y position
    10.Plot several lines with different format styles in one command using arrays
    11.Create multiple types of charts on a single set of axes
    12.Display grid and draw line charts. Customized the grid lines with linestyle -, width .5. and color blue
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.drawLine,
            2 : obj.plotUsingTextFile,
            3 : obj.plotUsingCSVFile,
            4 : obj.addlegends,
            5 : obj.diffColorWidth,
            6 : obj.diffStyle,
            7 : obj.setmarker,
            8 : obj.setaxis,
            9 : obj.quantitiesPlot,
            10 : obj.allDiffStyleLine,
            11 : obj.plotChart,
            12 : obj.plotGridChart,
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