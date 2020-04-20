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