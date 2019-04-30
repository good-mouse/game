import bot
import human
import goroda
import verification
import os
os.system('cls')
bot_name = ("Нага")
print("Привет!, меня зовут " + bot_name + "\nА как зовут тебя?")
name = input();
print("Приятно познакомиться " + name )
def menu():
	while True:
		print("Давай поиграем в одну из этих игр")
		print("1.Угадай число\n2.Города")
		print("Введи номер игры")
		games = input()
		a = verification.games_number(games)
		if a == True: 
			if games == '1' : numbers()
			elif games == '2': 
				os.system('cls')
				goroda.game()
		else :
			print("Я тебя не понимаю")
			continue
	
def numbers():
	print("Давай поиграем в игру Угадай число")
	print("Кто будет угадывать, Ты или Я?")
	a = ''
	otvet = False
	while otvet == False:
		a = input()
		a = a.lower()
		otvet = verification.answer(a)
		if otvet == False : print("Я тебя не понимаю, введи Ты или Я")
	if a == 'я':
		os.system('cls')
		bot.game()
	elif a == 'ты':
		os.system('cls')
		human.game()
menu()

os.system('cls')