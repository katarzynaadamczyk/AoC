'''
Advent of Code 
2023 day 7
my solution to task  2

solution 2 - as solution 1, just adds the count of 'J' to max count of other cards
'''
from collections import Counter

cards_priorities = {x: i for i, x in enumerate('AKQJT98765432J')}
rank = 'RANK'
bid = 'BID'
kind = 'KIND'
kinds = ['FIVE', 'FOUR', 'FULL', 'THREE', 'TWO', 'ONE', 'HIGH']
tests = {'FIVE': lambda x: len(x) == 1 and 5 in x,
         'FOUR': lambda x: len(x) == 2 and 4 in x,
         'FULL': lambda x: len(x) == 2 and 3 in x and 2 in x,
         'THREE': lambda x: 3 in x,
         'TWO': lambda x: len(x) == 3,
         'ONE': lambda x: len(x) == 4 and 2 in x, 
         'HIGH': lambda x: len(x) == 5}

def get_kind(hand):
    values_of_hand = Counter(hand)
    if 'J' in values_of_hand.keys():
        act_card, act_max = 'A', 0
        for card, value in values_of_hand.items():
            if value > act_max and card != 'J':
                act_card = card
                act_max = value
        values_of_hand[act_card] = values_of_hand.get(act_card, 0) + values_of_hand['J']
        del values_of_hand['J']
    for kind, test in tests.items():
        if test(values_of_hand.values()):
            return kind

    return None

def get_data(filename):
    data = {}
    with open(filename, 'r') as myfile:
        for line in myfile:
            line = line.strip().split()
            data.setdefault(line[0], {bid: int(line[-1]), kind: get_kind(line[0]), rank: 0})
    return data

def sort_hands(hands):
    return sorted(list(hands.keys()), key=lambda hand: (kinds.index(hands[hand][kind]), cards_priorities[hand[0]],\
                                                  cards_priorities[hand[1]], cards_priorities[hand[2]],\
                                                  cards_priorities[hand[3]], cards_priorities[hand[4]]))

def insert_ranks(sorted_hands, hands_data):
    max_rank = len(sorted_hands)
    for i, hand in enumerate(sorted_hands):
        hands_data[hand][rank] = max_rank - i

def solution_2(filename):
    data = get_data(filename)
    insert_ranks(sort_hands(data), data)
    return sum([x[bid] * x[rank] for x in data.values()])

def main():
    print('test 1:', solution_2('2023/Day_7/test_2.txt'))
    print('Solution 1:', solution_2('2023/Day_7/task.txt'))
    
if __name__ == '__main__':
    main()
