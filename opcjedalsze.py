
from wybora import wybora
from wyborb import wyborb
from wyborc import wyborc
from wybord import wybord
from wybore import wybore

def start():
    print("Wybierz dalsza opcje swej przygody:")
    print("a. Gra fabularna, rpg")
    print('b, Inna opcaj gry fabularnej, rpg')
    print("b. Gra w wisielca - rozrywkowa")
    print("c. Gra w karty (np. Blackjack)- hazard")
    print("d. Gra RPG z roznymi postaciami.")
    print("e. Gra z drillowcami.")
    wybor_gry = input("Wybierz literę od a do h: ").lower()

    if wybor_gry == 'a':
        wybora()
    elif wybor_gry == 'b':
        wyborb()
    elif wybor_gry == 'c':
        wyborc()
    elif wybor_gry == 'd':
        wybord()
    elif wybor_gry == 'e':
        wybore()       
    else:
        print("Niepoprawny wybór. Wybierz literę od a do h.")

if __name__ == "__main__":
    start()
