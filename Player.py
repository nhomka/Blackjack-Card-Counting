from CardFunctions import *
import time

class Player(object):
    """description of class"""
    is_dealer = False
    hidden_card = None

    def __init__(self, name, is_dealer = False):

        self.name = name
        self.is_dealer = is_dealer
        self.hand = []
        self.bank = 1000
        self.bet = 0
        self.hand_total = 0
        self.hold = False
        self.over = False

        self.hand_split1 = []
        self.hand_split2 = []
        self.bet_split1 = 0
        self.bet_split2 = 0
        self.hand_total_split1 = 0
        self.hand_total_split2 = 0
        self.hold_split1 = False
        self.hold_split2 = False
        self.over_split1 = False
        self.over_split2 = False

    def deal_shown_card(self, deck, hand=None):
        if hand == None:
            hand = self.hand
        hand.append(deck.deal_card())
        if self.compute_hand_total(hand) > 21:
            if hand == self.hand:
                self.over = True
                return True
            else:
                return True
        else:
            return False

    def deal_hidden_card(self, deck):
        if self.hidden_card == None:
            self.hand.append("hidden_card")
            self.hidden_card = deck.deal_card()
        else:
            print("player " + name + " already has a hidden card")
        self.hand_total = self.compute_hand_total()

    def show_hidden_card(self):
        if self.hidden_card != None:
            self.hand.pop()
            self.hand.append(self.hidden_card)
            self.hidden_card = None
        else:
            print("no hidden card to show.")
        self.hand_total = self.compute_hand_total()

    def compute_hand_total(self, hand = None):
        if hand == None:
            hand = self.hand

        hand_value = 0
        for card in hand:
            hand_value += CardFunctions.get_card_value(card, hand_value)
            
        has_ace = False
        for card in hand:
            if card[0].capitalize() == "A": 
                has_ace = True
                
        if has_ace:
            if hand_value <= 11:
                hand_value += 10

        return hand_value

    def place_bet(self):
        bet = int(input(self.name + ", enter the amount you would like to bet.  You have: " + str(self.bank) + " dollars.\r\n"))

        if bet <= self.bank:
            self.bank -= bet
            return bet
        else:
            response = input("you do not have sufficient funds to place this bet.  You can place a new bet or skip the round.  Place a new bet? (Y/N)")
            if response.capitalize() == "Y":
                self.place_bet()
            else:
                return 0

    def place_optimal_bet(self, deck, table_minimum):
        time.sleep(.5)
        true_count = deck.get_true_count()
        starting_bet = table_minimum * 4
        bet = true_count * starting_bet

        if bet <= self.bank:
            self.bank -= bet
            print(self.name + " is betting " + str(bet))
            return bet

        else:
            bet = self.bank
            self.bank = 0
            print(self.name + " is betting " + str(bet))
            return bet

    def double(self):
        if self.bet <= self.bank:
            self.bank -= self.bet
            self.bet = self.bet * 2
            return self.bet

    def manual_play(self, deck, hand=None):
        if hand == None:
            hand = self.hand
        while not self.hold and not self.over:
            hit_status = input(self.name + ", your hand is: " + str(hand) + ". With a total value of: " + str(self.compute_hand_total(hand)) + ". Hit or stay? (H/S)\r\n")
            if hit_status.capitalize() == "H":
                if self.deal_shown_card(deck, hand):
                    print(self.name + ", you went over with a hand of: " + str(hand))
                    return self.compute_hand_total(hand)
            else:
                print(self.name + ", you are staying with a hand total of: " + str(self.compute_hand_total(hand)))
                return self.compute_hand_total(hand)

    def hand_is_hard(self, hand=None):
        if hand == None:
            hand = self.hand

        hand_value = 0
        for card in hand:
            hand_value += CardFunctions.get_card_value(card, hand_value)

        has_ace = False
        for card in self.hand:
            if card[0].capitalize() == "A": 
                has_ace = True

        if has_ace:
            if hand_value <= 11:
                return False
            else:
                return True
        else:
            return True

    def hand_can_split(self, hand=None):
        if hand == None:
            hand = self.hand

        tens = ['1', 'J', 'Q', 'K']
        if len(hand) == 2 and (hand[0][0] == hand[1][0] or (hand[0][0] in tens and hand[1][0] in tens)):
            return True
        else:
            return False

    def split(self, bet, deck, hand=None):
        if hand == None:
            hand = self.hand

        if bank > bet:
            bank -= bet
            self.bet_split1 = bet

            self.hand_split1.append(self.hand.pop())
            self.hand_split1.append(deck.deal_card())
            self.hand_total_split1 = self.compute_hand_total(hand_split1)
            if self.hand_total_split1 > 21:
                self.over = True


    def hold_hand(self):
        self.hold = True

    def wins(self, bet):
        self.bank += 2*bet

    def pushes(self, bet):
        self.bank += bet

    def reset(self):
        self.hand = []
        self.bet = 0
        self.hand_total = 0
        self.hidden_card = None
        self.hold = False
        self.over = False