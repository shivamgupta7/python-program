import json, os
import tabulate

class addressbook:

    def __init__(self, fname, lname, address, city, state, zipCode, phone):
        # make all attributes as private
        self._fname = fname
        self._lname = lname
        self._address = address
        self._city = city
        self._state = state
        self._zipCode = zipCode
        self._phone = phone 

    def __str__(self):
        return "First Name:{0}\nLast Name:{1}\nAddress:{2}\nCity:{3}\nState:{4}\nZip Code:{5}\nPhone No:{6}".format(self._fname,self._lname,self._address,self._city,self._state,self._zipCode,self._phone)
    
    @property  # get method
    def fname(self):
        return self._fname
    
    @fname.setter  # set method
    def fname(self,fname):
        self._fname = fname

    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self,lname):
        self._lname = lname

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address
    
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        self._city = city

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, state):
        self._state = state
    
    @property
    def zipCode(self):
        return self._zipCode
    
    @zipCode.setter
    def zipCode(self, zipCode):
        self._zipCode = zipCode

    @property
    def phone(self, phone):
        return self._phone

    @phone.setter    
    def phone(self,phone):
        self._phone = phone

    @staticmethod
    def open_addressbook(filepath):
        """
        Function to open the address book file specified
        Returns the addressbook or None
        """
        path_exists = os.path.exists(filepath)
        addressbook = None
        if path_exists:
            try:                   # safest way to open or close file.
                with open(filepath, 'r') as infile:
                    addressbook = json.load(infile)
            finally:
                infile.close()
        return addressbook

    @classmethod
    def printAllContacts(cls,filepath):
        """
        Function to print list of all contacts details in the addressbook as form of tables.
        """
        address_books = cls.open_addressbook(filepath)
        if address_books:
            contacts = address_books['persons']
            header = contacts[0].keys()
            rows =  [person.values() for person in contacts]
            print(tabulate.tabulate(rows, header))
        else:
            print('No address book found!')

    @classmethod
    def add_contact(cls,filepath):
        """
        Function to add contact details to the addressbook
        It take user input and creates a contact that is added
        """
        new_contact = {}
        try:
            new_fname = input('Please enter the first name: ')
            addressbook.fname = new_fname          # set first name 
            new_contact['fname'] = addressbook.fname    # get first name
            if not new_contact['fname']:
                raise ValueError('Error: Empty First Name')

            new_lname = input('Please enter last name: ')
            addressbook.lname = new_lname
            new_contact['lname'] = addressbook.lname
            if not new_contact['lname']:
                raise ValueError('Error: Empty Last Name')

            new_address = input('Please enter address: ')
            addressbook.address = new_address
            new_contact['address'] = addressbook.address
            if not new_contact['address']:
                raise ValueError('Error: Empty address')

            new_city = input('Please enter city name: ')
            addressbook.city = new_city
            new_contact['city'] = addressbook.city
            if not new_contact['city']:
                raise ValueError('Error: Empty City Name')

            new_state = input('Please enter state name: ')
            addressbook.state = new_state
            new_contact['state'] = addressbook.state
            if not new_contact['state']:
                raise ValueError('Error: Empty State Name')

            new_zipCode = input('Please enter zip code: ')
            addressbook.zipCode = new_zipCode
            new_contact['zipCode'] = addressbook.zipCode
            if not new_contact['zipCode']:
                raise ValueError('Error: Empty Zip Code')

            new_phone = input('Please enter phone number: ')
            addressbook.phone = new_phone
            new_contact['phone'] = addressbook.phone
            if not new_contact['phone']:
                raise ValueError('Error: Empty Phone Number')

        except ValueError as err:
            print(err)
            print('Contact not added.')
            exit()

        except KeyboardInterrupt:
            print('\nHiting the interrupt key.')
            print('Contact not added.')
            exit()

            # Try to open the current addressbook
        addressbooks = cls.open_addressbook(filepath)

        if addressbooks is None:
            # If there was no addressbook create one
            print('Creating new address book')
            contacts = []
            addressbooks = {'persons': contacts}

        print(new_contact)
        try:
            with open(filepath, 'w') as outfile:
                # Write the output file with the new contact
                addressbooks['persons'].append(new_contact)
                json.dump(addressbooks, outfile, indent=4)
        finally:
            outfile.close()

    @classmethod
    def retrievePersonContact(cls,filepath):
        """
        Function to retirve specified contact details in the addressbook
        Returns a contact or None
        """
        print('Search data using: \n1.First Name\n2.Last Name\n3.City\n4.State')
        choice = int(input('Enter your choice: '))
        contact_details = []
        address_books = cls.open_addressbook(filepath)
        if not address_books:
            print('No address book found!')
        else:
            if choice == 1:
                fname = input('Enter First Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['fname'].casefold() == fname.casefold():  # casefold() convert string into lower case
                        contact_details.append(person)

            elif choice == 2:
                lname = input('Enter Last Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['lname'].casefold() == lname.casefold():
                        contact_details.append(person)

            elif choice == 3:
                city = input('Enter City Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['city'].casefold() == city.casefold():
                        contact_details.append(person)

            elif choice == 4:
                state = input('Enter State Name which contact you want to search: ')
                for person in address_books['persons']:
                    if person['state'].casefold() == state.casefold():
                        contact_details.append(person)
            
        if contact_details:
            header = contact_details[0].keys()
            rows =  [person.values() for person in contact_details]
            print(tabulate.tabulate(rows, header))
            return contact_details
        else:
            print("No contacts find")

    @classmethod
    def removePersonContact(cls,filepath):
        """
        Function to remove specified contact details from the addressbook
        """
        # Try to open the current addressbook and find the person contact
        address_books = cls.open_addressbook(filepath)
        persons = addressbook.retrievePersonContact(filepath)

        if persons:
            try:
                with open(filepath, 'w') as outfile:
                    # If contact was found delete it
                    for person in persons:
                        address_books['persons'].remove(person)
                    json.dump(address_books, outfile, indent= 4)
                    print('Contact removed.')
            finally:
                outfile.close()

    @classmethod
    def modify_contact(cls,filepath):
        '''
        Function to modify specified contact details in the addressbook
        '''
        address_books = cls.open_addressbook(filepath)
        if address_books:
            fname= (input("Enter the first name of the contact to be modified: "))
            is_contact_modified=False
            for person in address_books['persons']:
                if person['fname'].casefold() == fname.casefold():
                    cls.do_modification(person)
                    with open(filepath, 'w') as outfile:
                        json.dump(address_books, outfile, indent= 4)
                    is_contact_modified=True
                    print("Contact modified")
                    break
            if not is_contact_modified:
                print("No contact with this name found")
        else:
            print("Address book empty. No contact to modified")

    @classmethod
    def do_modification(cls, contact):
        '''
        Function to modifiy specified contact here
        '''
        try:
            while True:
                print ("Enter 1. to modify city\n2. to modify state\n3. to modify phone no\n4.quit without modifying")
                choice= int(input())
                if choice == 1:
                    new_city = input("Enter new city name: ")
                    contact['city'] = new_city
                    break
                elif choice == 2:
                    new_state = input("Enter new state name: ")
                    contact['state'] = new_state
                    break
                elif choice == 3:
                    new_phone = input('Enter new phone number: ')
                    contact['phone'] = new_phone
                    break
                else:
                    print("Incorrect choice")
                    break
        except EOFError:
            print("EOF Error occurred")
        except KeyboardInterrupt:
            print("KeyboardInterrupt occurred")

    @classmethod
    def sortContact(cls,filepath):
        '''
        Function to sort the entries in the address book alphabetically 
        by last name (with ties broken by first name if necessary)
        '''
        address_books = cls.open_addressbook(filepath)
        if address_books:
            sort_contact = sorted(address_books['persons'], key = lambda person: (person['lname'], person['fname']))
            header = sort_contact[0].keys()
            rows =  [x.values() for x in sort_contact]
            print(tabulate.tabulate(rows, header))
        else:
            print('No address book found!')

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Open Address book(load json file)
    2.Print all person contacts
    3.Add new person contact in address book
    4.Retirve specified contact details in the addressbook
    5.Remove specified contact details from the addressbook
    6.Modify specified contact details in the addressbook
    7.Sort contact by last name
    ''')

def switchToFunction(case,filepath):
    '''
    Create switch function to move perticular program
    '''
    obj = addressbook
    switcher = {
        1 : obj.open_addressbook,
        2 : obj.printAllContacts,
        3 : obj.add_contact,
        4 : obj.retrievePersonContact,
        5 : obj.removePersonContact,
        6 : obj.modify_contact,
        7 : obj.sortContact
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    func(filepath)

def main():
    menu()
    choice = int(input("Enter which program you want to run: "))
    FILE_PATH = "data/address_book_file.json"
    switchToFunction(choice,FILE_PATH)
    options = input('Do you want to continue?[y/n]: ')
    if options.lower() == 'y':
        main()
    else:
        exit()

if __name__ == "__main__":
    main()