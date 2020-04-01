class programWeek1:
    
    def reverse_name(self):
        self.fname = input("Enter your First name : ")   # take input from user
        self.lname = input("Enter your Last name : ")    # take input from user
        print(self.fname[::-1],self.lname[::-1])         # reverse first and last name 


obj = programWeek1()   # create object of class
obj.reverse_name()     # calling methods(function) in class