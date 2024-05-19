# osoba.py
from colors import Colors

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        return (f'{Colors.END}{Colors.BLUE}Witaj{Colors.END}{Colors.MAGENTA} {self.imie} {self.nazwisko}{Colors.BLUE}. {Colors.END}{Colors.MAGENTA} Masz{self.wiek}{Colors.END}{Colors.BLUE} lat.{Colors.END}')

    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie

    def zmien_nazwisko(self, nowe_nazwisko):
        self.nazwisko = nowe_nazwisko

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek