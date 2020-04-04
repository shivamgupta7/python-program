from array import *

class programArray:

    def create_int_array(self, lst):
        '''
        Create an array of 5 integers and display the array items.
        Access individual element through indexes.
        '''
        array_num = array('i', lst)
        for ele in array_num:
            print(ele)
        return array_num[0], array_num[1], array_num[2], array_num[3], array_num[4]

    def reverse_array(self, lst):
        '''
        Reverse the order of the items in the array.
        '''
        self.array_num = array('i', lst)
        self.array_num.reverse()
        return self.array_num

def main():
    obj = programArray()
    print(obj.create_int_array([3,5,2,8,7]))
    print(obj.reverse_array([3,5,2,8,7]))

if __name__ == "__main__":
    main()