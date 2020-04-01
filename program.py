import calendar
from datetime import date

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
        
        ''' program to calculate number of days between two dates.'''

        self.f_date = input("Input the first date (yyyy/mm/dd) : ")
        self.l_date = input("Input the last date (yyyy/mm/dd): ")
        self.year1 = int(self.f_date.split("/")[0])
        self.month1 = int(self.f_date.split("/")[1])
        self.date1 = int(self.f_date.split("/")[2])
        self.year2 = int(self.l_date.split("/")[0])
        self.month2 = int(self.l_date.split("/")[1])
        self.date2 = int(self.l_date.split("/")[2])
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

if __name__ == "__main__":
    main()