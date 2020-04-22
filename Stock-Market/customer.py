"""This python file having the custom constructor to initialize 
the values of Customer of the variables and this file also
contain the data handler of the values(getter and setter methods).
"""


# 'Customer' class for constructor and data-handler
class Customer(object):

    # overriding user-defined constructor to initialize the values to the user-input
    def __init__(self, Customer_name, amount, noOfShare):
        self.__CustomerName = Customer_name
        self.__amount = amount
        self.__noOfShare = noOfShare

    # data-handler methods to get the and set the value to the variables
    @property
    def customer_name(self):  # getter method to get the 'customer name'
        return self.__CustomerName

    @property
    def amount(self):  # getter method to get the 'amount'
        return self.__amount

    @property
    def noOfShare(self):  # getter method to get the 'number of share'
        return self.__noOfShare

    @customer_name.setter
    def customer_name(self, Customer_name):  # setter method to set the value of 'customer name'
        self.__CustomerName = Customer_name

    @amount.setter
    def amount(self,amount):  # setter method to set the value of 'amount'
        self.__amount = amount

    @noOfShare.setter
    def noOfShare(self, noOfShare):  # setter method to set the value of 'number of share'
        self.__noOfShare = noOfShare