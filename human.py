import verification
from random import randint
import os
#Algorithm
def algorithm(min,max):
	while True:
		current = (min + max) // 2
		if min == max : 
			current = min
			print('Я его угадал! Это число %i' % current)
			break
		print('Ваше число: %i ? (да, больше, меньше)' % current)
		decision = input()
		decision = decision.lower()
		bukva = verification.is_right(decision)
		
		if bukva == False : print("Я тебя не понимаю, введи Да, Больше или Меньше")
		
		if decision == 'да':
			os.system('cls')
			print('Я его угадал! Это число %i' % current)
			break
		elif decision=='больше':
			if min == max - 1 : #Вычисление элементарного ответа
				current = max
				print('Я его угадал! Это число %i' % current)
				break
			else : min = current + 1
		elif decision=='меньше':
			if min == max - 1 :  #Вычисление элементарного ответа
				current = min
				print('Я его угадал! Это число %i' % current)
				break
			else :max = current - 1
		
					
def game():
	print("Ну чтож давай поиграем в игру \nПравила простые, ты загадываешь число, я попробую его угадать.\nТы будешь подсказывать мне когда будешь говорить больше твое число, или меньше.\nУ меня будет ограниченное число попыток")
	print("Кто загадает интервал?\nТы или я?")
	a = ''
	otvet = False
	while otvet == False:
		a = input()
		a = a.lower()
		otvet = verification.answer(a)
		if otvet == False : print("Я тебя не понимаю, введи Ты или Я")
	if a == 'я':
		i()
		os.system('cls')
	elif a == 'ты':
		you()
		os.system('cls')

def i():
	#Кол-во попыток
	attemptsNumber = 0
	number = 0
	current = 0
	print("Хорошо.\nВведи интервал, в котором ты загадаешь число")
	
	interval = False
	while interval == False:
		chislo1 = False
		
		print("Минимум: ") 
		while chislo1 == False:
			min = input()
			chislo1 = verification.is_number(min)
			if chislo1 == False: print("Это не целое число \nВведи минимум еще раз")
			
		chislo1 = False
			
		print("Максимум: ") 
		while chislo1 == False:
			max = input()
			chislo1 = verification.is_number(max)
			if chislo1 == False: print("Это не целое число \nВведи максимум еще раз")
		min = int(min)
		max = int(max)
		interval = verification.is_interval(min,max)
		if interval == False: print("Интервал не подходит, выбери другой")
		else : 
			os.system('cls')
			attemptsNumbers = verification.attempts(min, max)
			stroka = verification.literacy(attemptsNumbers)
			print("Итак, загадывай число от %i до %i \nУ меня есть %i %s" % (min,max,attemptsNumbers,stroka))
	print("Если загадал, нажми ENTER и я начну угадывать")
	input()
	algorithm(min,max)
	print("Сыграем еще раз? \nда/нет")
	bukva = False
	while bukva == False:
		decision = input()
		decision = decision.lower()
		bukva = verification.decis(decision)
		if bukva == False : print("Я тебя не понимаю, введи Да или Нет")
		if decision == 'да':
			os.system('cls')
			game()
		elif decision == 'нет':
			return
def you():
	#Кол-во попыток
	attemptsNumber = 0
	number = 0
	current = 0
	max = randint(0, 1000)
	min = randint(0, max)
	attemptsNumbers = verification.attempts(min, max)
	os.system('cls')
	stroka = verification.literacy(attemptsNumbers)
	print("Итак, загадывай число от %i до %i \nУ меня есть %i %s" % (min,max,attemptsNumbers,stroka))
	print("Если загадал, нажми ENTER и я начну угадывать")
	input()
	algorithm(min,max)
	print("Сыграем еще раз? \nда/нет")
	bukva = False
	while bukva == False:
		decision = input()
		decision = decision.lower()
		bukva = verification.decis(decision)
		if bukva == False : print("Я тебя не понимаю, введи Да или Нет")
		if decision == 'да':
			os.system('cls')
			game()
		elif decision == 'нет':
			return
		
	
	