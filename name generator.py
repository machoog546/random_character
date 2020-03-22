import names, random

ages = ['Young', 'Teen', 'Adult', 'Old']
personality = ["open", "driven", 'extravert ', 
                'agreeable', 'anxiety', 'fear',
                 'anger', 'frustration', 'envy', 'jealousy', 
                 'guilt', 'depressed', 'lonely']
trustLevel = ["parinoid", "trusting", 'neutral', 'flip-floppy']

notes =  open('Char Notes.txt', 'w+')



while True:
    person = names.get_full_name()
    age = random.choice(ages)
    trust = random.choice(trustLevel)
    des1, des2 = random.choice(personality), random.choice(personality)


    print("Name: " + person)
    print("Age: " + age)
    print("Trust level: " + trust)
    print("Personality traits: " + des1 + ", " + des2 )

    addNotes = input("Would you like to add notes?\ny to add, or enter to skip, e to exit: \n")
    if addNotes.lower() == 'y':
        notesToAdd = input("Enter input below. Press return to save:\n")
        notes.write(notesToAdd)
    if addNotes.lower() == 'e':
        break

    print()