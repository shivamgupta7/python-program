"""This python file having all the important 
methods necessary for commercial data processing.
"""
# importing important modules
import datetime
import json
import os
from transaction import *
from customer import *
from company import *

# this method to open the json file specified Returns the json file object or None
def open_jsonfile(filepath):
    path_exists = os.path.exists(filepath)
    jsonObj = None
    if path_exists:
        try:                  # safest way to open or close file.
            with open(filepath, 'r') as infile:
                jsonObj = json.load(infile)
        finally:
            infile.close()
    return jsonObj

# this method write the customer information to the customer JSON file after taking the @param customer object contains
# all the information about customer
def save(customer_obj):
    customer_info = open_jsonfile('data/customer.json')
    for data in list(customer_info['Customers']):
        if customer_info["Customers"][data]["Name"] == customer_obj.customer_name:
            print("Data already found in Database! Please insert a new data.\n")
            exit()
    customer_info["Customers"][customer_obj.customer_name] = ({
        'Name': customer_obj.customer_name,
        'Shares': customer_obj.noOfShare,
        'Amounts': customer_obj.amount
        })
    with open('data/customer.json', 'w') as data:  # writing the data to the customer.json file
        json.dump(customer_info, data, indent=4)
    print("\nPerson Detail Added Successfully!\n")

# this function is search for the given company and return None if the company name given as argument not found
def searchCompany(symbol):
    try:
        company_info = open_jsonfile('data/company.json')
        name_keys = list(company_info.keys())
        count = 0
        for data in name_keys:
            if company_info[data]["Company Symbol"].casefold() == symbol.casefold():
                count += 1
                company_name = company_info[data]["Company Name"]
                company_symbol = company_info[data]["Company Symbol"]
                total_share = company_info[data]["Total Share"]
                share_Price = company_info[data]["Share Price"]
        try:
            new_obj = {
                "Company Name": company_name,
                "Company Symbol": company_symbol,
                "Total Share": total_share,
                "Share Price": share_Price
                }
        except Exception as e:
            print("\n", e)
        if count == 0:
            return None
        else:
            return new_obj

    except SyntaxError:
        print("error in name")

# this function is search for the given customer and return None if the customer name given as argument not found
def searchCustomer(name):
    try:
        customer_info = open_jsonfile('data/customer.json')
        count = 0
        for data in list(customer_info['Customers']):
            if data.casefold() == name.casefold():
                count += 1
                customername = customer_info["Customers"][data]["Name"]
                no_of_share = customer_info["Customers"][data]["Shares"]
                amount = customer_info["Customers"][data]["Amounts"]
        try:
            new_obj = {
                "Name": customername,
                "Shares": no_of_share,
                "Amounts": amount
                }
        except Exception as e:
            print("\n", e)
        if count == 0:
            return None
        else:
            return new_obj

    except SyntaxError:
        print("error in name")

def buy(share_no, customer, company):

    customer_info = open_jsonfile('data/customer.json')
    company_info = open_jsonfile('data/company.json')
    transaction_info = open_jsonfile('data/transaction.json')
    customer_available_amount = float(customer_info["Customers"][customer]["Amounts"])
    spending_amount = float(float(company_info[company]["Share Price"]) * share_no)
    if share_no <= company_info[company]["Total Share"]:

        if spending_amount <= customer_available_amount:

            transaction = Transaction

            transaction.customer_name = customer_info["Customers"][customer]["Name"]
            transaction.company_symbol = company_info[company]["Company Symbol"]
            transaction.buyOrSell = "Buy"
            transaction.total_share = share_no
            transaction.total_price = float(company_info[company]["Share Price"]) * share_no

            now = datetime.datetime.now()
            today = now.strftime("%Y-%m-%d %H:%M")
            transaction.time = today
            transaction_info["Transaction"][transaction.customer_name] = ({
                'Customer Name': transaction.customer_name,
                'Company Symbol': transaction.company_symbol,
                'Buy or Sell': transaction.buyOrSell,
                'Total Share': transaction.total_share,
                'Total Price': transaction.total_price,
                'Time': transaction.time
                })
            with open('data/transaction.json', 'w+') as data:
                json.dump(transaction_info, data, indent=4)
            print("\nTransaction Successful.")

            company_info[company]['Total Share'] -= share_no

            with open("data/company.json", "w") as company_data:
                json.dump(company_info, company_data, indent=4)

            customer_info["Customers"][customer]["Amounts"] -= spending_amount
            customer_info["Customers"][customer]["Shares"] += share_no

            with open("data/customer.json", "w") as company_data:
                json.dump(customer_info, company_data, indent=4)

        else:
            print("\n>>> Transaction Failed <<<\n>>> You don't have sufficient amount <<<")
    else:
        print("\nCompany don't have sufficient Share(s)\nPlease reduce your amount of Share(s)")

def sell(share_no, name, company_name):

    customer_info = open_jsonfile('data/customer.json')
    company_info = open_jsonfile('data/company.json')
    transaction_info = open_jsonfile('data/transaction.json')

    if share_no <= customer_info["Customers"][name]["Shares"]:
        customer_info["Customers"][name]["Shares"] -= share_no
        customer_info["Customers"][name]["Amounts"] += (company_info[company_name]["Share Price"] * share_no)
        with open("data/customer.json", "w") as company_data:
            json.dump(customer_info, company_data, indent=4, sort_keys=True)

        company_info[company_name]["Total Share"] += share_no
        with open("data/company.json", "w") as company_data:
            json.dump(company_info, company_data, indent=4, sort_keys=True)

        list_ = []
        transaction = Transaction

        transaction.customer_name = customer_info["Customers"][name]["Name"]
        transaction.company_symbol = company_info[company_name]["Company Symbol"]
        transaction.buyOrSell = "Sell"
        transaction.total_share = share_no
        transaction.total_price = float(company_info[company_name]["Share Price"]) * share_no

        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d %H:%M")
        transaction.time = today
        transaction_info["Transaction"][transaction.customer_name] = ({
            'Customer Name': transaction.customer_name,
            'Company Symbol': transaction.company_symbol,
            'Buy or Sell': transaction.buyOrSell,
            'Total Share': transaction.total_share,
            'Total Price': transaction.total_price,
            'Time': transaction.time
        })

        list_.append(transaction_info)
        with open('data/transaction.json', 'w') as data:
            json.dump(list_[0], data, indent=4)

        print("\n>>>         Transaction Successful         <<<")
        print("You have successfully sold your", share_no, "to", company_name)
        print("Your Shares deducted and equivalent money added to your account\n")
    else:
        print("\nYou don't have sufficient amount of share(s) to sell\n")

def buy_shares():

    customer_info = open_jsonfile('data/customer.json')
    company_info = open_jsonfile('data/company.json')

    name = input("\nEnter customer name: ")
    customer = searchCustomer(name)
    if customer is not None:
        detailData.display_company_symbol()
        symbol = input("Choose and enter company symbol from above chart to Buy Shares : ")
        for data in company_info:
            if company_info[data]["Company Symbol"].casefold() == symbol.casefold():
                company_name = company_info[data]["Company Name"]
        company = searchCompany(symbol)
        if company is not None:
            # display only selected company details
            for data in company_info:
                if company_info[data]["Company Symbol"].casefold() == symbol.casefold():
                    print("\nYour selected company details: \nName: ", company_info[data]["Company Name"], "\nSymbol: ",
                          company_info[data]['Company Symbol'],
                          "\nShare Price: ", company_info[data]['Share Price'], "\n")

            # display only selected available customer amount
            for data in list(customer_info['Customers']):
                if customer_info["Customers"][data]["Name"].casefold() == name.casefold():
                    print("--- Available amount of", name, "for transaction: ", customer_info["Customers"][data]["Amounts"], "---\n")
            share_no = int(input("Enter the number of Shares you want to buy (take reference from above chart) : "))
            buy(share_no, name, company_name)
        else:
            print("\n!!! Company Not Found !!!")
    else:
        print("\n!!! Customer Not Found !!!")

def sell_share():
    customer_info = open_jsonfile('data/customer.json')
    company_info = open_jsonfile('data/company.json')
    name = input("\nEnter customer name: ")
    customer = searchCustomer(name)
    if customer is not None:
        detailData.display_company_symbol()
        symbol = input("Choose and enter company symbol from above chart to sell Shares : ")
        for data in company_info:
            if company_info[data]["Company Symbol"].casefold() == symbol.casefold():
                company_name = company_info[data]["Company Name"]
        company = searchCompany(symbol)
        if company is not None:
            print("\n--- Available shares of", name, "is", customer_info["Customers"][name]["Shares"], " ---\n")
            share_no = int(input("Enter the number of Shares you want to sell : "))
            sell(share_no, name, company_name)
        else:
            print("\n!!! Company Not Found !!!")
    else:
        print("\n!!! Customer Not Found !!!")

class detailData:

    @staticmethod
    def display_company_symbol():
        company_info = open_jsonfile('data/company.json')
        print("\n Symbol Reference Chart of Companies\n"
              "--------------------------------------")
        for data in company_info:
            print("Name: ", company_info[data]["Company Name"], "\nSymbol:", company_info[data]["Company Symbol"], "\n")
        
    @staticmethod
    def add_customer():
        print("Customer Information")
        name = input("Enter customer name : ")
        amount = float(input("Enter a amount : "))
        no_of_share = int(input("Enter the Number Of Share : "))
        customer_obj = Customer(name, amount, no_of_share)
        customer_obj.customer_name = name
        customer_obj.amount = amount
        customer_obj.noOfShare = no_of_share
        save(customer_obj)

    @staticmethod
    def add_company():
        print("Company Information")
        company_name = input("Enter company name : ")
        company_symbol = input("Enter a company Symbol : ")
        share_price = float(input("Enter the Price Of Share : "))
        total_share = int(input("Enter the total Number Of Share : "))
        company_obj = Company(company_name, company_symbol, share_price,total_share)
        company_obj.company_name = company_name
        company_obj.company_symbol = company_symbol
        company_obj.share_price = share_price
        company_obj.total_share = total_share
        company_info = open_jsonfile('data/company.json')
        for data in list(company_info):
            if data.casefold() == company_obj.company_name.casefold():
                print("Data already found in Database! Please insert a newly data.\n")
                break
            else:
                company_info[company_obj.company_name] = ({
                    "Company Name": company_obj.company_name,
                    "Company Symbol": company_obj.company_symbol,
                    "Share Price": company_obj.share_price,
                    "Total Share": company_obj.total_share
                    })
                with open('data/company.json', 'w') as data:
                    json.dump(company_info, data, indent=2)
        print("\nCompany Detail Added Successfully!\n")
