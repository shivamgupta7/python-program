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

    def storeSquares_in_dict(self):
        '''
        Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
        '''
        self.dictionary = {}
        self.number = int(input("Input a number(range) : "))
        for num in range(1,self.number+1):
            self.dictionary[num] = num*num
        return self.dictionary

    def delete_key(self, mydict):
        '''
        Remove a key from a dictionary.
        '''
        key = int(input("Enter which key you want to delete : "))
        if key in mydict:
            del mydict[key]
        return mydict

    def uniqueValues_in_dict(self, listOfmydict):
        '''
        unique values in a dictionary.
        '''
        self.uniqueValues = set(values for dic in listOfmydict for values in dic.values())
        return self.uniqueValues

    def frequency_Of_char(self, string):
        '''
        create a dictionary from a string.
        Note: Track the count of the letters from the string.
        '''
        self.all_freq = {} 
        for i in string:
            if i in self.all_freq: 
                self.all_freq[i] += 1
            else: 
                self.all_freq[i] = 1
        return self.all_freq

    def dict_to_table(self):
        '''
        Print a dictionary in table format.
        '''
        data = {1: ["Rohit", 22, 'Data Structures'], 
                 2: ["Shivam", 21, 'Machine Learning'], 
                 3: ["Himanshu", 23, 'Networking']} 
   
        print ("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))  
        for value in data.values(): 
            name, age, course = value 
            print ("{:<10} {:<10} {:<10}".format(name, age, course))

    def count_value_associated_key(self):
        '''
        Count the values associated with key in a dictionary.
        '''
        data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
        counts = sum(dic['success'] for dic in data)
        return counts

    def check_multiple_key(self, mydict):
        '''
        Check multiple keys exists in a dictionary.
        '''
        keys = [int(x) for x in input("Enter the key(one or more seprated by space) which you want to check: ").split()]
        if all(key in mydict for key in keys):
            return True
        else: 
            return False

def main():
    obj = programDictionary()
    print(obj.dictSort_by_value({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
    print(obj.dictSort_by_value({1: 2, 3: 4, 4: 3, 2: 1, 0: 0},'DESC'))
    print(obj.add_new_key({1: 2, 3: 4, 4: 3, 2: 1, 0: 0},{5:7}))
    print(obj.concatenate_dict())
    print(obj.iterate_dict({5: 50, 6: 60, 3: 30, 4: 40}))
    print(obj.storeSquares_in_dict())
    print(obj.delete_key({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
    print(obj.uniqueValues_in_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))
    print(obj.frequency_Of_char('abcaacddbegfb'))
    obj.dict_to_table()
    print(obj.count_value_associated_key())
    print(obj.check_multiple_key({5: 50, 6: 60, 3: 30, 4: 40}))

if __name__ == "__main__":
    main()