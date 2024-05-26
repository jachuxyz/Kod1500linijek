from random import randint, choice
import time
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

def wybore():
    print(f'{Colors.BLUE}Wybierz swoje imię:')
    print('Imię do wyboru -> Ludwik')
    print('Imię do wyboru -> Bożena')
    print('Imię do wyboru -> Seba')
    wybierz_imie_swej_postaci = input('Wybierz imię swojej postaci: ')

    if wybierz_imie_swej_postaci == 'Ludwik':
        print(f'{Colors.GREEN}Wybrane przez ciebie imię to Ludwik. Czy chcesz usłyszeć w jakiej sytuacji się znajduje aktualnie?')
        opcja = input("Wybierz opcję (wpisz 'tak' lub 'nie'): ")
        if opcja == 'tak':
            print('Ludwik Zapalka - tak właśnie się nazywa dokładnie twoja postać. Pracuje ona aktualnie w księgowości, lecz myśli nad zmianą pracy do firmy zajmującej się kryptowalutą. Czy chcesz do niej przejść?')
        elif opcja == 'nie':
            print('Niestety podjąłeś złą decyzję. W tej grze ważne są szczegóły. Będzie ci później trudno podejmować decyzje, lecz wciąż masz szanse wygrać.')
        else:
            print('Wybierz dobrą opcję!')

        opcja = input("Wybierz opcję (wpisz 'tak' lub 'nie'): ")
        if opcja == 'tak':
            print('Postąpiłeś ryzykownie, gdyż ta branża jest dość ryzykowna.')

            print('Już pierwszego dnia odkryłeś potencjał kryptowaluty ETHERIUM. Postanowiłeś kupić ją za wszystkie udziały firmy, a to cię straciło. Twój szef ma cię za nieodpowiedzialnego, więc cię zwolnił. Wracając do domu, spotkała cię niespodziewana sytuacja. Napadli na ciebie drilowcy. Chcesz się bić?')
        elif opcja == 'nie':
            print('Ze smutku przez fakt, że odrzuciłeś decyzję, postanawiasz wcześniej wrócić do domu. Po drodze napadają na ciebie trzej osiedlowi drilowcy. Zamierzasz się bić?')
        else:
            print('Wybierz dobrą opcję!')
            

        opcja = input("Wybierz opcję (wpisz 'tak' lub 'nie'): ")



        if opcja == 'tak':
            bitwa()
        elif opcja == 'nie':



            print(f'{Colors.RED}Jesteś skończony... drilowcy wgnietają cię w ziemię.{Colors.RED}')
        
        else:
            print('Wybierz dobrą opcję!')

    elif wybierz_imie_swej_postaci == 'Giueniu':
        print(f'{Colors.GREEN}Jesteś nauczycielką w szkole, pracujesz już w niej ponad 21 lat. Dzieci powoli zaczynają cię wykańczać. Zarabiasz niewielką kwotę, aktualnie na koncie masz 127,65 złotych. Jesteś przy upadku psychiczki.{Colors.RED}')
   
    class Postac:
        def __init__(self, hp):
            self.hp = hp
            self.running = True

        def run(self):
            while self.running and self.hp > 0:
                time.sleep(5)
                self.trac_hp(10)

            if self.hp <= 0:
                print("Porażka - Zdrowie psychiczne spadło do zera!")

        def trac_hp(self, amount):
            self.hp -= amount
            print(f"Zdrowie psychiczne: {self.hp} HP")

        def stop(self):
            self.running = False

    moja_postac = Postac(hp=500)



    print(f'{Colors.END}Pewnego razu napadają na ciebie zamaskowani uczniowie, żądają od ciebie 150 złotych, co zamierzasz robić? Oddasz im czy nie?')
    opcja = input("Wybierz opcję (wpisz 'oddaje' lub 'nie oddaje'): ")
    if opcja == 'oddaje':
        print(f'{Colors.RED}Nie masz takiej kwoty! Zostajesz pobita, a twój stan psychiczny jest u schyłku wytrzymałości!{Colors.END}')
        moja_postac.trac_hp(480)

    elif opcja == 'nie oddaje':
        print('Postanawiasz uciekać, niestety oni cię doganiają. Jedyną opcją na przetrwanie jest walka...')
        bitwa()

    else:
        print(f'Wybierz dobrą opcję!!!{Colors.YELLOW}')




    
    from random import randint, choice

    life = 13
    zlotowki = 127.65

    def atak_bronia():
        return randint(2, 3)

    def atak_reka():
        global zlotowki
        if zlotowki < 4:
            print("-" * 40)
            print("Nie masz wystarczającej ilości złotówek!")
            return 0
        zlotowki -= 4
        return randint(2, 9)

    def wybierz_atak():
        print('A - broń')
        print('B - piesci')
        co = input().upper()
        if co == 'A':
            return atak_bronia()
        elif co == 'B':
            return atak_reka()
        else:
            print("Nie wybrano dobrego wyboru")
        return 0

    def macko():
        return ["Macko", 100, 3, 0]

    liczba_pokonanych_przeciwników = 0

    while life > 0:
        opponent = macko()
        print("-" * 40)

        while opponent[1] > 0 and life > 0:
            print(f"Seba walczy teraz z {opponent[0]}")
            print(f"{opponent[0]} ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")

            life -= opponent[2]
            if life <= 0:
                print(f"Masz {life} HP i {zlotowki} złotówek")
            atak = wybierz_atak()
            opponent[1] -= atak
            print(f"Zadałeś {atak} obrażeń")

        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_pokonanych_przeciwników += 1

    print("-" * 40)
    print("KONIEC GRY!")
    print(f"Zabiłeś {liczba_pokonanych_przeciwników} napastników!")

    if liczba_pokonanych_przeciwników == 0:
        print('Porażka!!! Przegrałeś!!!')

        
    elif liczba_pokonanych_przeciwników == 1:
        print('Udało ci się! Juz teraz tylko wypoczywac.')


    elif wybierz_imie_swej_postaci == 'Seba':
        print(f'Jesteś Seba. Wszyscy się ciebie boją. Idziesz właśnie wyjaśnić sprawę z Mackiem, który się tobie ostatnio sprzeciwiał.{Colors.YELLOW}')

def bitwa():
    life = 13
    zlotowki = 127.65

    def atak_piescia():
        
        return randint(3, 5)

    def ucieczka():
        global zlotowki
        if zlotowki < 4:
            print("-" * 40)
            print("Nie masz wystarczającej ilości złotówek!")
            return 0
        zlotowki -= 4
        return randint(29, 29)

    def wybierz_atak():
        print('A - z pięści')
        print('B - ucieczka')
        co = input().upper()
        if co == 'A':
            return atak_piescia()
        elif co == 'B':
            return ucieczka()
        else:
            print("Nie wybrano dobrej akcji")
        return 0

    def drilowcy():
        opponents = [
            ["Malik Montana", 100, 3, 0],
            ["Drillowiec", 100, 3, 0]
        ]
        return choice(opponents)

    liczba_pokonanych_przeciwników = 0

    while life > 0:
        opponent = drilowcy()
        print("-" * 40)

        while opponent[1] > 0 and life > 0:
            print(f"Ludwik walczy teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń")

            life -= opponent[2]
            if life <= 0:
                print(f"Masz {life} HP i {zlotowki} złotówek")
            atak = wybierz_atak()
            opponent[1] -= atak
            print(f"Zadałeś {atak} obrażeń")

        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_pokonanych_przeciwników += 1

    print("-" * 40)
    print("KONIEC GRY!")
    print(f"Zabiłeś {liczba_pokonanych_przeciwników} drilowców  ")
    if liczba_pokonanych_przeciwników == 0:
        print('Porazka!!! Przegrałeś!!!')
    if liczba_pokonanych_przeciwników == 1:
        print('Brawoo, odtąd żyjesz spokojnym  zyciem.')

if __name__ == "__main__":
    wybore()
