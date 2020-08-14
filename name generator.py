import names, random, sys, yaml#, random-word

def main():
	db, nameList = load_yaml()
	print("Number of names in characters.yaml: " + str(len(nameList)))
	print()
	ages = ['Young', 'Teen', 'Adult', 'Old']
	personality = ["open", "driven", 'extravert ', 
					'agreeable', 'anxiety', 'fear',
					'anger', 'frustration', 'envy', 'jealousy', 
					'guilt', 'depressed', 'lonely']
	trustLevel = ["parinoid", "trusting", 'neutral', 'flip-floppy']

	#notes =  open('Char Notes.txt', 'a+')



	while True:
		
		numOfNames = 0
		people = {}
		print('Name options:')
		while numOfNames < 4:
			thisName =  names.get_full_name()
			#we need to check for dup name
			people[str(numOfNames+1)] = thisName #get 4 names to pick
			print(numOfNames+1, ". ", thisName)
			numOfNames += 1

		age = random.choice(ages)
		trust = random.choice(trustLevel)
		des1, des2 = random.choice(personality), random.choice(personality)

		print()
		print("Age: " + age)
		print("Trust level: " + trust)
		print("Personality traits: " + des1 + ", " + des2 )
		print()

		addNotes = input("Would you like to add notes? Enter 1-4 to save name.\n\n\t\tOR\n\nEnter for new names/traits, e to exit: \n")
		if addNotes.lower() in ['1','2','3','4']:
			chosenName = people[addNotes]
			notesToAdd = input("Enter extra notes below. Press return to save:\n")

			#save_yaml(db)
		if addNotes.lower() == 'e':
			sys.exit()

		print()

def load_yaml():
	with  open(r'characters.yaml') as charFile:
		db = yaml.safe_load(charFile)
		nameList = []
		for key in db:
			nameList.append(key)
		charFile.close() #check this?
	return db, nameList

def dup_name(nameList, name):
	pass

def update_yaml(db):
	#open file
	#add name, age, trust level, personality, notes
	#get new name nameList
	#close file
	#return nameList
	pass 

main()