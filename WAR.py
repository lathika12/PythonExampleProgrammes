#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

LIST_MAIN = []
LIST_SYS = []
LIST_PLR =[]
LIST_DRW = []


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """

    def __init__(self):
        print("Initializing the deck of cards.")
        Deck.creatingDeck()
        Deck.shuffleDeck(LIST_MAIN)
        Deck.splitDecks(LIST_MAIN)

    def creatingDeck():
        # Creating 52 elements to shuffle
        for k in SUITE:
            for l in RANKS:
                LIST_MAIN.append(k+l)

    def shuffleDeck(dck):
        # shuffling the given  deck
        shuffle(dck)

    def splitDecks(dck):
        LIST_PLR.extend(dck[:26])
        LIST_SYS.extend(dck[26:])


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''

    def __init__(self,player):
        print("Playing For Current Hand")
        self.player = player

    def add_card(self,card):
        print("Inside add card with card : " , card)
        LIST_PLR.append(card)
        LIST_SYS.remove(card)

    def remove_card(self,card):
        print("Inside remove card with card : " , card)
        LIST_PLR.remove(card)
        LIST_SYS.append(card)

    def draw_hand(self,card1,card2):
        print("Inside draw hand card with card : " , card1, card2)
        LIST_DRW.append(card1)
        LIST_DRW.append(card2)
        LIST_PLR.remove(card1)
        LIST_SYS.remove(card2)

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def __init__(self, name):
        self.name = name
        self.hand = Hand(self.name)
        print("Inside player : " + self.name)

    def playHand(self,crd_sys,crd_pl):
        sy = RANKS.index(crd_sys[0][1:])
        pl = RANKS.index(crd_pl[0][1:])
        print("Playing :  {0}  for System \n and \nPlaying :  {1}  for player".format(sy,pl))
        if(sy>pl):
            print("SYSTEM GOT THIS ROUND")
            self.hand.remove_card(crd_pl[0])
        elif(pl>sy):
            print("PLAYER" + self.name + " GOT THIS ROUND")
            self.hand.add_card(crd_sys[0])
        else:
            print("It is a draw")
            self.hand.draw_hand(crd_pl[0],crd_sys[0])


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
# Use the 3 classes along with some logic to play a game of war!
print("+++++++++++++++++++++++++++++++++")
# Initialize the player
name = input("Welcome player, please enter your name: ")

# Sort the deck into two lists - system and player
print("Initializing your deck")
deck = Deck()
print("\n ++++++++++++++++++++++++++++++++++ \n")

print(LIST_DRW,LIST_PLR,LIST_SYS,LIST_MAIN)

ip = input("READY TO BEGIN? Press y/n : ")
ip = ip.lower()

if(ip == 'y'):
    #playing multiple hands as you go
    player = Player(name)
    print("Looping")
    for m in range(100):
        print("LISTS:" , LIST_DRW, "\n", LIST_PLR , "\n", LIST_SYS)

        if(len(LIST_SYS) != 0 and len(LIST_PLR) != 0):
            print("INSIDE FOR LOOP :" , m)
            player.playHand(LIST_SYS,LIST_PLR)
        else:
            break

# Ask the player if he wants to start playing hands
