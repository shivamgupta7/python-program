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
        print('''
        Type of series : {}
        Converted python list : {}
        Type of python list : {}'''.format(type(data), data.tolist(), type(data.tolist())))
        return data.tolist()

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
        return switcher.get(choice, '\nInvalid input.')

    def get_power(self):
        '''
        Program to get the powers of an array values element-wise
        '''
        size = int(input('\nEnter the size of array: '))
        data = np.arange(size)
        print('\nOriginal array: ', data)
        power = np.power(data, 3)
        print("\nPower of array value to element wise:")
        return power

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
        # print(df)
        return df

    def dataframeInformation(self):
        '''
        Display a summary of the basic information about a specified DataFrame and its data
        '''
        df = self.dictToDataFrame()
        return df.info()

    def firstNRows(self):
        '''
        Get the first n rows of a given DataFrame
        '''
        df = self.dictToDataFrame()
        n_rows = int(input('\nEnter how many row you want to print: '))
        return df.head(n_rows)

    def selectColumns(self):
        '''
        Select the 'name' and 'score' columns from the following DataFrame
        '''
        df = self.dictToDataFrame()
        print('Select specific columns :')
        return df[['name','score']]

    def select_row_columns(self):
        '''
        Select the specified columns and rows from a given DataFrame.Select 'name' 
        and 'score' columns in rows 1, 3, 5, 6 from the following data frame.
        '''
        df = self.dictToDataFrame()
        print("Select specific columns and rows:")
        return df.iloc[[1, 3, 5, 6], [0, 1]]

    def attempts(self):
        '''
        Select the rows where the number of attempts in the examination is greater than 2
        '''
        df = self.dictToDataFrame()
        print('Attempts in the examination is greater than 2: ')
        return df[df['attempts'] > 2]

    def shapeOfDataFrame(self):
        '''
        Count the number of rows and columns of a DataFrame.
        '''
        df = self.dictToDataFrame()
        print('\n Shape of data frame : ')   #row : len(df.axes[0]), col : len(df.axes[1])
        return df.shape   #(row, col)

    def check_null(self):
        '''
        Select the rows where the score is missing, i.e. is NaN.
        '''
        df = self.dictToDataFrame()
        return df[df.score.isnull()]

    def score_attempts(self):
        '''
        select the rows where number of attempts in the 
        examination is less than 2 and score greater than 15
        '''
        df = self.dictToDataFrame()
        return df[ (df.score > 15) & (df.attempts < 2) ]

    def set_value(self):
        '''
        Change the score in row 'd' to 11.5
        '''
        df = self.dictToDataFrame()
        df.at['d', 'score'] = 11.5
        return df

    def sum_attempts(self):
        '''
        Calculate the sum of the examination attempts by the students
        '''
        df = self.dictToDataFrame()
        print('Sum of the examination attempts')
        return df[df.attempts.sum()]

    def mean_score(self):
        '''
        Calculate the mean score for each different student in data frame
        '''
        df = self.dictToDataFrame()
        print('Mean score for each different student: ')
        return df[df.score.mean()]

    def append_delete_row(self):
        '''
        Append a new row 'k' to DataFrame with given values for each column. 
        Now delete the new row and return the original data frame
        '''
        df = self.dictToDataFrame()
        df.loc['k'] = ['Suresh', 15.5, 1, 'yes']
        print('''Print all records after insert a new record: \n{}
        \nDelete the new row and display the original rows: '''.format(df))
        return df.drop('k')

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
    6.Display a summary of the basic information about a specified DataFrame and its data
    7.Get the first 3 rows of a given DataFrame
    8.Select the 'name' and 'score' columns from the following DataFrame
    9.Select the specified columns and rows from a given DataFrame
    10.Select the rows where the number of attempts in the examination is greater than 2
    11.Count the number of rows and columns of a DataFrame
    12.Select the rows where the score is missing, i.e. is NaN.
    13.select the rows where number of attempts in the examination is less than 2 and score greater than 15
    14.Change the score in row 'd' to 11.5
    15.Calculate the sum of the examination attempts by the students
    16.Calculate the mean score for each different student in data frame
    17.append a new row 'k' to DataFrame with given values for each column. 
    Now delete the new row and return the original data frame
    ''')
    try:
        choice = int(input('Enter which program you want to run: '))
        switcher = {
            1 : obj.arrToSeries,
            2 : obj.seriesToList,
            3 : obj.add_sub_mul_div,
            4 : obj.get_power,
            5 : obj.dictToDataFrame,
            6 : obj.dataframeInformation,
            7 : obj.firstNRows,
            8 : obj.selectColumns,
            9 : obj.select_row_columns,
            10 : obj.attempts,
            11 : obj.shapeOfDataFrame,
            12 : obj.check_null,
            13 : obj.score_attempts,
            14 : obj.set_value,
            15 : obj.sum_attempts,
            16 : obj.mean_score,
            17 : obj.append_delete_row,
            }
        func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
        print(func())
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