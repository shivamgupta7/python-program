import json, os
import tabulate

from inventoryfactory import inventoryFactory

class inventoryManagement:

    @classmethod
    def modify_product(cls, filepath, obj):
        '''
        Function to modify specified product details in the inventory book
        '''
        inventory_books = obj.open_inventorybook(filepath)
        try:
            if inventory_books:
                print('1.Modify into Rice\n2.Modify into Pulses\n3.Modify into Wheats')
                choice = int(input('Enter where you want to modify: '))
                switcher = {1: "Rice", 2: "Pulse", 3: "Wheats"}
                grain = switcher.get(choice)
                name= input("Enter the name of the product to be modified: ")
                is_product_modified=False
                for item in inventory_books[grain]:
                    if item['name'].casefold() == name.casefold():
                        cls.do_modification(item)
                        with open(filepath, 'w') as outfile:
                            json.dump(inventory_books, outfile, indent= 4)
                        is_product_modified=True
                        outfile.close()
                        print("Product modified")
                        break
                if not is_product_modified:
                    print("No product with this name found")
            else:
                print("Inventory book empty. No product to modified")

        except KeyError:
            print('Invalid Input! Product not modify.')
            exit()

        except KeyboardInterrupt:
            print('\nHiting the interrupt key!')
            print('Product not modified.')
            exit()
    
    @classmethod
    def do_modification(cls, product):
        '''
        Function to modifiy specified product weight and price
        '''
        try:
            while True:
                print ("1.Modify weigth\n2.Modify price\n3.quit without modifying")
                choice= int(input('Enter which you want to modify: '))
                if choice == 1:
                    new_weight = float(input("Enter new weigth: "))
                    inventoryManagement.weight = new_weight
                    product['weight'] = inventoryManagement.weight
                    break
                elif choice == 2:
                    new_price = float(input("Enter new price: "))
                    inventoryManagement.price = new_price
                    product['price'] = inventoryManagement.price
                    break
                else:
                    print("Incorrect choice")
                    break
        except EOFError:
            print("EOF Error occurred")
        except KeyboardInterrupt:
            print("KeyboardInterrupt occurred")

    @classmethod
    def retrieveProduct(cls, filepath, obj):
        """
        Function to retirve specified product details in the inventorybook
        Returns a product or None
        """
        inventory_books = obj.open_inventorybook(filepath)
        try:
            if inventory_books:
                print('1.Search into Rice\n2.Search into Pulses\n3.Search into Wheats')
                choice = int(input('Enter where you want to search: '))
                switcher = {1: "Rice", 2: "Pulses", 3: "Wheats"}
                grain = switcher.get(choice)
                print(grain)
                name= input("Enter the name of the product to be search: ")
                is_product = False
                for item in inventory_books[grain]:
                    if item['name'].casefold() == name.casefold():
                        header = item.keys()
                        rows =  [item.values()]
                        print(tabulate.tabulate(rows, header))
                        is_product = True
                if not is_product:
                    print('Product not found!')
            else:
                print("Inventory book empty!")

        except KeyError:
            print('Invalid Input! Product not Search.')
            exit()

        except KeyboardInterrupt:
            print('\nHiting the interrupt key!')
            print('Product not search.')
            exit()

    @classmethod
    def claculatePrice(cls, filepath, obj):
        '''
        Function to calculate all inventory price
        '''
        inventorybook = obj.open_inventorybook(filepath)
        for grain in inventorybook:
            totalPrice = 0
            for item in inventorybook[grain]:
                totalPrice += item['price'] * item['weight']
            print('Total {} price is {}'.format(grain,totalPrice))

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Modify specified product details in the inventory book
    2.Retirve specified product details in the inventorybook
    3.Calculate all inventory price
    ''')

def switchToFunction(case,filepath,obj):
    '''
    Create switch function to move perticular program
    '''
    manager = inventoryManagement
    switcher = {
        1 : lambda: manager.modify_product(filepath,obj),
        2 : lambda: manager.retrieveProduct(filepath,obj),
        3 : lambda: manager.claculatePrice(filepath,obj),
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    func()

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    FILE_PATH = "data/inventory.json"
    obj = inventoryFactory
    switchToFunction(choice,FILE_PATH,obj)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()