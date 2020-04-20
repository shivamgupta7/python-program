"""This python file having the custom constructorto initialize 
the values of Company of the variables and this file also
contain the data handler of the values(getter and setter methods).
"""

# 'Company' class for constructor and data-handler
class Company(object):

    # overriding user-defined constructor to initialize the values to the user-input
    def __init__(self, company_name, company_symbol, share_price, total_share):
        self.__companyName = company_name
        self.__companySymbol = company_symbol
        self.__sharePrice = share_price
        self.__totalShare = total_share

    # data-handler methods to get the and set the value to the variables
    @property
    def company_name(self):  # getter method to get the 'company name'
        return self.__companyName

    @property
    def company_symbol(self):  # getter method to get the 'company symbol'
        return self.__companySymbol

    @property
    def share_price(self):  # getter method to get the 'share price'
        return self.__sharePrice

    @property
    def total_share(self):  # getter method to get the 'total share'
        return self.__totalShare

    @company_name.setter
    def company_name(self, company_name):  # setter method to set the value of 'company name'
        self.__companyName = company_name

    @company_symbol.setter    
    def company_symbol(self, company_symbol):  # setter method to set the value of 'company symbol'
        self.__companySymbol = company_symbol

    @share_price.setter
    def share_price(self, share_price):  # setter method to set the value of 'share price'
        self.__sharePrice = share_price

    @total_share.setter
    def total_share(self, total_share):  # setter method to set the value of 'total share'
        self.__totalShare = total_share