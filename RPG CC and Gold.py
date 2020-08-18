import random

#########################################################################################



class Default():

	def __init__(self,name='no_name',gender = 'Neuter',weapon='no_weapon',skill='no_skill',hitpoints=5,player_gold = 10):
		self.name = name
		self.gender = gender
		self.weapon = weapon
		self.skill = skill
		self.hitpoints = hitpoints
		self.player_gold = player_gold

	def __str__(self):

		print(f'{self.name}{self.gender}{self.weapon}{self.skill}{self.hitpoints}')

	def test(self):
		print('My Yoshi')

	def treasue_chest(self):
		treasue = True
		print('You found a treasure chest!')
		while treasue == True:
			choice = input(f'Do you open[O] the chest or ignore[I] it? ')
			if choice.upper() == 'O':
				loot = random.randint(1,6)
				print(f'Yay you found {loot} gold coins!')
				self.player_gold = self.player_gold + loot
				return(f'{self.player_gold}')
				treasue = False
			elif choice.upper() == 'I':
				print('Still Yay')
				treasue = False
			else:
				print('Try Again')
				continue 


class Enemy():

	def __init__(self,name='no_name',melee='none',ranged ='none',magic='none',item='none', stealth='none', enemy_hitpoints = 10):
		self.name = name
		self.melee = melee
		self.ranged = ranged
		self.magic = magic
		self.item = item
		self.stealth = stealth
		self.enemy_hitpoints = enemy_hitpoints
		

	def __str__(self):
		return(f'{self.name},{self.melee},{self.ranged},{self.magic},{self.item},{self.stealth},{self.enemy_hitpoints}')

#########################################################################################

class Knight(Default):



	def __init__(self,name='no_name',gender = 'Neuter',weapon='Blade',skill='Deflect',hitpoints=12):
		Default.__init__(self)		
		self.name = name
		self.gender = gender
		self.weapon = weapon
		self.skill = skill
		self.hitpoints = hitpoints


	def __str__(self):

		return(f'{self.name}\n{self.gender}\n{self.weapon}\n{self.skill}\n{self.hitpoints}\n')

	def goblin_attack(self):
		goblins = True
		print('A goblin blocks your path\n')
		while goblins == True:
			choice = input(f'{self.weapon}[W] or {self.skill}[S]? ')
			if choice == 'W' or choice == 'w':
				dmg = random.randint(1,4)
				print(f'You escaped, but you took {dmg} damage.')
				self.hitpoints = self.hitpoints - dmg
				print(f'You now have {self.hitpoints}hp')
				goblins = False
				break
			elif choice == 'S' or choice == 's':
				print('You Lived')
				goblins = False
				break
			else:
				print('Try Again')
				continue


#########################################################################################

class Wizard(Default):

	def __init__(self,name='no_name',gender='Neuter',weapon='Wand',skill='Teleport',hitpoints=8):
		Default.__init__(self)
		self.name = name
		self.gender = gender
		self.weapon = weapon
		self.skill = skill
		self.hitpoints = hitpoints

	def __str__(self):

		return(f'{self.name}\n{self.gender}\n{self.weapon}\n{self.skill}\n{self.hitpoints}\n')
	
	def goblin_attack(self):
		goblins = True
		print('A goblin blocks your path\n')
		while goblins == True:
			choice = input(f'{self.weapon}[W] or {self.skill}[S]? ')
			if choice == 'W' or choice == 'w':
				print('You Died')
				goblins = False
				break
			elif choice == 'S' or choice == 's':
				print('You Lived')
				goblins == False
				break
			else:
				print('Try Again')
				continue

#########################################################################################

class Rogue(Default):

	def __init__(self,name='no_name',gender='Neuter',weapon='Dagger',skill='Evade',hitpoints=10):
		Default.__init__(self)
		self.name = name
		self.gender = gender
		self.weapon = weapon
		self.skill = skill
		self.hitpoints = hitpoints

	def __str__(self):

		return(f'{self.name}\n{self.gender}\n{self.weapon}\n{self.skill}\n{self.hitpoints}\n')

	def goblin_attack(self):
		goblins = True
		print('A goblin blocks your path\n')
		while goblins == True:
			choice = input(f'{self.weapon}[W] or {self.skill}[S]? ')
			if choice == 'W' or choice == 'w':
				print('You Died')
				goblins = False
				break
			elif choice == 'S' or choice == 's':
				print('You Lived')
				goblins = False
				break
			else:
				print('Try Again')
				continue
#########################################################################################









#########################################################################################



game_on = True
ready_check = False
game_over = False
class_check = False
gender_check = False
char = Default()



while game_on == True:


#########################################################################################

	while ready_check == False:
		choice = input('Are you ready?: ')
		if choice == 'Y' or choice == 'y':
			print('Let us begin\n')



			ready_check = True
		elif choice == 'N' or choice == 'n':
			print("press 'Y' to begin")
			continue
		else:
			print('Try Again')
			continue


#########################################################################################

	name = input('What is your name: ')

#########################################################################################

	while gender_check == False:
	 	choice = input('Are you a man or a woman? ')
	 	if choice == 'M' or choice == 'm':
	 		gender = 'Man'
	 		name = 'Sir ' + name
	 		gender_check = True
	 	elif choice == 'W' or choice == 'w' or choice == 'F' or choice == 'f':
	 		gender = 'Woman'
	 		name = 'Lady ' + name
	 		gender_check = True
	 	else:
	 		print('Try Again')
	 		continue





	while class_check == False:
		choice = input('Choose your class Knight[K], Wizard[W], or Rogue[R]: ')
		if choice == 'K' or choice == 'k':
			print(f'Hello {name}\n')
			char = Knight(name,gender)
			class_check = True
		
		elif choice == 'W' or choice == 'w':
			print(f'Hi {name}\n')
			char = Wizard(name,gender)
			class_check = True

		elif choice == 'R' or choice == 'r':
			print(f'Hi {name}\n')
			char = Rogue(name,gender)
			class_check = True

		else:
			print('Try Again')
			continue








#########################################################################################
	
	print(char)
	print
	char.goblin_attack()
	char.treasue_chest()
	char.test()
	goblin = Enemy()
	print(goblin)



	






















































#########################################################################################




	game_over = True

	while game_over == True:
		choice = input('Play again?: ')
		if choice == 'Y' or choice == 'y':
			game_on = True
			ready_check = False
			game_over = False
			class_check = False
			gender_check = False
			char = Default()
			break
		elif choice == 'N' or choice == 'n':
			game_on = False
			game_over = False
		else:
			print('Try Again')
			continue










