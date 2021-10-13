import random as rnd
def play_dice(user_money):
	bet = int(input("Сколько ставишь?:")) #FIXME: не всё интуется, например Вася

	#Luck - влияет на первый аргумент randint'а
	#тест ставки
	if bet > user_money:
		print("У тeбя сток нет")
		play_dice(user_money)
	elif bet <= 0:
		print("Ставки от 1!")
	else:
		user_dice = rnd.randint(2, 12)
		casino_dice = rnd.randint(2, 12)

		#проверка выпавших чисел
		print("У тебя выпало", user_dice)
		print("У крупье выпало", casino_dice)
		if user_dice > casino_dice:
			print("Ты выйграл", bet)
			user_money += bet
		elif user_dice == casino_dice:
			print("Ничья")
		else:
			print("Ты проиграл", bet)
			user_money -= bet
		return user_money


