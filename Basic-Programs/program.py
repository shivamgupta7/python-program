import calendar
from datetime import date
import multiprocessing
import os
import getpass
import time
import glob    # get a list of file excludung directories
import sys
import socket
from http.client import HTTPConnection
import subprocess
import struct

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

    def access_print_url(self):
        '''
        Access and print a URL's content to the console.
        '''
        self.conn = HTTPConnection("www.google.com")
        self.conn.request("GET", "/")
        self.result = self.conn.getresponse()
        self.contents = self.result.read()   # retrieves the entire contents.
        return self.contents

    def get_system_command(self):
        '''
        Get system command output.
        '''
        command = input("Enter the command : ")
        returned_output = subprocess.check_output(command, shell=True, universal_newlines=True)
        return returned_output

    def get_group_ids(self):
        '''
        Get the effective group id, effective user id, real group id, a list of
        supplemental group ids associated with the current process.
        '''
        self.effect_group_id = os.getegid()           # Get the effective group id
        self.effect_user_id = os.geteuid()            # Get the effective user id
        self.real_group_id = os.getgid()              # Get the real group id
        self.supplemental_group_ids = os.getgroups()  # Get the list of supplemental group ids
        return self.effect_group_id, self.effect_user_id, self.real_group_id, self.supplemental_group_ids

    def divisible_by_fifteen(self,num_list):
        '''
        Get numbers divisible by fifteen from a list using an anonymous function.
        '''
        self.result = list(filter(lambda x: (x % 15 == 0), num_list))    # use anonymous function to filter
        return self.result

    def var_definedOrNot(self):
        '''
        Determine whether variable is defined or not.
        '''
        try:
            var_name1 = 123
        except NameError:
            print("Variable is not defined....!")
        else:
            print("Variable is defined.")
            
        try:
            var_name2
        except NameError:
            print("Variable is not defined....!")
        else:
            print("Variable is defined.")

    def get_empty_variable(self):
        '''
        Empty a variable without destroying it.
        '''
        n = 20
        d = {"x":200}
        l = [1,2,3,4]
        t = (5,6,7,8)
        return type(n)(), type(d)(), type(l)(), type(t)()

    def left_padding(self):
        '''
        Add leading character to a string.
        '''
        self.string = input("Enter the string : ")
        self.fillchar = input("Enter the left padding number or char : ")
        self.width = int(input("Enter the width/length of string : "))
        self.new_string = self.string.ljust(self.width, self.fillchar)    # ljust() :- Return the string left justified in a string of specified length.
        return self.new_string

    def extract_key_value(self, dictionary):
        '''
        Extract single key-value pair of a dictionary in variables.
        '''
        (key, value), = dictionary.items()
        return key, value

    def int_to_binary(self,integer):
        '''
        Convert an integer to binary keep leading zeros.
        '''
        self.binary = format(integer, '010b')
        return self.binary

    def python_shell_mode(self):
        '''
        Determine if the python shell is executing in 32bit or 64bit mode on operating system.
        '''
        self.mode = struct.calcsize("P") * 8
        return self.mode

    def find_min_max(self,data):
        '''
        Find the maximum and minimum numbers from a sequence of numbers.
        '''
        self.min = data[0]
        self.max = data[0]
        for num in data:
            if num > self.max:
                self.max = num
            elif num < self.min:
                self.min = num
        return self.min, self.max

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
    print(obj.access_print_url())
    print(obj.get_system_command())
    print(obj.get_group_ids())
    print(obj.divisible_by_fifteen([45, 55, 60, 37, 100, 105, 220]))
    obj.var_definedOrNot()
    print(obj.get_empty_variable())
    print(obj.left_padding())
    print(obj.extract_key_value({7:'shivam'}))
    print(obj.int_to_binary(12))
    print(obj.python_shell_mode())
    print(obj.find_min_max([2, 10, 15, 40, 32, -4, 15, 28]))

if __name__ == "__main__":
    main()