import random
from colors import Colors

def wyborc():
    print(f'{Colors.GREEN}Witaj w grze Blackjack!{Colors.END}\n')

    print(f'{Colors.YELLOW}Zasady gry:{Colors.END}')
    print(f'{Colors.YELLOW}1. Celem gry jest uzyskanie sumy punktów jak najbliżej 21, ale nie przekraczając tej liczby.{Colors.END}')
    print(f'{Colors.YELLOW}2. Każda karta ma wartość liczbową równą swojej wartości numerycznej (2-10), karty J, Q i K mają wartość 10, a as może być 1 lub 11, w zależności od sytuacji.{Colors.END}')
    print(f'{Colors.YELLOW}3. Na początku każdego rozdania gracz otrzymuje dwie karty. Jeden z krupierów karty jest odkryty, a drugi ukryty.{Colors.END}')
    print(f'{Colors.YELLOW}4. Gracz może dobrać karty, aby zbliżyć się do 21. Jeśli przekroczy 21, przegrywa tę rundę.{Colors.END}')
    print(f'{Colors.YELLOW}5. Krupier następnie dobiera karty, aż suma punktów w jego ręce osiągnie co najmniej 17.{Colors.END}')
    print(f'{Colors.YELLOW}6. Jeśli gracz ma lepszą rękę niż krupier bez przekraczania 21, wygrywa. Jeśli krupier ma lepszą rękę lub gracz przekroczył 21, przegrywa.{Colors.END}\n')

    talia = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    random.shuffle(talia)

    karty_gracza = []
    karty_krupiera = []

    def wartosc_karty(karta):
        if karta in ['J', 'Q', 'K']:
            return 10
        elif karta == 'A':
            return 11
        else:
            return int(karta)

    def wartosc_reki(reka):
        suma = sum(wartosc_karty(karta) for karta in reka)
        if suma > 21 and 'A' in reka:
            while suma > 21 and 'A' in reka:
                suma -= 10
                reka.remove('A')
        return suma

    def wyswietl_reke_gracza():
        print(f'{Colors.CYAN}Twoje karty:{Colors.END}', ', '.join(karty_gracza))
        print(f'{Colors.CYAN}Wartość Twojej ręki:{Colors.END}', wartosc_reki(karty_gracza), "\n")

    def wyswietl_reke_krupiera(pokaz_ukryta_karte=False):
        if pokaz_ukryta_karte:
            print(f'{Colors.PURPLE}Karty krupiera:{Colors.END}', ', '.join(karty_krupiera))
            print(f'{Colors.PURPLE}Wartość ręki krupiera:{Colors.END}', wartosc_reki(karty_krupiera), "\n")
        else:
            print(f'{Colors.PURPLE}Karty krupiera:{Colors.END}', karty_krupiera[0], "[Ukryta karta]\n")

    
    for _ in range(2):
        karty_gracza.append(talia.pop())
        karty_krupiera.append(talia.pop())

    wyswietl_reke_gracza()
    wyswietl_reke_krupiera()

    # Tura gracza
    while wartosc_reki(karty_gracza) < 21:
        decyzja = input(f"{Colors.YELLOW}Czy chcesz dobrać kartę? (t/n): {Colors.END}").lower()
        if decyzja == 't':
            karty_gracza.append(talia.pop())
            wyswietl_reke_gracza()
        else:
            break

    if wartosc_reki(karty_gracza) > 21:
        print(f'{Colors.RED}Przegrałeś, suma Twoich kart przekroczyła 21!{Colors.END}')
        return

  
    wyswietl_reke_krupiera(pokaz_ukryta_karte=True)
    while wartosc_reki(karty_krupiera) < 17:
        karty_krupiera.append(talia.pop())
        wyswietl_reke_krupiera(pokaz_ukryta_karte=True)

    if wartosc_reki(karty_krupiera) > 21 or wartosc_reki(karty_gracza) > wartosc_reki(karty_krupiera):
        print(f'{Colors.GREEN}Gratulacje! Wygrałeś!{Colors.END}')
    elif wartosc_reki(karty_gracza) == wartosc_reki(karty_krupiera):
        print(f'{Colors.YELLOW}Remis! Nikt nie wygrywa.{Colors.END}')
    else:
        print(f'{Colors.RED}Przegrałeś! Krupier ma lepszą rękę.{Colors.END}')

if __name__ == "__main__":
    wyborc()
