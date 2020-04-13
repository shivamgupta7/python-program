import json, os

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
        else:
            print('File does not exist.')
        return addressbook

    @classmethod
    def printAllContacts(cls,filepath):
        """
        Function to print list of all contacts details in the addressbook as form of tables.
        """
        address_books = cls.open_addressbook(filepath)
        if address_books:
            print("{:<10} {:<10} {:<30} {:<10} {:<15} {:<10} {:<10}".format('FNAME', 'LNAME', 'ADDRESS', 'CITY', 'STATE', 'ZIP CODE', 'PHONE NO'))
            for person in address_books['persons']:
                print("{:<10} {:<10} {:<30} {:<10} {:<15} {:<10} {:<10}".format(person['fname'],person['lname'],person['address'],person['city'],person['state'],person['zipCode'],person['phone']))
        else:
            print('No address book found!')

def menu():
    '''
    Menu of programs
    '''
    print('''
    1.Open Address book(load json file)
    2.Print all person contacts
    ''')

def switchToFunction(case,filepath):
    '''
    Create switch function to move perticular program
    '''
    obj = addressbook
    switcher = {
        1 : lambda: obj.open_addressbook(filepath),
        2 : lambda: obj.printAllContacts(filepath),
        }
    func = switcher.get(case, lambda: 'Invalid choice please select correct options.')
    func()

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