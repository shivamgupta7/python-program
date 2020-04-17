import json, os
import tabulate

class inventoryManagement:

    def __init__(self, name, weight, price):
        # make all attributes as private
        self._name = name
        self._weight = weight
        self._price = price
    
    @property  # get method
    def name(self):
        return self._name
    
    @name.setter  # set method
    def name(self, name):
        self._name = name

    @property  # get method
    def weight(self):
        return self._weight
    
    @weight.setter  # set method
    def weight(self, weight):
        self._weight = weight

    @property  # get method
    def price(self):
        return self._price
    
    @price.setter  # set method
    def price(self, price):
        self._price = price
    
    @staticmethod
    def open_inventorybook(filepath):
        """
        Function to open the inventory book file specified
        Returns the inventorybook or None
        """
        path_exists = os.path.exists(filepath)
        inventorybook = None
        if path_exists:
            try:                   # safest way to open or close file.
                with open(filepath, 'r') as infile:
                    inventorybook = json.load(infile)
            finally:
                infile.close()
        return inventorybook

    @staticmethod
    def save_inventorybook(filepath, types, product):
        '''
        Function to save the inventory book file specified type of product
        '''
        # Try to open the current inventory book
        inventorybook = inventoryManagement.open_inventorybook(filepath)

        if inventorybook is None:
            # If there was no inventory book create one
            print('Creating new inventory book')
            inventorybook = {'Rice': [], 'Pulses': [], 'Wheats': []}
        
        try:
            with open(filepath, 'w') as outfile:
                # Write the output file with the new product into inventory book
                inventorybook[types].append(product)
                json.dump(inventorybook, outfile, indent=4)
                print('Product added into inventory book.')
        finally:
            outfile.close()

    @classmethod
    def printAllInventory(cls,filepath):
        """
        Function to print list of all products details in the inventorybook as form of tables.
        """
        inventory_books = cls.open_inventorybook(filepath)
        if inventory_books:
            print('1.Rice\n2.Pulses\n3.Wheats\n4.All')
            choice = int(input('Enter your choice: '))
            if choice == 1:
                rices = inventory_books['Rice']
                header = rices[0].keys()
                rows =  [rice.values() for rice in rices]
                print(tabulate.tabulate(rows, header))
            elif choice == 2:
                pulses = inventory_books['Pulses']
                header = pulses[0].keys()
                rows =  [pulse.values() for pulse in pulses]
                print(tabulate.tabulate(rows, header))
            elif choice == 3:
                wheats = inventory_books['Wheats']
                header = wheats[0].keys()
                rows =  [wheat.values() for wheat in wheats]
                print(rows)
                print(tabulate.tabulate(rows, header))
            elif choice == 4:
                header = inventory_books['Rice'][0].keys()
                rice =  [rice.values() for rice in inventory_books['Rice']]
                pulse =  [pulses.values() for pulses in inventory_books['Pulses']]
                wheat =  [wheats.values() for wheats in inventory_books['Wheats']]
                all_inventory = rice + pulse + wheat
                rows =  [item for item in all_inventory]
                print(tabulate.tabulate(rows, header))
            else:
                print('Invalid choice.')
        else:
            print('No inventory book found!')

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Open Inventory book(load json file)
    2.Print list of all products details in the inventorybook
    ''')

def switchToFunction(case,filepath):
    '''
    Create switch function to move perticular program
    '''
    obj = inventoryManagement
    switcher = {
        1 : lambda: obj.open_inventorybook(filepath),
        2 : lambda: obj.printAllInventory(filepath),
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    func()

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    FILE_PATH = "data/inventory.json"
    switchToFunction(choice,FILE_PATH)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()