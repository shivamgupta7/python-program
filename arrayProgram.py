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

def main():
    obj = programArray()
    print(obj.create_int_array([3,5,2,8,7]))

if __name__ == "__main__":
    main()