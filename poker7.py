def get_card_value(card):
    """Returns the numeric value of the card.
        For this function, Jacks have value 11, Queens have value 12, Kings have value 13, and Aces have value 14
        Returns None for invalid cards
    """
    try:
        value_list = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        return value_list.index(card[:-1])+2
    except:
        return None

def get_card_suit(card):
    """Returns the suit of the card, which can take the values "H", "D", "S", or "C".
    """
    return card[-1]

def count_values(lst):
    """Determines the number of times each value of card appears in the list.
    """
    numbers = [0] * 15
    for card in lst:
        numbers[get_card_value(card)] += 1
    return numbers

def get_best_hand(lst):
    """Returns the best possible hand in the list of cards lst as a tuple (value, name)
        where value is a numeric value to measure the value of the best hand, and
        name is a string to indicate the best hand.
    """
    if has_straight_flush(lst):
        return (22, "Straight flush")
    elif has_four_of_a_kind(lst):
        return (21, "Four of a kind")
    elif has_full_house(lst):
        return (20, "Full house")
    elif has_flush(lst):
        return (19, "Flush")
    elif has_straight(lst):
        return (18, "Straight")
    elif has_three_of_a_kind(lst):
        return (17, "Three of a kind")
    elif has_two_pairs(lst):
        return (16, "Two pairs")
    elif has_pair(lst):
        return (15, "Pair")
    else:
        highcard = 14
        while count_values(lst)[highcard] == 0:
            highcard -= 1
        return (highcard, "High card " + str((list(range(11)) + ["Jack","Queen","King","Ace"])[highcard]))

def holdem(community_cards, player_cards):
    """Determines the winner of a game of Texas Hold'Em.
        The community cards is a list of cards, while player_cards is a list of lists of cards
    """
    current_best_player = -1
    current_best_hand = (-1, "Everybody loses")
    for player in range(len(player_cards)):
        current_player_best_hand = get_best_hand(community_cards + player_cards[player])
        if current_player_best_hand[0] > current_best_hand[0]:
            current_best_player = player
            current_best_hand = current_player_best_hand
    print("Player", current_best_player, "wins with a", current_best_hand[1])
    return current_player_best_hand

def _do_test(name, passed):
    """Prints the test results to screen
    """
    if passed:
        print(name + " passed!")
    else:
        print(name + " failed!")

def tester():
    """Tests some of the functions.
    """
    _do_test("Straight test 1",has_straight(["5D","6D","7D","8D","9D","10D","JD"]))
    # Straight flush: 7-8-9-10-J of diamonds
    _do_test("Straight test 2",has_straight(["AD","2S","3S","4C","9D","10D","5H"]))
    # Straight: A-2-3-4-5
    _do_test("Straight test 3",has_straight(["AD","JD","7D","QH","KH","10S","JS"]))
    # Straight: 10-J-Q-K-A
    _do_test("Straight test 4",not has_straight(["5D","7D","9D","JD","KD","AD","2D"]))
    _do_test("Flush test 1",has_flush(["5D","6D","7D","8D","9D","10D","JD"]))
    # Straight flush: 7-8-9-10-J of diamonds
    _do_test("Flush test 2",not has_flush(["AD","2S","3S","4C","9D","10D","5H"]))
    _do_test("Flush test 3",not has_flush(["AD","JD","7D","QH","KH","10S","JS"]))
    _do_test("Flush test 4",has_flush(["5H","7D","9H","JH","KH","AD","2H"]))
    # Flush: 7-9-J-K-A of diamonds
    _do_test("Straight flush test 1",has_straight_flush(["5D","6D","7D","8D","9D","10D","JD"]))
    # Straight flush: 7-8-9-10-J of diamonds
    _do_test("Straight flush test 2",not has_straight_flush(["AD","2S","3S","4C","9D","10D","5H"]))
    # Straight:A-2-3-4-5
    _do_test("Straight flush test 3",not has_straight_flush(["AD","JD","7D","QH","KH","10D","QD"]))
    # Flush: 7-10-J-Q-A of diamonds, Straight: 10-J-Q-K-A
    _do_test("Straight flush test 4",not has_straight_flush(["5H","7D","9H","JH","KH","AD","2H"]))
    # Flush: 2-5-9-J-H of hearts
    _do_test("Four of a kind test 1",has_four_of_a_kind(["AH","AD","9H","JH","KH","AS","AC"]))
    # Four of a kind: Aces
    _do_test("Four of a kind test 2",not has_four_of_a_kind(["AH","10D","9H","JH","KH","AS","AC"]))
    # Three of a kind: Aces
    _do_test("Four of a kind test 3",has_four_of_a_kind(["AH","2D","3H","4D","4H","4S","4C"]))
    # Four of a kind: 4
    _do_test("Three of a kind test 1",has_three_of_a_kind(["AH","AD","9H","JH","KH","AS","AC"]))
    # Four of a kind: Aces
    _do_test("Three of a kind test 2",has_three_of_a_kind(["AH","3D","3H","3S","4C","AS","AC"]))
    # Three of a kind: Aces, three of a kind: 3, full house: Aces over 3
    _do_test("Three of a kind test 3",not has_three_of_a_kind(["AH","2D","3H","4D","5H","6S","4C"]))
    # Pair: 4
    _do_test("Full house test 1",not has_full_house(["AH","AD","9H","JH","KH","AS","AC"]))
    # Four of a kind: Aces
    _do_test("Full house test 2",has_full_house(["AH","3D","3H","3S","3C","AS","AC"]))
    # Full house: Aces over 3
    _do_test("Full house test 3",not has_full_house(["AH","2D","4H","4D","5H","6S","4C"]))
    # Three of a kind: 4
    _do_test("Two pairs test 1",not has_two_pairs(["AH","AD","9H","JH","KH","AS","AC"]))
    # Four of a kind: Aces
    _do_test("Two pairs test 2",has_two_pairs(["AH","3D","3H","3S","3C","AS","AC"]))
    # Three of a kind: Aces, three of a kind: 3, full house: Aces over 3
    _do_test("Two pairs test 3",not has_two_pairs(["AH","2D","3H","4D","5H","6S","4C"]))
    # Pair: 4
    _do_test("Pair test 1",has_pair(["AH","AD","9H","JH","KH","AS","AC"]))
    # Pair: Aces
    _do_test("Pair test 2",has_pair(["AH","3D","3H","3S","3C","AS","AC"]))
    # Pair: Aces
    _do_test("Pair test 3",has_pair(["AH","2D","3H","4D","5H","6S","4C"]))
    # Pair: 4
    _do_test("Pair test 4",not has_pair(["AH","2D","3H","4D","5H","6S","7C"]))
    _do_test("Texas hold'em test", holdem(["4C","KS","4H","8S","7S"],[["AC","4D"],["AS","9S"]]) == (19, "Flush"))




# beginning of work


def has_flush(lst):
  """Returns True if the list of cards lst contains a flush.
        A flush is 5 cards of the same suit.
  """
  for suit in "DHSC":
    count_suit_cards = 0
    for card in lst:
      if get_card_suit(card) == suit:
        count_suit_cards += 1 
    if count_suit_cards >= 5:
      return True
  return False


def has_straight(lst):
  """Returns True if the list of cards lst contains a straight.
      A straight is 5 cards of consecutive values, e.g. 9-10-J-Q-K.
      Note that Aces are both low and high, so A-2-3-4-5 and 10-J-Q-K-A are both straights!
  """
  counts = count_values(lst)
  counts[1] = counts[14]
    
  for position in range(len(counts)-4):
    found_straight = True
    for other_position in range(position, position+5):
      if counts[other_position] < 1:
        found_straight = False
    if found_straight:
      return True
  return False
  

def has_straight_flush(lst):
    """Returns true if the list of cards lst contains a straight flush.
        A straight flush is 5 consecutive cards of the same suit.
    """
    for suit in "DHSC":
      suit_cards = []
      for card in lst:
        if get_card_suit(card) == suit:
          suit_cards.append(card)
      if has_straight(suit_cards):
        return True 
      return False
        

def has_four_of_a_kind(lst):
    """Returns true if the list of cards lst contains a four of a kind.
        A four of a kind is 4 cards with the same value.
    """
    return max(count_values(lst)) >= 4


def has_three_of_a_kind(lst):
    """Returns true if the list of cards lst contains a three of a kind.
        A three of a kind is 3 cards with the same value.
    """
    return max(count_values(lst)) >= 3
    

def has_full_house(lst):
    """Returns true if the list of cards lst contains a full house.
        A full house is a three of a kind and a pair.
        Note that the pair cannot be the same value as the three of a kind.
    """
    return has_two_pairs(lst) and has_three_of_a_kind(lst)
    

def has_pair(lst):
    """Returns true if the list of cards lst contains a pair.
        A pair is 2 cards of the same value.
    foundPair = False
    for count in count_values(lst):
      if count >= 2:
        foundPair = True
    return foundPair
    """
    return max(count_values(lst)) >= 2


def has_two_pairs(lst):
    """Returns true if the list of cards lst contains two pairs.
        A pair is 2 cards of the same value.
    """
    twoPairNumber = 0
    for count in count_values(lst):
      if count >= 2:
        twoPairNumber += 1 
    return twoPairNumber >= 2
    

# end of work of week 4


listOfCards = ["2S","3S","4S","5S","6S","7S","8S","9S","10S","JS","QS","KS","AS","2H","3H","4H","5H","6H","7H","8H","9H","10H","JH","QH","KH","AH","2C","3C","4C","5C","6C","7C","8C","9C","10C","JC","QC","KC","AC","2D","3D","4D","5D","6D","7D","8D","9D","10D","JD","QD","KD","AD"]

player1cards = ["AS"]
del(listOfCards[12])
import random
random.shuffle(listOfCards)
player1cards.append(listOfCards[0])
