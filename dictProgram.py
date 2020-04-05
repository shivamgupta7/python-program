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

    def dictSort_by_value(self,mydict,sort_by='ASC'):
        '''
        Sorting algorithms for dictionary using bubble sort.
        '''
        d_items = list(mydict.items())
        for j in range(len(d_items) - 1):
            for i in range(len(d_items) - 1):
                d_items[i], d_items[i+1] = self.order(d_items[i], d_items[i+1],sort_by)
        return dict(d_items)

def main():
    obj = programDictionary()
    print(obj.dictSort_by_value({1: 2, 3: 4, 4: 3, 2: 1, 0: 0}))
    print(obj.dictSort_by_value({1: 2, 3: 4, 4: 3, 2: 1, 0: 0},'DESC'))

if __name__ == "__main__":
    main()