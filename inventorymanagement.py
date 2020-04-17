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

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Open Inventory book(load json file)
    ''')

def switchToFunction(case,filepath):
    '''
    Create switch function to move perticular program
    '''
    obj = inventoryManagement
    switcher = {
        1 : lambda: obj.open_inventorybook(filepath),
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