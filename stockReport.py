"""'StockReport' is a program to read in Stock Names, Number of Share, Share Price.
Print a Stock Report with total value of each Stock and the total value of Stock
having functions in the Class to calculate the value of each stock and the value
of total stocks.
"""

# Stock class having constructor and data handler methods
class Stock:
    # user-defined constructor to initialize the values to the user-input
    def __init__(self, stock_name, no_of_share, share_price):
        self.__stock_name = stock_name
        self.__no_of_share = no_of_share
        self.__share_price = share_price

# data-handler methods to get the and set the value to the variables
    @property
    def stock_name(self):  # getter method to get the 'stock name'
        return self.__stock_name

    @stock_name.setter
    def stock_name(self, stock_name):  # setter method to set the value of 'stock name'
        self.__stock_name = stock_name

    @property
    def no_of_share(self):  # getter method to get the 'number of price'
        return self.__no_of_share

    @no_of_share.setter
    def no_of_share(self, no_of_share):  # setter method to set the value of 'number of share'
        self.__no_of_share = no_of_share

    @property
    def share_price(self):  # getter method to get the 'share price'
        return self.__share_price

    @share_price.setter
    def share_price(self, share_price):  # setter method to set the value of 'share price'
        self.__share_price = share_price


# 'StockPortfolio' class having method to calculate total value of each stock and method to calculate  grand-total
# value of all the stocks
class StockPortfolio:

    no_of_stocks = int(input("\nEnter total number of stocks: "))
    count = 0  # initializing count variable to run the while loop until the total number of stocks given by the user
    objects = []  # creating the blank list to store all the Stock objects having Stock details
    try:
        while count < no_of_stocks:

            # taking details of stock details from the user
            name = input("Enter the name of Stock: ")
            if not name:
                raise ValueError('Error: Not enter Stock name')
            share = int(input("Enter the number of share(s) for Stock: "))
            if not share:
                raise ValueError('Error: Not enter Stock Share')
            price = float(input("Enter the price of Stock: "))
            if not price:
                raise ValueError('Error: Not enter Stock price')

            # creating new object of Stock class by calling the constructor
            obj = Stock(name, share, price)
            obj.stock_name = name  # setting name of the stock taken from the user
            obj.no_of_share = share  # setting number of stocks, input taken from the user
            obj.share_price = price  # setting share price taken from the user

            objects.append(obj)  # appending all the objects created one by one to the list 'objects'
            count += 1
            print()

    except ValueError as err:
            print(err)
            print('Stock not added.')
            exit()

    except KeyboardInterrupt:
        print('\nHiting the interrupt key.')
        print('Stock not added.')
        exit()

    # this method calculate individual Stocks total stock value having @param objects and @param index and @return stock
    # value which is calculated total value of individual stock
    @staticmethod
    def cal_stock_val(objects, index):
        # multiplying price of one share and the number of shares to calculate the value of individual stock
        stock_value = objects[index].no_of_share * objects[index].share_price
        return stock_value

    # this method calculate total value of all stocks having @param objects and @return total calculated stocks value
    @staticmethod
    def cal_total_stocks_value(objects):
        total_stocks_value = 0
        for index in range(len(objects)):
            # multiplying price of one share and the number of shares to calculate the value of individual stock and
            # adding in a variable to get grand total value of all Stocks
            total_stocks_value += objects[index].no_of_share * objects[index].share_price
        return total_stocks_value

    print(" >>> Stock Report <<<\n----------------------")
    for index in range(len(objects)):
        print(" Stock Name:", objects[index].stock_name, "\n", "Number of Share:", objects[index].no_of_share,"\n",
              "Share Price:", objects[index].share_price, "\n", "Value of", objects[index].stock_name, ":", cal_stock_val.__func__(objects, index), "\n")

    print(">>> Value of total stocks:", cal_total_stocks_value.__func__(objects), "<<<")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    stock = StockPortfolio()  # creating object of 'StockPortfolio' class