#I added a few more sentences to the story since it ended unfinished, involving the teacher coming in and attempting to punish the whole family before they managed to evade him.
while True:
    adjective = input("adjective: ")
    animal = input("animal: ")
    verb1 = input("verb: ")
    exclamation1 = input("exclamation: ")
    verb2 = input("verb: ")
    verb3 = input("verb: ")
    verb4 = input("verb: ")
    exclamation2 = input("exclamation: ")
    exclamation3 = input("exclamation: ")
    verb5 = input("verb: ")
    noun = input("noun: ")
    verb6 = input("verb: ")
    verb7 = input("verb: ")
    verb8 = input("verb: ")
    
    
    print("\nYour story is:")
    print()
    print("The other day, I was really in trouble. It all started when I saw a very")
    print(f"{adjective} {animal} {verb1} down the hallway. '{str.capitalize(exclamation1)}!' I yelled. But all")
    print(f"I could think to do was {verb2} over and over. Miraculously,")
    print(f"that caused it to {verb3}, but not before it tried to {verb4}")
    print(f"right in front of my family. My mom said '{str.capitalize(exclamation1)}!' and we all started laughing")
    print(f"uncontrollably until the teacher happened upon the scene and declared that since the")
    print(f"{animal} had been {verb5} by the {noun}, I and my family had somehow harmed it and")
    print(f"we were to be punished by being {verb6}. Fortunately, we managed to {verb7} over the teacher and escape, and")
    print(f"we {verb8} about it all the way home!")
    
    
    print("\nRedo? (yes/no)") 
    response = input().lower()
    if response == "yes": True
    else: break