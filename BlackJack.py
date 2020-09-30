'''
This is the main script to run the game
'''
import random
import Deck
import Bet
import Draw
import Reset

start = True
bank = 1000
cpuhand = []
cpuhandtotal = 0
playerhand = []
playerhandtotal = 0
bet = 0
compare = False


## Deck.shuffle() -- shuffle the deck
## bet = Bet.bet() -----start a bet and store it as var bet (does not check if it's over bank total)
## bank -= bet ---------reduce bank by bet ammount
## Draw.draw(2,playerhand,Deck.deck) ##---draws 2 cards off top of deck and removes them from the deck
##playerhandtotal = (Deck.total(playerhand)) ## --- returns the total value of hand and assigns it to playerhandtotal
##	Deck.deck = (Reset.reset(playerhand,Deck.deck)) --puts cards from players hand back into deck
##	Deck.deck = (Reset.reset(cpuhand,Deck.deck)) -- puts cards from cpu hand back into deck
print('welcome to BlackJack!')

while start:
	print(f'You currently have ${bank}')
	Deck.shuffle()
	dealerbust = False
	betini = True
	if bank <= 0:
		print('You have no more money')
		exit()
	##start initial bet
	while betini:
		bet = Bet.bet()
		if bet <= bank:
			bank -= bet

			print(f'Your bet is {bet}')
			print(f'You have {bank} remaining')
			betini = False
		else:
			print('Sorry you do not have enough.')


	##draw initial cards

	Draw.draw(2,playerhand,Deck.deck)
	playerhandtotal = (Deck.total(playerhand))
	Draw.draw(2,cpuhand,Deck.deck)
	cpuhandtotal = (Deck.total(cpuhand))
	
	##for i in range(0,len(playerhand)): ## to show more detail name of card
   		##print(Deck.decklib[playerhand[i]][1])

	print(f'Your hand {playerhand} your total is {playerhandtotal}')
	##for i in range(0,(len(cpuhand)-1)) ##to show more detail name of card
		##print(f'Dealer has a {Deck.decklib[cpuhand[i]][1]}')

	
	##initiate hit or stay sequance
	answer = True
	while answer == True:
		answer = input('Would you like to Hit or Stay? ').lower()
		if answer == 'hit':                    ##player hits
			Draw.draw(1,playerhand,Deck.deck)
			playerhandtotal = Deck.total(playerhand)
			print(f'your hand: {playerhand}')
			print(f'your total: {playerhandtotal}')
			answer = True

			if playerhandtotal > 21:
					print(f'You busted with: {playerhandtotal} and lost {bet}')
					Deck.deck = (Reset.reset(playerhand,Deck.deck))
					Deck.deck = (Reset.reset(cpuhand,Deck.deck))

					answer = False


		elif answer == 'stay': ##player stays and ends the while loop
			answer = False
			compare = True

		elif answer != 'stay' or answer != 'hit': ##continues while loop if not answered correctly
			print('Invalid response.')
			answer = True  


##AI FUNCTION
	while compare == True:
		if cpuhandtotal == playerhandtotal:
			print(f'Push: you get {bet} back')
			
			bank += bet

			Deck.deck = (Reset.reset(playerhand,Deck.deck))
			Deck.deck = (Reset.reset(cpuhand,Deck.deck))

			compare = False

		elif cpuhandtotal > 21:	##check if dealer is bust
				print(f'Dealer Busts! you won ${bet*2}')
				bank += (bet*2)

				Deck.deck = (Reset.reset(playerhand,Deck.deck))
				Deck.deck = (Reset.reset(cpuhand,Deck.deck))

				compare = False

		elif playerhandtotal > cpuhandtotal: ##if dealer is less than player dealer hits
			print(f'Dealer Hand:{cpuhand}')
			print('Dealer Hits.')
			Draw.draw(1,cpuhand,Deck.deck)
			cpuhandtotal = Deck.total(cpuhand)
			print(cpuhandtotal)
			print(cpuhand)
			
			compare = True

		


		elif playerhandtotal < cpuhandtotal: ##if dealer wins
				print(f'Dealer wins with {cpuhand} and a total of: {cpuhandtotal}')

				Deck.deck = (Reset.reset(playerhand,Deck.deck))
				Deck.deck = (Reset.reset(cpuhand,Deck.deck))

				compare = False







