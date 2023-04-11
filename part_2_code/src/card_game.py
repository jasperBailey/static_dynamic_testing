### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:


    def check_for_ace(self, card):
        if card.value == 1: # should be '==' instead of '='. '=' assigns a new value to card.value, rather than comparing it
            return True
        else: # there should be a ':' immediately after 'else'
            return False
   

    def highest_card(self, card1, card2): # should be 'def' rather than 'dif', which is not a keyword.
                                       # There should also be a comma between card1 and card2
        if card1.value > card2.value:
            return card1 # should be 'card1' rather than 'card2'
        else:
            return card2

    def cards_total(self, cards): # whole function should be indented
        total = 0 # should be initialised with a value, likely 0.
        for card in cards:
            total += card.value
        return "You have a total of " + str(total) # should not be in for loop, should cast total to string