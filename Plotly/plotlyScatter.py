import plotly.graph_objects as go
from numpy.random import randn

class programPlotly:

    def scatter_plot(self, **kwargs):
        '''
        Draw a scatter plot
        '''
        fig = go.Figure(data=go.Scatter(x=kwargs['x'], y=kwargs['y'],mode='markers'))
        fig.update_layout(
            title=kwargs['title'],
            xaxis_title="x Axis",
            yaxis_title="y Axis",
            font=dict(family="Courier New, monospace",size=15,)
        )
        fig.write_image("images/fig1.png")
        fig.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Draw a scatter plot for random 1000 x and y coordinates
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : lambda: obj.scatter_plot(x=randn(1000),y=randn(1000),title='Scatter plot for random 1000 x and y coordinates'),
        }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        func()
    except Exception as e:
        print("\n",e)

def main():
    obj = programPlotly()
    switchToFunction(obj)
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()