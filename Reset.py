def reset(hand,deck):
	num = len(hand)
	for cards in range(0,num):
		deck.append(hand.pop())
	return deck