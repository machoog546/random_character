import names, random

ages = ['Young', 'Teen', 'Adult', 'Old']
personality = ["open", "driven", 'extravert ', 
                'agreeable', 'anxiety', 'fear',
                 'anger', 'frustration', 'envy', 'jealousy', 
                 'guilt', 'depressed', 'lonely']
trustLevel = ["parinoid", "trusting", 'neutral', 'flip-floppy']

notes =  open('Char Notes.txt', 'a+')



while True:
    person = names.get_full_name()
    age = random.choice(ages)
    trust = random.choice(trustLevel)
    des1, des2 = random.choice(personality), random.choice(personality)

    print()
    print("Name: " + person)
    print("Age: " + age)
    print("Trust level: " + trust)
    print("Personality traits: " + des1 + ", " + des2 )
    print()

    addNotes = input("Would you like to add notes?\n\ny to add, or enter to skip, e to exit: \n")
    if addNotes.lower() == 'y':
        notes.write("Name: " + person + '\r')
        notes.write("\tAge: " + str(age) + '\r')
        notes.write("Trust level: " + trust + '\r')
        notes.write("\tPersonality traits: " + des1 + ", " + des2  + '\r')
        
        notesToAdd = input("Enter input below. Press return to save:\n")
        notes.write('\t--' + notesToAdd)
        notes.write('\n\n')

    if addNotes.lower() == 'e':
        break

    print()