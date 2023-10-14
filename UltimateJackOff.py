bet = 500
payouts = {
    'royal_flush' : 125000,
    'straight_flush' : 25000,
    'four_of_a_kind' : 12500,
    'full_house' : 4000,
    'flush' : 3000,
    'straight' : 2000,
    'three_of_a_kind' : 1500,
    'two_pair' : 800,
    'jacks_or_better' : 500
}
deck = ['ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'th', 'jh', 'qh', 'kh', 
        'ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'td', 'jd', 'qd', 'kd',
        'ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'tc', 'jc', 'qc', 'kc',
        'as', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'ts', 'js', 'qs', 'ks']
hold_ev = {
    'hhhhh' : 0,
    'hhhhd' : 0,
    'hhhdh' : 0,
    'hhhdd' : 0,
    'hhdhh' : 0,
    'hhdhd' : 0,
    'hhddh' : 0,
    'hhddd' : 0,
    'hdhhh' : 0,
    'hdhhd' : 0,
    'hdhdh' : 0,
    'hdhdd' : 0,
    'hddhh' : 0,
    'hddhd' : 0,
    'hdddh' : 0,
    'hdddd' : 0,
    'dhhhh' : 0,
    'dhhhd' : 0,
    'dhhdh' : 0,
    'dhhdd' : 0,
    'dhdhh' : 0,
    'dhdhd' : 0,
    'dhddh' : 0,
    'dhddd' : 0,
    'ddhhh' : 0,
    'ddhhd' : 0,
    'ddhdh' : 0,
    'ddhdd' : 0,
    'dddhh' : 0,
    'dddhd' : 0,
    'ddddh' : 0,
    'ddddd' : 0
}
def get_hand_value(hand):
    card_values = {
        'ace' : 0,
        'one' : 0,
        'two' : 0,
        'three' : 0,
        'four' : 0,
        'five' : 0,
        'six' : 0,
        'seven' : 0,
        'eight' : 0,
        'nine' : 0,
        'ten' : 0,
        'jack' : 0,
        'queen' : 0,
        'king' : 0,
    }
    values_found = []
    found_jacks_or_better = False
    found_two_pair = False
    found_three_of_a_kind = False
    found_straight = False
    found_flush = True
    found_full_house = False
    found_four_of_a_kind = False
    flush_suite = hand[0][1]
    for card in hand:
        values_found.append(card[0])
        if card[1] != flush_suite:
            found_flush = False
        if card[0] == 'a':
            card_values['ace'] += 1
        elif card[0] == '1':
            card_values['one'] += 1
        elif card[0] == '2':
            card_values['two'] += 1
        elif card[0] == '3':
            card_values['three'] += 1
        elif card[0] == '4':
            card_values['four'] += 1
        elif card[0] == '5':
            card_values['five'] += 1
        elif card[0] == '6':
            card_values['six'] += 1
        elif card[0] == '7':
            card_values['seven'] += 1
        elif card[0] == '8':
            card_values['eight'] += 1
        elif card[0] == '9':
            card_values['nine'] += 1
        elif card[0] == 't':
            card_values['ten'] += 1
        elif card[0] == 'j':
            card_values['jack'] += 1
        elif card[0] == 'q':
            card_values['queen'] += 1
        elif card[0] == 'k':
            card_values['king'] += 1
    found_pair = False
    for type, count in card_values.items():
        if count == 2:
            if type == 'ace' or type == 'jack' or type == 'queen' or type == 'king':
                found_jacks_or_better = True
            if found_pair:
                found_two_pair = True
            else:
                found_pair = True
        if count == 3:
            found_three_of_a_kind = True
        if count == 4:
            found_four_of_a_kind = True
    if found_pair and found_three_of_a_kind:
        found_full_house = True
    if found_four_of_a_kind:
        return payouts['four_of_a_kind']
    if found_full_house:
        return payouts['full_house']
    if found_three_of_a_kind:
        return payouts['three_of_a_kind']
    if found_two_pair:
        return payouts['two_pair']
    if found_jacks_or_better:
        return payouts['jacks_or_better']
    if found_pair:
        return 0
    values_found_numbered_ace_high = []
    values_found_numbered_ace_low = []
    for value in values_found:
        if value == 'a':
            values_found_numbered_ace_high.append(14)
            values_found_numbered_ace_low.append(1)
        elif value == 'j':
            values_found_numbered_ace_high.append(11)
            values_found_numbered_ace_low.append(11)
        elif value == 'q':
            values_found_numbered_ace_high.append(12)
            values_found_numbered_ace_low.append(12)
        elif value == 'k':
            values_found_numbered_ace_high.append(13)
            values_found_numbered_ace_low.append(13)
        elif value == 't':
            values_found_numbered_ace_high.append(10)
            values_found_numbered_ace_low.append(10)
        else:
             values_found_numbered_ace_high.append(int(value))
             values_found_numbered_ace_low.append(int(value))
    values_found_numbered_ace_high.sort()
    previous_value = values_found_numbered_ace_high[0]
    found_straight = True
    for index, value in enumerate(values_found_numbered_ace_high):
        if index == 0:
            continue
        if value == previous_value + 1:
            previous_value = value
        else:
            found_straight = False
            break
    if found_straight:
        if values_found_numbered_ace_high[0] == 10 and found_flush:
            return payouts['royal_flush']
        elif found_flush:
            return payouts['straight_flush']
        else:
            return payouts['straight']
    values_found_numbered_ace_low.sort()
    previous_value = values_found_numbered_ace_low[0]
    found_straight = True
    for index, value in enumerate(values_found_numbered_ace_low):
        if index == 0:
            continue
        if value == previous_value + 1:
            previous_value = value
        else:
            found_straight = False
            break
    if found_straight:
        if found_flush:
            return payouts['straight_flush']
        else:
            return payouts['straight']
    if found_flush:
        return payouts['flush']
    return 0
def get_hand_evs(hand, hold_pattern):
    deck_remaining = set(deck) - set(hand)
    new_hand = []
    for index, value in enumerate(hold_pattern):
        if value == 'h':
            new_hand.append(hand[index])
    hand = new_hand
    if len(hand) == 5:
        return get_hand_value(hand)
    if len(hand) == 4:
        total_winnings = 0
        total_hands = 47
        for card in deck_remaining:
            hand.append(card)
            total_winnings += get_hand_value(hand)
            hand.pop(4)
        return total_winnings / total_hands
    if len(hand) == 3:
        total_winnings = 0
        total_hands = 1081
        for index1, card1 in enumerate(deck_remaining):
            hand.append(card1)
            for index2, card2 in enumerate(deck_remaining):
                if index2 > index1:
                    hand.append(card2)
                    total_winnings += get_hand_value(hand)
                    hand.pop(4)
            hand.pop(3)
        return total_winnings / total_hands
    if len(hand) == 2:
        total_winnings = 0
        total_hands = 16215
        for index1, card1 in enumerate(deck_remaining):
            hand.append(card1)
            for index2, card2 in enumerate(deck_remaining):
                if index2 > index1:
                    hand.append(card2)
                    for index3, card3 in enumerate(deck_remaining):
                        if index3 > index2:
                            hand.append(card3)
                            total_winnings += get_hand_value(hand)
                            hand.pop(4)
                    hand.pop(3)
            hand.pop(2)
        return total_winnings / total_hands
    if len(hand) == 1:
        total_winnings = 0
        total_hands = 178365
        for index1, card1 in enumerate(deck_remaining):
            hand.append(card1)
            for index2, card2 in enumerate(deck_remaining):
                if index2 > index1:
                    hand.append(card2)
                    for index3, card3 in enumerate(deck_remaining):
                        if index3 > index2:
                            hand.append(card3)
                            for index4, card4 in enumerate(deck_remaining):
                                if index4 > index3:
                                    hand.append(card4)
                                    total_winnings += get_hand_value(hand)
                                    hand.pop(4)
                            hand.pop(3)
                    hand.pop(2)
            hand.pop(1)
        return total_winnings / total_hands
    if len(hand) == 0:
        total_winnings = 0
        total_hands = 1533939
        for index1, card1 in enumerate(deck_remaining):
            hand.append(card1)
            for index2, card2 in enumerate(deck_remaining):
                if index2 > index1:
                    hand.append(card2)
                    for index3, card3 in enumerate(deck_remaining):
                        if index3 > index2:
                            hand.append(card3)
                            for index4, card4 in enumerate(deck_remaining):
                                if index4 > index3:
                                    hand.append(card4)
                                    for index5, card5 in enumerate(deck_remaining):
                                        if index5 > index4:
                                            hand.append(card5)
                                            total_winnings += get_hand_value(hand)
                                            hand.pop(4)
                                    hand.pop(3)
                            hand.pop(2)
                    hand.pop(1)
            hand.pop(0)
        return total_winnings / total_hands
def get_best_pattern(hand):
    best_ev = 0
    best_pattern = ''
    for pattern in hold_ev.keys():
        new_ev = get_hand_evs(hand, pattern)
        if new_ev > best_ev:
            best_ev = new_ev
            best_pattern = pattern
    return best_pattern
print(get_best_pattern(['6c', 'ah', '8c', '2c', 'qd']))