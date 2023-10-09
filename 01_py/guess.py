import random

randomne_cislo = random.randint(1, 100)

finished = False

while not finished:
    tip = int(input("Tvuj tip: "))
    if tip == randomne_cislo:
        print("Vyhra!")
        finished = True
    elif randomne_cislo > tip:
        print ("Moc male")
    elif randomne_cislo < tip:
        print ("Moc velke")
    
