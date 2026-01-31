# version 2.0
import keyboard as keyb
import random
import time
from colorama import Fore, Back, Style
from colorama import init
init()

print(Fore.YELLOW)
print("Loading...")
time.sleep(random.randint(1,3))
sha = int(input("What will be the difficulty?\n max = 4 \n min = 1 \n:"))
print("Enter - exit")
while True:

#_______________________________________________________________________________________________________________________________________

	if sha == 1:
		a = int(random.randint(0,20))
		s = int(random.randint(0,20))
		d = "+"
		b = '-'
		asa = random.choice([d,b])
		if asa == d:
			answer1S = a + s	
		elif asa == b:
			s = random.randint(0,a) 
			answer1S = a - s	
		print("\n" + str(a ) + str( asa ) + str( s) + '= ?')
		# ответ
		answer1 = int(input("answer: "))
		if answer1 == answer1S:
			print(Fore.GREEN)
			print("\nRight")
		elif answer1 != answer1S:
			print(Fore.RED)
			print("Wrong\ntry again")
		while answer1 != answer1S:
			answer1 = int(input("answer: "))
			if answer1 == answer1S:
				print(Fore.GREEN)
				print("\nRight")
				print(Fore.YELLOW)
			elif answer1 != answer1S:
				print(Fore.RED)
				print("Wrong\ntry again\n")
				print(Fore.YELLOW)
#_______________________________________________________________________________________________________________________________________

	if sha == 2:
		a = int(random.randint(0,100))
		s = int(random.randint(0,100))
		d = "+"
		b = '-'
		g = "*"
		asa = random.choice([d,b,g])
		if asa == d:
			answer1S = a + s
		elif asa == b:
			s = random.randint(0,a) 
			answer1S = a - s
		else :
			a = int(random.randint(0,25))
			s = int(random.randint(2,10))
			answer1S = a * s 	
			
		print("\n" + str(a ) + str( asa ) + str( s) + '= ?')
		# ответ
		answer1 = int(input("answer: "))
		if answer1 == answer1S:
			print(Fore.GREEN)
			print("\nRight")
		elif answer1 != answer1S:
			print(Fore.RED)
			print("Wrong\ntry again")
		while answer1 != answer1S:
			answer1 = int(input("answer: "))
			if answer1 == answer1S:
				print(Fore.GREEN)
				print("\nRight")
				print(Fore.YELLOW)
			elif answer1 != answer1S:
				print(Fore.RED)
				print("Wrong\ntry again\n")
				print(Fore.YELLOW)
		
#___________________________________________________________________________________________________

	elif sha == 3:
		a = int(random.randint(0,500))
		s = int(random.randint(0,500))
		d = "+"
		b = '-'
		g = "*"
		asa = random.choice([d,b,g])
		if asa == d:
			answer1S = a + s
		elif asa == b:
			s = random.randint(-100,250) 
			answer1S = a - s

		else :
			a = int(random.randint(0,50))
			s = int(random.randint(2,15))
			answer1S = a * s 	

		print("\n" + str(a ) + str( asa ) + str( s) + '= ?')
		answer1 = int(input("answer: "))
		if answer1 == answer1S:
			print(Fore.GREEN)
			print("\nRight")
		elif answer1 != answer1S:
			print(Fore.RED)
			print("Wrong\ntry again")
		while answer1 != answer1S:
			answer1 = int(input("answer: "))
			if answer1 == answer1S:
				print(Fore.GREEN)
				print("\nRight")
			elif answer1 != answer1S:
				print(Fore.RED)
				print("Wrong\ntry again")

#_________________________________________________________________________________________________________________________________________________________________________

	elif sha == 4: 
		a = int(random.randint(0,1000))
		s = int(random.randint(0,1000))
		d = "+"
		b = '-'
		g = "*"
		asa = random.choice([d,b,g])
		if asa == d:
			answer1S = a + s
		elif asa == b:
			s = random.randint(0,500) 
			answer1S = a - s
		else :
			a = int(random.randint(0,100))
			s = int(random.randint(2,15))
			answer1S = a * s

		print("\n" + str(a ) + str( asa ) + str( s) + '= ?')
		answer1 = int(input("answer: "))
		if answer1 == answer1S:
			print(Fore.GREEN)
			print("\nRight")
		elif answer1 != answer1S:
			print(Fore.RED)
			print("Wrong\ntry again")
		while answer1 != answer1S:
			answer1 = int(input("answer: "))
			if answer1 == answer1S:
				print(Fore.GREEN)
				print("\nRight")
			elif answer1 != answer1S:
				print(Fore.RED)
				print("Wrong\ntry again")



input()







































	
	




