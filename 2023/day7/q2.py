from collections import Counter

with open('puzzle', 'r') as f:
    puzzle = f.readlines()

hands = [(line.split(' ')[0], int(line.split(' ')[1].strip())) for line in puzzle]


def first_sort(hands):
    groups = {}
    for i in range(1,8):
        groups[i] = []
    
    for hand in hands:
        hand_counter = Counter(hand[0])
        values = sorted(hand_counter.values())

        # special J
        if "J" in hand_counter and hand_counter['J'] != 5:

            j_count = hand_counter['J']
            hand_counter.pop('J')
            values = sorted(hand_counter.values())
            values[-1] = values[-1] + j_count


        if values == [5]:    groups[1].append(hand)
        elif values == [1,4]:groups[2].append(hand)
        elif values == [2,3]:groups[3].append(hand)
        elif values == [1,1,3]:groups[4].append(hand)
        elif values == [1,2,2]:groups[5].append(hand)  
        elif values == [1,1,1,2]:groups[6].append(hand)
        elif values == [1,1,1,1,1]:groups[7].append(hand) 
        else: raise Exception("group error")
    
    return groups

def second_sort(grouped_hands) -> int:
    ranks = 'AKQT98765432J'
    rank_dict = {rank: index for index, rank in enumerate(ranks)}
    return [rank_dict[char] for char in grouped_hands]

first_groups = first_sort(hands=hands)

final_hands = []
for rank, value in first_groups.items():
    sorted_value = sorted(value, key=lambda x:second_sort(x[0]))
    final_hands.extend(sorted_value)

print(len(final_hands))
ans = 0
for idx, item in enumerate(final_hands[::-1]):
    ans += (item[1]*(idx+1))
print(ans)
