import matplotlib.pyplot as plt

class programMatplotlib:

    def drawLine(self):
        '''
        Program to draw a line using given axis values with 
        suitable label in the x axis , y axis and a title
        '''
        x = [0, 1, 2 , 3, 4 ,5]
        y = [0, 1, 4, 9, 16, 25]
        plt.plot(x, y)
        # Set the x axis label of the current axis.
        plt.xlabel('x - axis')
        # Set the y axis label of the current axis.
        plt.ylabel('y - axis')
        # Set a title 
        plt.title('Sample draw line!')
        # save plot in .png
        plt.savefig('data/line_plot.png')
        # Display a figure.
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.draw a line using given axis values with suitable label in the x axis, y axis and a title
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.drawLine,
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