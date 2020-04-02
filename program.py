import calendar
from datetime import date
import multiprocessing
import os
import getpass
import time
import glob    # get a list of file excludung directories
import sys
import socket

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

    def sort_three_number(self):
        '''
        Sort three integers without using conditional statements and loops.
        '''
        self.number1 = int(input("Input first number: "))
        self.number2 = int(input("Input second number: "))
        self.number3 = int(input("Input third number: "))

        self.min = min(self.number1, self.number2, self.number3)
        self.max = max(self.number1, self.number2, self.number3)
        self.middle = (self.number1 + self.number2 + self.number3) - self.min - self.max
        return self.min, self.middle, self.max

    def sort_file_by_date(self, path):
        '''
        Sort files by last modified date.
        '''
        self.files = glob.glob(path)
        self.files.sort(key=os.path.getmtime)
        return self.files

    def get_command_argu(self):
        '''
        Get the command-line arguments (name of the script, the number
        of arguments, arguments) passed to a script.
        '''
        self.script_name = sys.argv[0]
        self.argu_length = len(sys.argv)
        self.argu_list = str(sys.argv)
        return self.script_name, self.argu_length, self.argu_list
        
    def get_builtin_module(self):
        '''
        Return the available built-in modules
        '''
        self.module_name = [', '.join(sys.builtin_module_names)]   # sys.builtin_module_names given all python built-in modules
        return self.module_name

    def get_object_size(self, object_name):
        '''
        Get the size of an object in bytes.
        '''
        self.obj_size = sys.getsizeof(object_name)   # sys.getsizeof() given size of file.
        return self.obj_size

    def get_recursion_limit(self):
        '''
        Get the current value of the recursion limit.
        '''
        return sys.getrecursionlimit()   # Return the current value of the recursion value

    def count_occurrence(self):
        '''
        Count the number occurrence of a specific character in a string.
        '''
        self.string = input("Enter the String : ")
        self.count_char = input("Enter character for count number of occurrence : ")
        self.occurrence = self.string.count(self.count_char)
        return self.occurrence

    def get_system_time(self):
        '''
        Get the system time.
        '''
        return time.ctime()

    def clear_screen(self):
        '''
        Clear the screen or terminal.
        '''
        return os.system("clear")

    def get_host_name(self):
        '''
        Get the name of the host on which the routine is running
        '''
        self.host_name = socket.gethostname()
        return self.host_name

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
    print(obj.sort_three_number())
    print(obj.sort_file("/media/shivam_gupta/Material/New folder/*.exe"))
    print(obj.get_command_argu())
    print(obj.get_builtin_module())
    print(obj.get_object_size(obj))
    print(obj.get_recursion_limit())
    print(obj.count_occurrence())
    print(obj.get_system_time())
    obj.clear_screen()
    print(obj.get_host_name())

if __name__ == "__main__":
    main()