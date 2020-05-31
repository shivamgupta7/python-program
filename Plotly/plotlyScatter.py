import plotly.graph_objects as go
from numpy.random import randn
import numpy as np
import pandas as pd

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

    def line_plot(self):
        '''
        Draw line and scatter plots for random 100 x and y coordinates
        '''
        point = 100
        random_x = np.linspace(0, 1, point)
        random_y0 = randn(point) + 5
        random_y1 = randn(point)
        random_y2 = randn(point) - 5
        fig = go.Figure()
        # Add traces
        fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                            mode='markers',
                            name='markers'))
        fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                            mode='lines+markers',
                            name='lines+markers'))
        fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                            mode='lines',
                            name='lines'))
        fig.update_layout(
            title="Line and scatter plots",
            xaxis_title="x Axis",
            yaxis_title="y Axis",
            font=dict(family="Courier New, monospace",size=18,)
        )
        fig.write_image("images/fig2.png")
        fig.show()

    def style_scatter(self):
        '''
        Draw a scatter plot for random 500 x and y coordinates and style it
        '''
        fig = go.Figure(data=go.Scatter(
            x = randn(500),
            y = randn(500),
            mode='markers',
            marker=dict(
                size=16,
                color=randn(500), #set color equal to a variable
                colorscale='Viridis', # one of plotly colorscales
                showscale=True)))
        fig.update_layout(
            title="scatter plots with stlying",
            xaxis_title="x Axis",
            yaxis_title="y Axis",
            font=dict(family="Courier New, monospace",size=18,)
        )
        fig.write_image("images/fig3.png")
        fig.show()

    def plotUsingDataFrame(self):
        '''
        Draw a scatter plot for a given dataset and show datalabels on hover
        https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv
        '''
        data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv')
        fig = go.Figure(data=go.Scatter(x=data['Postal'],
                                y=data['Population'],
                                mode='markers',
                                marker_color=data['Population'],
                                text=data['State']))
        fig.update_layout(
            title="Population of USA States",
            xaxis_title="States",
            yaxis_title="Populations",
            font=dict(
                family="Courier New, monospace",
                size=18,
            ))
        fig.write_image("images/fig4.png")
        fig.show()

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Draw a scatter plot for random 1000 x and y coordinates
    2.Draw line and scatter plots for random 100 x and y coordinates
    3.Draw a scatter plot for random 500 x and y coordinates and style it
    4.Draw a scatter plot for a given dataset and show datalabels on hover
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : lambda: obj.scatter_plot(x=randn(1000),y=randn(1000),title='Scatter plot for random 1000 x and y coordinates'),
            2 : obj.line_plot,
            3 : obj.style_scatter,
            4 : obj.plotUsingDataFrame,
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