import random

MIN_VALUE = 1
MAX_VALUE = 100

def safe_input():
    while True:
        try:
            user_tip = int(input("Tvůj tip: "))
            return user_tip
        except:
            print("Není to číslo! ")

randomne_cislo = random.randint(MIN_VALUE, MAX_VALUE)

finished = False

while not finished:
    tip = safe_input()
    if tip <= MAX_VALUE and tip >= MIN_VALUE:
        if tip == randomne_cislo:
            print("Vyhra!")
            finished = True
        elif randomne_cislo > tip:
            print ("Moc male")
        elif randomne_cislo < tip:
            print ("Moc velke")
    else:
        raise ValueError("Číslo mimo zadany rozsah")
