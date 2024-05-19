# zmienne.py
from colors import Colors



def pobierz_dane():
    print(f'{Colors.BLUE}Zmodyfikuj swoją postać:{Colors.END}')
    imie = input(f"{Colors.MAGENTA}Podaj imię:{Colors.END}{Colors.GREEN}... {Colors.END}")
    nazwisko = input(f"{Colors.MAGENTA}Podaj nazwisko:{Colors.END}{Colors.GREEN} ...{Colors.END}")
    wiek = int(input(f"{Colors.MAGENTA}Podaj wiek:{Colors.END}{Colors.GREEN}... {Colors.END}"))
    return imie, nazwisko, wiek