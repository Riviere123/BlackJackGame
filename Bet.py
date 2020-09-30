'''
this will ask the player how much to bet
'''


def bet():

	waiting = True

	while waiting:
		
		try:
			ammount = int(input('How much would you like to bet '))
			waiting = False
			
			return ammount

		except:
			print('That is an invalid entry. Please enter an Integer.')