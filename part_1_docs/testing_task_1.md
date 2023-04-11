### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # should be '==' instead of '='. '=' assigns a new value to card.value, rather than comparing it
      return True
    else # there should be a ':' immediately after 'else'
      return False
   

  dif highest_card(self, card1 card2): # should be 'def' rather than 'dif', which is not a keyword.
                                       # There should also be a comma between card1 and card2
  if card1.value > card2.value: # function content should be indented
    return card # should be 'card1' rather than 'card2'
  else:
    return card2

def cards_total(self, cards): # whole function should be indented
  total # should be initialised with a value, likely 0.
  for card in cards:
    total += card.value
    return "You have a total of" + total # should not be in for loop, should cast total to string
  
```
