"""This python file having the data handler of the 
values(getter and setter methods) of Transaction.
"""

# 'transaction' class for data-handler
class Transaction(object):

    # overriding user-defined constructor to initialize the values to the user-input
    def __init__(self, customer_name, company_symbol, buyOrSell, total_share, total_price, time):
        self.__customerName = customer_name
        self.__companySymbol = company_symbol
        self.__buyOrSell = buyOrSell
        self.__totalShare = total_share
        self.__totalPrice = total_price
        self.__time = time
    
    # data-handler methods to get the and set the value to the variables
    @property
    def customer_name(self):  # getter method to get the 'customer name'
        return self.__customerName

    @property
    def company_symbol(self):  # getter method to get the 'company symbol'
        return self.__companySymbol

    @property
    def buyOrSell(self):  # getter method to get the 'buyOrSell'
        return self.__buyOrSell

    @property
    def total_share(self):  # getter method to get the 'total share'
        return self.__totalShare

    @property
    def total_price(self):  # getter method to get the 'total_price'
        return self.__totalPrice

    @property
    def time(self):  # getter method to get the 'time'
        return self.__time

    @customer_name.setter
    def customer_name(self, customer_name):  # setter method to set the value of 'customer name'
        self.__customerName = customer_name

    @company_symbol.setter
    def company_symbol(self, company_symbol):  # setter method to set the value of 'company symbol'
        self.__companySymbol = company_symbol

    @buyOrSell.setter
    def buyOrSell(self, buyOrSell):  # setter method to set the value of 'buyOrSell'
        self.__buyOrSell = buyOrSell

    @total_share.setter
    def total_share(self, total_share):  # setter method to set the value of 'total_share'
        self.__totalShare = total_share

    @total_price.setter
    def total_price(self, total_price):  # setter method to set the value of 'total_price'
        self.__totalPrice = total_price

    @time.setter
    def time(self, time):  # setter method to set the value of 'time'
        self.__time = time