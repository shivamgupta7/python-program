import random
from random import shuffle

def RANKS():
    return [ "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King", "Ace" ]

def SUITS():
    return [ "Clubs", "Diamonds", "Hearts", "Spades" ]

class Card:

    def __init__( self, rank, suit ):
        self.rank = rank
        self.suit = suit

    def __str__( self ):
        return self.rank + " of " + self.suit

class Deck:

    def __init__( self ):
        self.contents = []
        self.contents = [ Card(rank, suit ) for rank in RANKS() for suit in SUITS() ]
        random.shuffle( self.contents )

class Players:

    def __init__(self):
        self.obj = Deck()

    def player1(self, n):
        print("\nPlayer 1 Gets:-\n")
        for index in range(n):
            print(self.obj.contents[index])
            self.obj.contents.remove(self.obj.contents[index])  # deleting the selected card from the list to avoid the repetition of card
        return self.obj.contents

    def player2(self, n):
        print("\nPlayer 2 Gets:-\n")
        for index in range(n):
            print(self.obj.contents[index])
            self.obj.contents.remove(self.obj.contents[index])
        return self.obj.contents

    def player3(self, n):
        print("\nPlayer 3 Gets:-\n")
        for index in range(n):
            print(self.obj.contents[index])
            self.obj.contents.remove(self.obj.contents[index])
        return self.obj.contents

    def player4(self, n):
        print("\nPlayer 4 Gets:-\n")
        for index in range(n):
            print(self.obj.contents[index])
        return self.obj.contents

# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    # calling all the function to to distribute the cards randomly
    player = Players()
    player.player1(9)
    player.player2(9)
    player.player3(9)
    player.player4(9)