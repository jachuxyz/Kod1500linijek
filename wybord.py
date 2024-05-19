import random

enemynames = ["Tomasz Gwiazda", "Lebron James", "Marcin Parówa", "Skeri Man", "Sigma"]
beaten = [1, 1, 1, 1, 0]
cost = [30, 50, 75, 100, 200, 250, 400]
hponlvl = [50, 100, 150, 200, 250, 300, 350, 450]
dmgonlvlA = [[5, 15], [10, 20], [20, 30], [45, 55], [60, 70], [65, 75], [80, 90], [120, 150]]
dmgonlvlB = [[1, 30], [5, 30], [12, 40], [30, 70], [30, 80], [50, 85], [60, 90], [80, 175]]
hplvl = 1
dmglvl = 1
money = 10000
enemies = [[70, [5, 10]], [150, [10, 20]], [200, [30, 50]], [350, [45, 60]], [500, [60, 100]]]
coinsgain = [10, 30, 50, 100, 150] 


# ----------------------------------------------------------------------------------------------------------------
def lobby():
    for i in range(0, 5):
        print(f"{i+1} - Walka z {enemynames[i]}")
    print("S - Status ulepszeń")
    print("P - Portfel")
    print(f"A - Ulepsz Damage - {cost[dmglvl-1]}")
    print(f"B - Ulepsz HP - {cost[hplvl-1]}")
    inp = input("Wybierz Akcję: ")
    return inp

def printatacks():
    print("A - Strzała")
    print("B - Ogień")

def main():
    global hplvl, dmglvl, money, beaten

    name = input("Podaj imię swojej postaci: ")
    running = True
    while running:
        action = lobby()
        if action == "1":
            yourhp = hponlvl[hplvl-1]
            enemyname = enemynames[0]
            enemyhp = enemies[0][0]
            print(f"{name} vs {enemyname}")
            yourturn = True
            while yourhp > 0 and enemyhp > 0:
                if yourturn:
                    print(f"Twoje HP - {yourhp}")
                    print(f"Przeciwnika HP - {enemyhp}")
                    printatacks()
                    inp = input("Wybierz Atak: ")
                    if inp == "A":
                        enemyhp -= random.randint(dmgonlvlA[dmglvl][0], dmgonlvlA[dmglvl][1]+1)
                        yourturn = False
                    if inp == "B":
                        enemyhp -= random.randint(dmgonlvlB[dmglvl][0], dmgonlvlB[dmglvl][1]+1)
                        yourturn = False
                    if inp != "A" and inp != "B":
                        print("Niepoprawny wybór")
                if not yourturn:
                    yourhp -= random.randint(enemies[0][1][0], enemies[0][1][1])
                    yourturn = True
            if yourhp > 0:
                print("Wygrałeś!")
                print(f"Otrzymujesz {coinsgain[0]} pieniędzy!")
                money += coinsgain[0]
                beaten[0] = 1
            else:
                print("Przegrałeś!")
        if action == "2":
            yourhp = hponlvl[hplvl-1]
            enemyname = enemynames[1]
            enemyhp = enemies[1][0]
            print(f"{name} vs {enemyname}")
            yourturn = True
            while yourhp > 0 and enemyhp > 0:
                if yourturn:
                    print(f"Twoje HP - {yourhp}")
                    print(f"Przeciwnika HP - {enemyhp}")
                    printatacks()
                    inp = input("Wybierz Atak: ")
                    if inp == "A":
                        enemyhp -= random.randint(dmgonlvlA[dmglvl][0], dmgonlvlA[dmglvl][1]+1)
                        yourturn = False
                    if inp == "B":
                        enemyhp -= random.randint(dmgonlvlB[dmglvl][0], dmgonlvlB[dmglvl][1]+1)
                        yourturn = False
                    if inp != "A" and inp != "B":
                        print("Niepoprawny wybór")
                if not yourturn:
                    yourhp -= random.randint(enemies[1][1][0], enemies[1][1][1])
                    yourturn = True
            if yourhp > 0:
                print("Wygrałeś!")
                print(f"Otrzymujesz {coinsgain[1]} pieniędzy!")
                money += coinsgain[1]
                beaten[1] = 1
            else:
                print("Przegrałeś!")
        if action == "3":
            yourhp = hponlvl[hplvl-1]
            enemyname = enemynames[2]
            enemyhp = enemies[2][0]
            print(f"{name} vs {enemyname}")
            yourturn = True
            while yourhp > 0 and enemyhp > 0:
                if yourturn:
                    print(f"Twoje HP - {yourhp}")
                    print(f"Przeciwnika HP - {enemyhp}")
                    printatacks()
                    inp = input("Wybierz Atak: ")
                    if inp == "A":
                        enemyhp -= random.randint(dmgonlvlA[dmglvl][0], dmgonlvlA[dmglvl][1]+1)
                        yourturn = False
                    if inp == "B":
                        enemyhp -= random.randint(dmgonlvlB[dmglvl][0], dmgonlvlB[dmglvl][1]+1)
                        yourturn = False
                    if inp != "A" and inp != "B":
                        print("Niepoprawny wybór")
                if not yourturn:
                    yourhp -= random.randint(enemies[2][1][0], enemies[2][1][1])
                    yourturn = True
            if yourhp > 0:
                print("Wygrałeś!")
                print(f"Otrzymujesz {coinsgain[2]} pieniędzy!")
                money += coinsgain[2]
                beaten[2] = 1
            else:
                print("Przegrałeś!")
        if action == "4":
            yourhp = hponlvl[hplvl-1]
            enemyname = enemynames[3]
            enemyhp = enemies[3][0]
            print(f"{name} vs {enemyname}")
            yourturn = True
            while yourhp > 0 and enemyhp > 0:
                if yourturn:
                    print(f"Twoje HP - {yourhp}")
                    print(f"Przeciwnika HP - {enemyhp}")
                    printatacks()
                    inp = input("Wybierz Atak: ")
                    if inp == "A":
                        enemyhp -= random.randint(dmgonlvlA[dmglvl][0], dmgonlvlA[dmglvl][1]+1)
                        yourturn = False
                    if inp == "B":
                        enemyhp -= random.randint(dmgonlvlB[dmglvl][0], dmgonlvlB[dmglvl][1]+1)
                        yourturn = False
                    if inp != "A" and inp != "B":
                        print("Niepoprawny wybór")
                if not yourturn:
                    yourhp -= random.randint(enemies[3][1][0], enemies[3][1][1])
                    yourturn = True
            if yourhp > 0:
                print("Wygrałeś!")
                print(f"Otrzymujesz {coinsgain[3]} pieniędzy!")
                money += coinsgain[3]
                beaten[3] = 1
            else:
                print("Przegrałeś!")
        if action == "5":
            yourhp = hponlvl[hplvl-1]
            enemyname = enemynames[4]
            enemyhp = enemies[4][0]
            print(f"{name} vs {enemyname}")
            yourturn = True
            while yourhp > 0 and enemyhp > 0:
                if yourturn:
                    print(f"Twoje HP - {yourhp}")
                    print(f"Przeciwnika HP - {enemyhp}")
                    printatacks()
                    inp = input("Wybierz Atak: ")
                    if inp == "A":
                        enemyhp -= random.randint(dmgonlvlA[dmglvl][0], dmgonlvlA[dmglvl][1]+1)
                        yourturn = False
                    if inp == "B":
                        enemyhp -= random.randint(dmgonlvlB[dmglvl])[0]
