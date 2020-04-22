from array import *

class programArray:

    def create_int_array(self, lst):
        '''
        Create an array of 5 integers and display the array items.
        Access individual element through indexes.
        '''
        array_num = array('i', lst)
        print(*array_num)
        return array_num[0], array_num[1], array_num[2], array_num[3], array_num[4]

    def reverse_array(self, lst):
        '''
        Reverse the order of the items in the array.
        '''
        self.new_array = array('i',[])
        self.array_num = array('i', lst)
        for index in range(len(self.array_num)-1,-1,-1):
            self.new_array.append(self.array_num[index])
        return self.new_array

    def count_occurrence(self, lst):
        '''
        Get the number of occurrences of a specified element in an array.
        '''
        self.array_num = array('i', lst)
        self.element = int(input("Enter the element for find number of occurrences : "))
        self.occurr = 0
        for item in self.array_num:
            if item == self.element:
                self.occurr += 1
        return self.occurr

    def remove_occurrence(self, lst):
        '''
        Remove the first occurrence of a specified element from an array.
        '''
        self.array_num = array('i', lst)
        self.element = int(input("Enter the element for remove the first occurrences : "))
        self.array_num.remove(self.element)
        return self.array_num

def main():
    obj = programArray()
    print(obj.create_int_array([3,5,2,8,7]))
    print(obj.reverse_array([3,5,2,8,7]))
    print(obj.count_occurrence([1, 3, 6, 4, 3, 7, 3, 9, 3]))
    print(obj.remove_occurrence([1, 3, 6, 4, 3, 7, 3, 9, 3]))

if __name__ == "__main__":
    main()