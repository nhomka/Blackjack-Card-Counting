class CardFunctions(object):
    """description of class"""

    def get_card_value(card, current_value):
        value = 0
        if card[0].isnumeric():
            if card[0] == "1":
                value = 10
            else:
                value = int(card[0])
        elif card[0].capitalize() == 'A':
            value = 1
        else:
            value = 10
        return value