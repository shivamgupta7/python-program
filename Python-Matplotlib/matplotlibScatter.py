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

    def compare_two_list(self):
        '''
        Draw a scatter plot comparing two subject marks of Mathematics and Science. 
        Use marks of 10 students.
        '''
        math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
        science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
        marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        plt.scatter(marks_range, math_marks, label='Math marks', color='r')
        plt.scatter(marks_range, science_marks, label='Science marks', color='g')
        plt.title('Scatter Plot')
        plt.xlabel('Marks Range')
        plt.ylabel('Marks Scored')
        plt.legend()
        plt.savefig('data/4_3.compare_two_list.png')
        plt.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Scatter graph taking a random distribution in X and Y
    2.Scatter plot with empty circles taking a random distribution in X and Y
    3.Scatter plot using random distributions to generate balls of different sizes
    4.Draw a scatter plot comparing two list
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.scatter_plot,
            2 : obj.scatter_plot_empty_circle,
            3 : obj.diff_size_ball,
            4 : obj.compare_two_list,
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