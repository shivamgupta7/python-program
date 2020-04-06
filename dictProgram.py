class programDictionary:

    def order(self, value1, value2, sort_by = 'ASC'):
        '''
        Comparision b/w two values
        '''
        if sort_by == 'DESC':
            if value1[1] > value2[1]:
                return value1, value2
            else:
                return value2, value1
        elif sort_by == 'ASC':
            if value1[1] < value2[1]:
                return value1, value2
            else:
                return value2, value1
        else:
            print('Argument sort_by is wrong. Please check it.')

    def dictSort_by_value(self, mydict,sort_by='ASC'):
        '''
        Sorting algorithms for dictionary using bubble sort.
        '''
        self.d_items = list(mydict.items())
        for index in range(len(self.d_items)):
            for next_index in range(index+1, len(self.d_items)):
                self.d_items[index], self.d_items[next_index] = self.order(self.d_items[index], self.d_items[next_index],sort_by)
        return dict(self.d_items)

    def add_new_key(self, mydict, element):
        '''
        Add a key to a dictionary
        '''
        mydict.update(element)
        return mydict

    def concatenate_dict(self):
        '''
        Concatenate following dictionaries to create a new one.
        '''
        self.new_dict = {}
        self.total_dict = int(input("How many dictionary you have? : "))
        for times in range(self.total_dict):
            self.dictionary = eval(input("Enter {0} dectionary(format {{key: value}}) :".format(times+1)))
            self.new_dict.update(self.dictionary)
        return self.new_dict

    def iterate_dict(self, mydict):
        '''
        Iterate over dictionaries using for loops.
        '''
        for key, value in mydict.items():
            print(key,"--->",value)

def main():
    obj = programDictionary()
    print(obj.dictSort_by_value({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
    print(obj.dictSort_by_value({1: 2, 3: 4, 4: 3, 2: 1, 0: 0},'DESC'))
    print(obj.add_new_key({1: 2, 3: 4, 4: 3, 2: 1, 0: 0},{5:7}))
    print(obj.concatenate_dict())
    print(obj.iterate_dict({5: 50, 6: 60, 3: 30, 4: 40}))

if __name__ == "__main__":
    main()