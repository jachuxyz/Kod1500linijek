import random

# Initial data
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

# Function to display the lobby
def lobby():
    for i in range(0, 5):
        print(f"{i+1} - Walka z {enemynames[i]}")
    print("S - Status ulepszeń")
    print("P - Portfel")
    print(f"A - Ulepsz Damage - {cost[dmglvl-1]}")
    print(f"B - Ulepsz HP - {cost[hplvl-1]}")
    inp = input("Wybierz Akcję: ")
    return inp

# Function to display attack options
def printatacks():
    print("A - Strzała")
    print("B - Ogień")

# Main function for the game
def wybord():
    global hplvl, dmglvl, money, beaten

    name = input("Podaj imię swojej postaci: ")
    running = True
    while running:
        action = lobby()
        if action in ["1", "2", "3", "4", "5"]:
            index = int(action) - 1
            yourhp = hponlvl[hplvl-1]
            enemyname = enemynames[index]
            enemyhp = enemies[index][0]
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
                    elif inp == "B":
                        enemyhp -= random.randint(dmgonlvlB[dmglvl][0], dmgonlvlB[dmglvl][1]+1)
                        yourturn = False
                    else:
                        print("Niepoprawny wybór")
                if not yourturn:
                    yourhp -= random.randint(enemies[index][1][0], enemies[index][1][1])
                    yourturn = True
            if yourhp > 0:
                print("Wygrałeś!")
                print(f"Otrzymujesz {coinsgain[index]} pieniędzy!")
                money += coinsgain[index]
                beaten[index] = 1
            else:
                print("Przegrałeś!")
        elif action == "S":
            print(f"HP Level: {hplvl}, Damage Level: {dmglvl}")
        elif action == "P":
            print(f"Money: {money}")
        elif action == "A":
            if money >= cost[dmglvl-1]:
                money -= cost[dmglvl-1]
                dmglvl += 1
                print(f"Ulepszono Damage do poziomu {dmglvl}")
            else:
                print("Nie masz wystarczająco pieniędzy")
        elif action == "B":
            if money >= cost[hplvl-1]:
                money -= cost[hplvl-1]
                hplvl += 1
                print(f"Ulepszono HP do poziomu {hplvl}")
            else:
                print("Nie masz wystarczająco pieniędzy")
        else:
            print("Niepoprawna akcja")

if __name__ == "__main__":
    wybord()