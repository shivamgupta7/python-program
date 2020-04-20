"""This python file having all the important 
methods necessary for commercial data processing.
"""
# importing important modules
import datetime
import json
import os

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