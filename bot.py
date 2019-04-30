from random import randint
import verification
import os

def game():	
	chislo = False
	interval = False
	#Кол-во попыток
	attemptsNumber = 0
	number = 0

	print("Ну чтож давай поиграем в игру \nПравила простые, я загадаю число, попробуй его угадать.\nУ тебя будет ограниченное число попыток")
	print("Введи интервал, в котором я загадаю число")

	while interval == False:
		chislo = False
		
		print("Минимум: ") 
		while chislo == False:
			min = input()
			chislo = verification.is_number(min)
			if chislo == False: print("Это не целое число \nВведи минимум еще раз")
			
		chislo = False
			
		print("Максимум: ") 
		while chislo == False:
			max = input()
			chislo = verification.is_number(max)
			if chislo == False: print("Это не целое число \nВведи максимум еще раз")
		min = int(min)
		max = int(max)
		interval = verification.is_interval(min,max)
		if interval == False: print("Интервал не подходит, выбери другой")
		else : 
			number = randint(min, max)
			os.system('cls')
		
		

	attemptsNumbers = verification.attempts(min, max)
	stroka = verification.literacy(attemptsNumbers)
	print("Итак, я загадал число от %i до %i \nУ тебя есть %i %s" % (min,max,attemptsNumbers,stroka))
	while attemptsNumber < attemptsNumbers:     
		print("Твое число: ")
		quess = input()
		check = verification.is_number(quess)
		if check == False: print("Это не целое число, попробуй еще раз")
		else:
			quess = int(quess)
			attemptsNumber += 1       

			if quess < number:
				print("Нет, мое число больше.")
			elif quess > number:                
				print("Нет, мое число меньше.")
			elif quess == number:
				print("Отлично, ты угадал число с %i попытки!" % attemptsNumber)   
				break

	if quess != number : print("Твои попытки закончились. Мое число : %i" % number)

