import calendar
from datetime import date
import multiprocessing
import os
import getpass
import time

class programWeek1:
    
    def reverse_name(self):

        '''Program which accepts the user's first and last name and print them in reverse order with a space between them.'''

        self.fname = input("Enter your First name : ")   # take input from user
        self.lname = input("Enter your Last name : ")    # take input from user
        print(self.fname[::-1],self.lname[::-1])         # reverse first and last name 
    
    def list_tuple(self):

        '''Program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.'''

        self.number = input("Input some comma seprated numbers : ")   # take input from user
        self.list = self.number.split(",")   # split() method splits a string into a list.
        self.tuple = tuple(self.list)        # convert list to tuple using tuple() function.
        print('List : ',self.list)
        print('Tuple : ',self.tuple)

    def display_colors(self):

        '''program to display the first and last colors from the following list.'''

        color_list = ["Red","Green","White" ,"Black"]
        print("First color is {0} and Last color is {1}.".format(color_list[0],color_list[-1]))

    def document_builtInFunction(self):

        ''' program to print the documents (syntax, description etc.) of Python built-in function(s).'''

        func = input("Enter a valid Python function name: ")
        print(help(func))     # help that provides a helpful message.

    def print_calendar(self):
        
        '''program to print the calendar of a given month and year'''

        self.year = int(input("Input the year : "))
        self.month = int(input("Input the month : "))
        print(calendar.month(self.year, self.month))   # print calendar for given month and year.

    def getNoOfDays(self):
        
        ''' Program to calculate number of days between two dates.'''

        self.f_date = input("Input the first date (yyyy/mm/dd) : ").split("/")
        self.l_date = input("Input the last date (yyyy/mm/dd): ").split("/")
        self.year1 = int(self.f_date[0])
        self.month1 = int(self.f_date[1])
        self.date1 = int(self.f_date[2])
        self.year2 = int(self.l_date[0])
        self.month2 = int(self.l_date[1])
        self.date2 = int(self.l_date[2])
        self.first_date = date(self.year1,self.month1,self.date1)   # using datetime module convert into date type
        self.last_date = date(self.year2,self.month2,self.date2)
        delta = self.last_date - self.first_date     # diffrence between dates
        print(delta)

    def is_group_member(self):
        
        '''program to check whether a specified value is contained in a group of values.'''

        list = [1, 5, 8, 3]
        self.value = int(input("Enter the seaching number : "))
        print(self.value in list)

    def histogram(self,items):
        
        '''Program to create a histogram from a given list of integers.'''
        
        self.items = items
        for number in items:
            output = ''
            times = number
            while( times > 0 ):
                output += '*'
                times = times - 1
            print(output)

    def concatenate_list_data(self, list):

        ''' concatenate all elements in a list into a string and return it.'''
        
        self.list = list
        result= ''
        for element in list:
            result += str(element)   # convert each element into string
        print(result)

    def set_difference(self):
        
        '''Print out a set containing all the colors from color_list_1 which are not present in color_list_2.'''
        
        self.color_list_1 = set(["White", "Black", "Red"])
        self.color_list_2 = set(["Red", "Green"])
        print(self.color_list_1.difference(self.color_list_2))

    def cpu_using(self):
        '''
        find out the number of CPUs using.
        '''
        print("Number of CPU using : ",multiprocessing.cpu_count())

    def all_files(self, path):
        '''
         list all files in a directory in Python.
        '''
        print(os.listdir(path))
   
    def check_environment(self):
        '''
        Access environment variables.
        '''
        print(os.environ)

    def get_current_username(self):
        '''
        Get the current username.
        '''
        print("Current Username : ",getpass.getuser())   # The getuser() function displays the login name of the user.

    def get_execution_time(self):
        '''
        Get execution time.
        '''
        self.start = time.time()
        self.end = time.time()
        print(self.end - self.start)

    def absolute_file_path(self,path_fname):
        '''
        Get an absolute file path.
        '''
        print(os.path.abspath(path_fname))

    def create_modification_dateTime(self, file):
        '''
         Get file creation and modification date/times.
        '''
        print("Created: %s" % time.ctime(os.path.getctime(file)))   # ctime() - The number of seconds to be converted into string representation. getctime() path creation time.
        print("Last modified: %s" % time.ctime(os.path.getmtime(file)))   # getmtime - path modification time.

def main():
    obj = programWeek1()   # create object of class
    obj.reverse_name()     # calling methods(function) in class
    obj.list_tuple()
    obj.display_colors()
    obj.document_builtInFunction()
    obj.print_calendar()
    obj.getNoOfDays()
    obj.is_group_member()
    obj.histogram([2,5,3,8])
    obj.concatenate_list_data([2,5,3,8])
    obj.set_difference()
    obj.cpu_using()
    obj.all_files('/home/shivam_gupta/Documents/python-program/')
    obj.check_environment()
    obj.get_current_username()
    obj.get_execution_time()
    obj.absolute_file_path('program.py')
    obj.create_modification_dateTime('program.py')

if __name__ == "__main__":
    main()