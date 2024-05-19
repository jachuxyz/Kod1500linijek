from colors import Colors
from random import randint, choice
def wyborb():
    print(f'{Colors.BLUE}Jesteś na odległej planecie.\n')
    print(f'Kiedy wchodzisz do tajemniczej jaskini, słyszysz dziwne dźwięki.')
    print(f'Postanawiasz zbadać ich pochodzenie.{Colors.END}')

    print(f'{Colors.YELLOW}"Kto tam?" - słyszysz nagle czyjś głos.{Colors.END}')

    odpowiedz = input(f"{Colors.BLUE}Możesz odpowiedzieć, co chcesz (A/B/C):{Colors.END} ").upper()

    if odpowiedz == 'A':
        print(f'{Colors.YELLOW}"To ty, zaginiony podróżniku?" - pyta tajemnicza postać zza głosu.{Colors.END}')
        print(f'{Colors.YELLOW}"Tak, jestem. Szukam drogi powrotnej na statek kosmiczny." - odpowiadasz.{Colors.END}')
    elif odpowiedz == 'B':
        print(f'{Colors.YELLOW}"Oddaj się, podróżniku!" - słyszysz groźny ton głosu zza jaskini.{Colors.END}')
        print(f'{Colors.YELLOW}"Spokojnie, nie jestem tu po to, by wam zrobić krzywdę." - próbujesz uspokoić sytuację.{Colors.END}')
    elif odpowiedz == 'C':
        print(f'{Colors.YELLOW}"Wyprowadź się stąd natychmiast!" - krzyczy ktoś zza jaskini.{Colors.END}')
        print(f'{Colors.YELLOW}"Przepraszam, nie wiedziałem, że ta jaskinia jest zajęta. Opuszczę ją natychmiast." - odpowiadasz spokojnie.{Colors.END}')
    else:
        print(f'{Colors.YELLOW}"Nikt nie ma prawa tu wchodzić!" - słyszysz głośny głos zza jaskini.{Colors.END}')
        print(f'{Colors.YELLOW}"Przepraszam, nie chciałem naruszyć Waszej przestrzeni. Jestem tu przypadkowo." - próbujesz wyjaśnić.{Colors.END}')

    print(f'{Colors.YELLOW}"Niech no ktoś spalił tę ukrytą bazę na planecie. Co chcesz tu robić, intruzie?" - pytanie wypływa z ciemności.{Colors.END}')

    odpowiedz2 = input(f"{Colors.BLUE}Odpowiedz, wybierz (A/B/C):{Colors.END} ").upper()

    if odpowiedz2 == 'A':
        print(f'{Colors.YELLOW}"Szukam informacji o tajemniczych zjawiskach, które obserwujemy na tej planecie." - odpowiadasz.{Colors.END}')
        print(f'{Colors.YELLOW}"Zjawiska, mówisz? Może powinieneś najpierw wyjść stąd żywy, zanim coś odkryjesz." - reakcja jest ostrożna.{Colors.END}')
    elif odpowiedz2 == 'B':
        print(f'{Colors.YELLOW}"Przyszedłem, by rozwikłać tajemnice tej planety. Może moglibyśmy współpracować?" - proponujesz.{Colors.END}')
        print(f'{Colors.YELLOW}"Współpraca? Nie ufam obcym. Musisz mnie przekonać, że jesteś godny zaufania." - reakcja jest nieufna.{Colors.END}')
    elif odpowiedz2 == 'C':
        print(f'{Colors.YELLOW}"Wybacz, jeśli naruszyłem waszą prywatność. Chciałem tylko znaleźć schronienie." - tłumaczysz się.{Colors.END}')
        print(f'{Colors.YELLOW}"Schronienie? To nie hotel. Ale widzę, że nie jesteś agresywny. Może jesteś tutaj z jakimś celem?" - pytanie jest ciekawe.{Colors.END}')
    else:
        print(f'{Colors.YELLOW}"Tym lepiej dla ciebie, że nie masz już wrogów." - słyszysz odgłos kroków zbliżających się z ciemności.{Colors.END}')
        print(f'{Colors.YELLOW}"Nie chcę mieć kłopotów. Opuszczę to miejsce." - mówisz, chcąc uniknąć konfrontacji.{Colors.END}')

    zloto = 4
    zdrowie = 20  
    wrogowie = [
        ["Obcy1", 100, 5, 0],  
        ["Obcy2", 100, 5, 0],
        ["Obcy3", 120, 6, 0],  
        ["Obcy4", 120, 6, 0],
        ["Obcy5", 140, 7, 0],
        ["Obcy6", 140, 7, 0],
        ["Obcy7", 160, 8, 0],
        ["Obcy8", 160, 8, 0]
    ]

    def atak_pieta():
        return randint(3, 6)

    def atak_mieczem():
        return randint(5, 10) 

    def wybierz_atak():
        print(f'{Colors.BLUE}Wybierz akcję:{Colors.END}')
        print(f'{Colors.YELLOW}A - kopnięcie')
        print(f'B - cios mieczem{Colors.END}')
        co = input().upper()
        if co == 'A':
            return atak_pieta()
        elif co == 'B':
            return atak_mieczem()
        else:
            print(f"{Colors.BLUE}Nie wybrano odpowiedniej akcji{Colors.END}")
            return 0

    def generuj_wroga():
        return choice(wrogowie)

    liczba_pokonanych_wrogow = 0

    while zdrowie > 0:
        wrog = generuj_wroga()
        print("-" * 40)

        while wrog[1] > 0 and zdrowie > 0:
            print(f"{Colors.BLUE}Walczysz teraz z {wrog[0]}")
            print(f"Przeciwnik ma {wrog[1]} HP i zadaje Ci {wrog[2]} obrażeń{Colors.END}")

            zdrowie -= wrog[2]
            if zdrowie <= 0:
                print(f"{Colors.BLUE}Masz {Colors.END}{Colors.GREEN}{zdrowie} HP {Colors.END}{Colors.YELLOW}i {Colors.END}{Colors.GREEN}{zloto} złota{Colors.END}")
                print(f'{Colors.RED}Porażka!!! Przegrałeś!!!{Colors.END}')
                break

            atk = wybierz_atak()
            wrog[1] -= atk
            print(f"{Colors.GREEN}Zadałeś {atk} obrażeń{Colors.END}")

        if wrog[1] <= 0:
            print('Pokonałeś przeciwnika!!!')
            liczba_pokonanych_wrogow += 1

        if liczba_pokonanych_wrogow % 2 == 0: 
            wrog = generuj_wroga()
            print(f"{Colors.BLUE}Zza rogu wyskakuje kolejny obcy!{Colors.END}")

    print("-" * 40)
    print(f"{Colors.RED}KONIEC GRY!{Colors.END}")
    print(f"{Colors.BLUE}Pokonałeś {liczba_pokonanych_wrogow} obcych{Colors.END}")

    if liczba_pokonanych_wrogow == 0:
        print(f'{Colors.RED}Porażka!!! Przegrałeś!!!{Colors.END}')
    elif liczba_pokonanych_wrogow == 1:
        print(f'{Colors.GREEN}Gratulacje! Wracasz do domu jako bohater.{Colors.END}')

if __name__ == "__main__":
    wyborb()