from pathlib import Path
from collections import namedtuple
from functools import cmp_to_key

path = Path(__file__).parent / "aoc-day7-input.txt"
with open(path) as my_file:
    lines = my_file.readlines()

card_strength = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def hand_type(hand):
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1
    
    number_of_unique_cards = len(card_counts.keys())
    if number_of_unique_cards == 1:
        return 7
    elif number_of_unique_cards == 2:
        count1, count2 = sorted(card_counts.values())
        if count1 == 1 and count2 == 4:
            return 6
        else:
            return 5
    elif number_of_unique_cards == 3:
        count1, count2, count3 = sorted(card_counts.values())
        if count1 == 1 and count2 == 1 and count3 == 3:
            return 4
        else:
            return 3
    elif number_of_unique_cards == 4:
        return 2
    else:
        return 1

def compare_hands(hand1, hand2):
    hand1_type = hand_type(hand1.cards)
    hand2_type = hand_type(hand2.cards)

    if hand1_type == hand2_type:
        index = 0
        while index < 5:
            if hand1.cards[index] != hand2.cards[index]:
                return card_strength.index(hand1.cards[index]) - card_strength.index(hand2.cards[index])
            index += 1
        print("WTF: ", hand1.cards, hand2.cards)
        return 0 # should never reach here
    else:
        return hand1_type - hand2_type

Hand = namedtuple("Hand", "cards bid")

hands = []

for line in lines:
    hand, bid = line.strip().split(' ')
    hands.append(Hand(hand, int(bid)))

hands2 = sorted(hands, key=cmp_to_key(compare_hands))

total_winnings = 0
rank = 0
for hand in hands2:
    rank += 1
    total_winnings += hand.bid * rank

print(total_winnings)