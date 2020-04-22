import pandas as pd
import numpy as np
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
        num = int(input("\nHow many element you want to add in series:"))
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

    def add_sub_mul_div(self):
        '''
        Program to add, subtract, multiple and divide two Pandas Series
        '''
        print("\nFor first pandas series : ")
        data1 = self.arrToSeries()
        print("\nPandas Series 1:\n", data1)
        print("\nFor second pandas series : ")
        data2 = self.arrToSeries()
        print("\nPandas Series 2:\n", data2)
        print('\n1.Add\n2.Subtract\n3.Multiply\n4.Division')
        choice = int(input('\nEnter your choice: '))
        switcher = {
            1 : data1+data2,
            2 : data1-data2,
            3 : data1*data2,
            4 : data1/data2
            }
        print(switcher.get(choice, '\nInvalid input.'))

    def get_power(self):
        '''
        Program to get the powers of an array values element-wise
        '''
        size = int(input('\nEnter the size of array: '))
        data = np.arange(size)
        print('\nOriginal array: ', data)
        power = np.power(data, 3)
        print("\nPower of array value to element wise:")
        print(power)

    def dictToDataFrame(self):
        '''
        Create and display a DataFrame from a specified dictionary data which has the index labels
        '''
        exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

        df = pd.DataFrame(exam_data , index=labels)
        print(df)

def switchToFunction(obj):
    '''
    Create switch function to move perticular program
    '''
    print('''
    1.Create and display a 1-D array-like object containing an array of data using Pandas module
    2.Convert a Panda module Series to Python list and it's type
    3.Program to add, subtract, multiple and divide two Pandas Series
    4.Program to get the powers of an array values element-wise
    5.Create and display a DataFrame from a specified dictionary data which has the index labels
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.arrToSeries,
            2 : obj.seriesToList,
            3 : obj.add_sub_mul_div,
            4 : obj.get_power,
            5 : obj.dictToDataFrame,
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