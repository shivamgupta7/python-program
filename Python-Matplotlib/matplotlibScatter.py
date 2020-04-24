import matplotlib.pyplot as plt
from pylab import randn
import random
import math

class programScatterplot:

    def scatter_plot(self):
        '''
        Draw a scatter graph taking a random distribution in X and Y and
        plotted against each other
        '''
        x_axis = randn(20)    # random
        y_axis = randn(20)
        plt.scatter(x_axis,y_axis, color='r')
        plt.title('Random distribution in X and Y')
        plt.xlabel("X-axis")
        plt.ylabel("Y_axis")
        plt.savefig('data/4_1.scatter_plot.png')
        plt.show()

    def scatter_plot_empty_circle(self):
        '''
        Draw a scatter plot with empty circles taking a random distribution
        in X and Y and plotted against each other
        '''
        x_axis = randn(20)    # random
        y_axis = randn(20)
        plt.scatter(x_axis,y_axis, facecolors='none', edgecolors='r')
        plt.title('Random distribution in X and Y')
        plt.xlabel("X-axis")
        plt.ylabel("Y_axis")
        plt.savefig('data/4_1.scatter_plot.png')
        plt.show()

    def diff_size_ball(self):
        '''
        Draw a scatter plot using random distributions to generate balls of
        different sizes.
        '''
        x_axis = [random.random() for _ in range(10)]
        y_axis = [random.random() for _ in range(10)]
        colors = [random.randint(1, 10) for i in range(10)]
        areas = [math.pi * random.randint(5, 15)**2 for i in range(10)]
        plt.scatter(x_axis, y_axis, s = areas, c = colors)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.savefig('data/4_2.diff_size_ball.png')
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Scatter graph taking a random distribution in X and Y
    2.Scatter plot with empty circles taking a random distribution in X and Y
    3.Scatter plot using random distributions to generate balls of different sizes
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.scatter_plot,
            2 : obj.scatter_plot_empty_circle,
            3 : obj.diff_size_ball,
            }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        func()
    except Exception as e:
        print("\n",e)

def main():
    obj = programScatterplot()
    switchToFunction(obj)
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()