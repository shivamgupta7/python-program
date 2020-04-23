import matplotlib.pyplot as plt

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

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Draw a line using given axis values with suitable label in the x axis, y axis and a title
    2.Draw a line using given axis values taken from a text file
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.drawLine,
            2 : obj.plotUsingTextFile,
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