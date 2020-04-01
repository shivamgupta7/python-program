class programWeek1:
    
    def reverse_name(self):
        self.fname = input("Enter your First name : ")   # take input from user
        self.lname = input("Enter your Last name : ")    # take input from user
        print(self.fname[::-1],self.lname[::-1])         # reverse first and last name 
    
    def list_tuple(self):
        self.number = input("Input some comma seprated numbers : ")   # take input from user
        self.list = self.number.split(",")   # split() method splits a string into a list.
        self.tuple = tuple(self.list)        # convert list to tuple using tuple() function.
        print('List : ',self.list)
        print('Tuple : ',self.tuple)

def main():
    obj = programWeek1()   # create object of class
    obj.reverse_name()     # calling methods(function) in class
    obj.list_tuple()

if __name__ == "__main__":
    main()