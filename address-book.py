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