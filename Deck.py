import itertools
import random

class Deck(object):
    """description of class"""
    number_of_decks = 1
    used_cards = []
    remaining_cards = []
    running_count = 0
    true_count = 0
    bad_cards_list = ['1', 'J', 'Q', 'K', 'A']
    good_cards_list = ['2', '3', '4', '5', '6']

    def __init__(self, number_of_decks):

        self.number_of_decks = number_of_decks
        self.shuffle()

    def shuffle(self):
        deck = self.get_fresh_deck()
        deck_list = list(itertools.chain.from_iterable([[i] * deck[i] for i in deck]))
        self.remaining_cards = deck_list
        random.shuffle(self.remaining_cards)
        print(self.remaining_cards)

    def deal_card(self):
        card = self.remaining_cards.pop()
        if card[0] in self.bad_cards_list:
            self.running_count -= 1
        elif card[0] in self.good_cards_list:
            self.running_count += 1
        return card

    def get_running_count(self):
        return self.running_count

    def get_true_count(self):
        self.true_count = int(self.running_count / (len(remaining_cards) / 52))
        return true_count

    def get_fresh_deck(self):
        nd = self.number_of_decks
        deck = {
            '2C' : nd,
            '2D' : nd,
            '2H' : nd,
            '2S' : nd,
            '3C' : nd,
            '3D' : nd,
            '3H' : nd,
            '3S' : nd,
            '4C' : nd,
            '4D' : nd,
            '4H' : nd,
            '4S' : nd,
            '5C' : nd,
            '5D' : nd,
            '5H' : nd,
            '5S' : nd,
            '6C' : nd,
            '6D' : nd,
            '6H' : nd,
            '6S' : nd,
            '7C' : nd,
            '7D' : nd,
            '7H' : nd,
            '7S' : nd,
            '8C' : nd,
            '8D' : nd,
            '8H' : nd,
            '8S' : nd,
            '9C' : nd,
            '9D' : nd,
            '9H' : nd,
            '9S' : nd,
            '10C' : nd,
            '10D' : nd,
            '10H' : nd,
            '10S' : nd,
            'JC' : nd,
            'JD' : nd,
            'JH' : nd,
            'JS' : nd,
            'QC' : nd,
            'QD' : nd,
            'QH' : nd,
            'QS' : nd,
            'KC' : nd,
            'KD' : nd,
            'KH' : nd,
            'KS' : nd,
            'AC' : nd,
            'AD' : nd,
            'AH' : nd,
            'AS' : nd
            }
        return deck