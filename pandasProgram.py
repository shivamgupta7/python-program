import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def series_data(num):
    # iterate over loop
    ds = pd.Series()
    for index in range(num):
        # getting element from user
        element = int(input("\nEnter {} element:".format(index+1)))
        # add element into data Series
        ds.at[index] = element
    return ds

class programPandas:

    def arrToSeries(self):
        '''
        Create and display a 1-D array-like object containing an array of data using Pandas module
        '''
        num = int(input("\nHow many element you want to add:"))
        data = series_data(num)
        return data

    def seriesToList(self):
        '''
        Convert a Panda module Series to Python list and it's type
        '''
        data = self.arrToSeries()
        print("Pandas Series :\n", data)
        # type of series
        print("Type of series : ", type(data))
        # convert series data into python list and display type
        print("Converted python list : ", data.tolist())
        print("Type of python list : ", type(data.tolist()))

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Create and display a 1-D array-like object containing an array of data using Pandas module
    2.Convert a Panda module Series to Python list and it's type
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.arrToSeries,
            2 : obj.seriesToList,
            }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        func()
    except Exception as e:
        print("\n",e)
    
def main():
    obj = programPandas()
    switchToFunction(obj)
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()