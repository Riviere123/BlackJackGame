import random

decklib = {'2c':[2,'Two of Clubs'], '3c':[3,'Three of Clubs'], '4c':[4,'Four of Clubs'], '5c':[5,'Five of Clubs'], '6c':[6,'Six of Clubs'], '7c':[7,'Seven of Clubs'], '8c':[8,'Eight of Clubs'], '9c':[9,'Nine of Clubs'], '10c':[10,'Ten of Clubs'], 'jc':[10,'Jack of Clubs'],'qc':[10,'Queen of Clubs'],'kc':[10,'King of Clubs'], 'ac':[11,'Ace of Clubs'], 
 '2d':[2,'Two of Diamonds'], '3d':[3,'Three of Diamonds'], '4d':[4,'Four of Diamonds'], '5d':[5,'Five of Diamonds'], '6d':[6,'Six of Diamonds'], '7d':[7,'Seven of Diamonds'], '8d':[8,'Eight of Diamonds'], '9d':[9,'Nine of Diamonds'], '10d':[10,'Ten of Diamonds'], 'jd':[10,'Jack of Diamonds'],'qd':[10,'Queen of Diamonds'],'kd':[10,'King of Diamonds'], 'ad':[11,'Ace of Diamonds'],
 '2s':[2,'Two of Spades'], '3s':[3,'Three of Spades'], '4s':[4,'Four of Spades'], '5s':[5,'Five of Spades'], '6s':[6,'Six of Spades'], '7s':[7,'Seven of Spades'], '8s':[8,'Eight of Spades'], '9s':[9,'Nine of Spades'], '10s':[10,'Ten of Spades'], 'js':[10,'Jack of Spades'], 'qs':[10,'Queen of Spades'], 'ks':[10,'King of Spades'],'as':[11,'Ace of Spades'], 
 '2h':[2,'Two of Hearts'], '3h':[3,'Hearts'], '4h':[4,'Four of Hearts'], '5h':[5,'Five of Hearts'], '6h':[6,'Six of Hearts'], '7h':[7,'Seven of Hearts'], '8h':[8,'Eight of Hearts'], '9h':[9,'Nine of Hearts'], '10h':[10,'Ten of Hearts'], 'jh':[10,'Jack of Hearts'], 'qh':[10,'Queen of Hearts'], 'kh':[10,'King of Hearts'],'ah':[11,'Ace of Hearts']}

deck = ['2c','3c','4c','5c','6c','7c','8c','9c','10c','jc','qc','kc','ac',
		'2d','3d','4d','5d','6d','7d','8d','9d','10d','jd','qd','kd','ad',
		'2s','3s','4s','5s','6s','7s','8s','9s','10s','js','qs','ks','as',
		'2h','3h','4h','5h','6h','7h','8h','9h','10h','jh','qh','kh','ah']


def shuffle():
	random.shuffle(deck)

def total(hand): ## totals the hand provided
	total = 0
	aces = hand.count('ah') + hand.count('ad') + hand.count('as') + hand.count('ac')
	for cards in hand:
		value = decklib[cards][0]
		total +=  value

	while total > 21 and aces > 0:
		total -= 10
		aces -= 1

	return total


