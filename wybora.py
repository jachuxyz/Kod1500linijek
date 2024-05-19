from random import randint, choice
from colors import Colors
def wybora():
    print(f'{Colors.BLUE}Jesteś w Gdańsku.\n')
    
    print(f'Gdy wychodzisz z samochodu, widzisz grupę osób.')

    print(f'Postanawiasz do nich podejść.{Colors.END}')

    print(f'{Colors.YELLOW}Masz jakiś problem?" - mówi nieznajomy, patrząc na Ciebie.{Colors.END}')

    odpowiedz = input(f"{Colors.BLUE}Możesz odpowiedzieć, co chcesz:{Colors.END} ")

    if odpowiedz:
        print(f'{Colors.YELLOW}Nieoczekiwanie nieznajomy postanawia zaatakować cie.{Colors.END}')
    else:
        print(f'{Colors.YELLOW}Nieoczekiwanie nieznajomy postanawia zaatakować cie.{Colors.END}')


    zlotowki = 4
    life = 20  

    przeciwnicy = [
        ["Napastnik1", 100, 5, 0],  
        ["Napastnik2", 100, 5, 0],
        ["Napastnik3", 120, 6, 0],  
        ["Napastnik4", 120, 6, 0],
        ["Napastnik5", 140, 7, 0],
        ["Napastnik6", 140, 7, 0],
        ["Napastnik7", 160, 8, 0],
        ["Napastnik8", 160, 8, 0]
    ]

    def atak_piescia():
        return randint(3, 6)  

    def atak_sztyletem():
        return randint(5, 10) 

    def wybierz_atak():
        print(f'{Colors.BLUE}Wybierz akcję:{Colors.END}')
        print(f'{Colors.YELLOW}A - z pięści')
        print(f'B - ze sztyletu{Colors.END}')
        co = input().upper()
        if co == 'A':
            return atak_piescia()
        elif co == 'B':
            return atak_sztyletem()
        else:
            print(f"{Colors.BLUE}Nie wybrano dobrej akcji{Colors.END}")
            return 0

    def drilowcy():
        return choice(przeciwnicy)

    liczba_pokonanych_przeciwników = 0

    while life > 0:
        opponent = drilowcy()
        print("-" * 40)

        while opponent[1] > 0 and life > 0:
            print(f"{Colors.BLUE}Walczysz teraz z {opponent[0]}")
            print(f"Przeciwnik ma {opponent[1]} HP i zadaje Ci {opponent[2]} obrażeń{Colors.END}")

            life -= opponent[2]
            if life <= 0:
                print(f"{Colors.BLUE}Masz {Colors.END}{Colors.GREEN}{life} HP {Colors.END}{Colors.YELLOW}i {Colors.END}{Colors.GREEN}{zlotowki} złotówek{Colors.END}")
                print(f'{Colors.RED}Porażka!!! Przegrałeś!!!{Colors.END}')
                break

            atak = wybierz_atak()
            opponent[1] -= atak
            print(f"{Colors.GREEN}Zadałeś {atak} obrażeń{Colors.END}")

        if opponent[1] <= 0:
            print('Zabiłeś przeciwnika!!!')
            liczba_pokonanych_przeciwników += 1

        if liczba_pokonanych_przeciwników % 2 == 0: 
            opponent = drilowcy()
            print(f"{Colors.BLUE}Na horyzoncie pojawił się kolejny napastnik!{Colors.END}")

    print("-" * 40)
    print(f"{Colors.RED}KONIEC GRY!{Colors.END}")
    print(f"{Colors.BLUE}Zabiłeś {liczba_pokonanych_przeciwników} drilowców{Colors.END}")

    if liczba_pokonanych_przeciwników == 0:
        print(f'{Colors.RED}Porażka!!! Przegrałeś!!!{Colors.END}')
    elif liczba_pokonanych_przeciwników == 1:
        print(f'{Colors.GREEN}Brawo, odtąd żyjesz spokojnym życiem.{Colors.END}')
if __name__ == "__main__":
    wybora()