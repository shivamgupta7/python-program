"""This program which implements a data type that might be used by a financial
institution to keep track of customer information. The StockAccount class also
maintains a list of CompanyShares object which has Stock Symbol and Number of
Shares as well as DateTime of the transaction. When buy or sell is initiated
StockAccount checks if CompanyShares are available and accordingly update or
create an Object.
"""
# importing important modules
from detailData import detailData

# 'StockAccount' class contains main menu
class StockAccount:
    
    @staticmethod
    def stockProgram():
        # displaying main menu
        print('''-----------Stock Accounts-----------
            Enter 1. To Add a Customer
            Enter 2. To Add a Company
            Enter 3. To Display Customer
            Enter 4. To Display Company
            Enter 5. For Transaction
            Enter 6. For Exit
            ''')

        try:
            choice = int(input("Enter your choice: "))
        except Exception as e:  # handling the exception for bad input
            print(e, "\n!!! Invalid Input !!!\n")
        try:
            switcher = {
                1 : lambda: detailData.add_customer(),
                2 : lambda: detailData.add_company(),
                3 : lambda: detailData.display_customer(),
                4 : lambda: detailData.display_company(),
                5 : lambda: detailData.transaction(),
                6 : lambda: exit()
                }
            func = switcher.get(choice, lambda: print('\nInvalid choice please select correct options.'))
            func()
        except Exception as e:  # handling exception for bad input
            print(e)

def main():
    StockAccount.stockProgram()
    options = input('\nDo you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    main()