import random
from random import shuffle

def RANKS():
    return [ "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace" ]

def SUITS():
    return [ "Clubs", "Diamonds", "Hearts", "Spades" ]

def num_rank(rank):
    if rank[0] == "J":
         return 11
    elif rank[0] == "Q":
         return 13
    elif rank[0] == "K":
         return 13
    elif rank[0] == "A":
         return 14
    return int(rank)

def bubble_sort(lst):
    length = len(lst)
    #repeating loop len(a)(number of elements) number of times
    for _ in range(length):
        #initially swapped is false
        swapped = False
        index = 0
        while index < length-1:
            #comparing the adjacent elements
            if lst[index] > lst[index+1]:
                #swapping
                lst[index],lst[index+1] = lst[index+1],lst[index]
                #Changing the value of swapped
                swapped = True
            index += 1
        #if swapped is false then the list is sorted
        #we can stop the loop
        if swapped == False:
            break
    return lst

class Card:

    def __init__( self, rank, suit ):
        self.rank = rank
        self.suit = suit

    def __str__( self ):
        return self.rank + " of " + self.suit

    def __lt__(self, other):
        tup1 = self.suit, num_rank(self.rank)
        tup2 = other.suit, num_rank(other.rank)
        return tup1 < tup2

class Deck:

    def __init__( self ):
        self.contents = []
        self.contents = [ Card(rank, suit ) for rank in RANKS() for suit in SUITS() ]
        random.shuffle( self.contents )

class Players:

    def __init__(self):
        self.obj = Deck()

    def player1(self, n):
        cards = []
        print("\nPlayer 1 Gets:-\n")
        for index in range(n):
            cards.append(self.obj.contents[index])
            # print(self.obj.contents[index])
            self.obj.contents.remove(self.obj.contents[index])  # deleting the selected card from the list to avoid the repetition of card
        sort_card = bubble_sort(cards)
        print(*sort_card, sep='\n')
        return sort_card

    def player2(self, n):
        cards = []
        print("\nPlayer 2 Gets:-\n")
        for index in range(n):
            cards.append(self.obj.contents[index])
            # print(self.obj.contents[index])
            self.obj.contents.remove(self.obj.contents[index])
        sort_card = bubble_sort(cards)
        print(*sort_card, sep='\n')
        return sort_card

    def player3(self, n):
        cards = []
        print("\nPlayer 3 Gets:-\n")
        for index in range(n):
            cards.append(self.obj.contents[index])
            # print(self.obj.contents[index])
            self.obj.contents.remove(self.obj.contents[index])
        sort_card = bubble_sort(cards)
        print(*sort_card, sep='\n')
        return sort_card

    def player4(self, n):
        cards = []
        print("\nPlayer 4 Gets:-\n")
        for index in range(n):
            cards.append(self.obj.contents[index])
            # print(self.obj.contents[index])
        sort_card = bubble_sort(cards)
        print(*sort_card, sep='\n')
        return sort_card

# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    # calling all the function to to distribute the cards randomly
    player = Players()
    player.player1(9)
    player.player2(9)
    player.player3(9)
    player.player4(9)