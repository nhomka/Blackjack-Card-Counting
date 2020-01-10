import Player
class Round(object):
    """description of class"""
    players = None
    deck = []
    bets = {}
    scores = {}
    dealer = None

    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        
        for player in self.players:
            self.bets[player] = 0
            self.scores[player] = 0
            if player.is_dealer:
                self.dealer = player

    def play_out_round(self):
        self.place_bets()
        self.initial_deal()

        for player in self.players:
            print(player.name + "(bet = " + str(self.bets[player]) + "): " + str(player.hand) + ": " + str(player.compute_hand_total()))

        self.continue_round()

        self.dealers_turn()
        
        for player in self.players:
            print(player.name + ": " + str(player.hand) + ": " + str(player.compute_hand_total()))

        self.determine_payouts()

        self.reset()

    def initial_deal(self):
        for player in self.players:
            player.deal_shown_card(self.deck)

        for player in self.players:
            if not player.is_dealer:
                player.deal_shown_card(self.deck)
            else:
                player.deal_hidden_card(self.deck)

    def continue_round(self):
        for player in self.players:
            while not player.hold and not player.is_dealer and not player.over:
                if player.hand_can_split():
                    split_status = input(player.name + ", your hand is: " + str(player.hand) + ". With a total value of: " + str(player.hand_total) + ". Split? (Y/N)\r\n")
                    if split_status.capitalize() == "Y":
                        player.split(self.bets[player], self.deck) #TODO
                else:
                    self.scores[player] = player.manual_play(self.deck) #TODO
                    player.hold = True

    def continue_round_optimally(self):
        for player in self.players:
            if not player.is_dealer and not player.over:
                return

    def optimal_hit_or_stay(self, player):
        dealer = self.dealer
        shown_card = dealer.hand[0][0]
        if player.hand_is_hard():
            return #TODO

    def dealers_turn(self):
        dealer = self.dealer
        dealer.show_hidden_card()
        while not dealer.hold and not dealer.over:
            hit_status = input(dealer.name + ", your hand is: " + str(dealer.hand) + ". With a total value of: " + str(dealer.compute_hand_total()) + ". Hit or stay? (H/S)\r\n")
            if hit_status == "H":
                dealer.deal_shown_card(self.deck)
                if dealer.over:
                    print(dealer.name + ", you went over with a hand of: " + str(dealer.hand))
            else:
                print(dealer.name + ", you are staying with a hand total of: " + str(dealer.compute_hand_total()))
                dealer.hold = True
                self.scores[self.dealer] = self.dealer.compute_hand_total()
            

    def determine_payouts(self):
        for player in self.players:
            if not player.is_dealer:
                if (self.scores[player] > self.scores[self.dealer] and not player.over) or (not player.over and self.dealer.over):
                    player.wins(self.bets[player])
                    print(player.name + " has won " + str(self.bets[player]) + " dollars.")
                elif (self.scores[player] == self.scores[self.dealer] and not player.over):
                    player.pushes(self.bets[player])
                    print("PUSH! " + player.name + " has tied and is returned their bet of " + str(self.bets[player]) + " dollars.")
                else:
                    print(player.name + " has lost " + str(self.bets[player]) + " dollars.")

    def place_bets(self):
        for player in self.players:
            if not player.is_dealer:
                self.bets[player] = player.place_bet()

    def reset(self):
        for player in self.players:
            player.reset()