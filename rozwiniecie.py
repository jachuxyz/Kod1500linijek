from colors import Colors
from osoba import Osoba
import wstep
import os
import msvcrt
import random
import time
from opcjedalsze import start

def rozwiniecie1(imie):
    def clear_screen():
        print("\033[H\033[J", end='')  



    def get_input():
        if os.name == 'nt':
            
            return msvcrt.getch().decode('utf-8')
        else:
            return input()

    def draw_car(y, x):
        print(f"\033[{y};{x}H⛟", end='', flush=True)  



    def draw_obstacles(obstacles, max_y):
        for obstacle in obstacles:
            y, x, symbol, color = obstacle
            print(f"{color}\033[{y};{x}H{symbol}", end='', flush=True) 

        print(Colors.END, end='', flush=True)

    def generate_obstacles(max_x, max_y, num_obstacles):
        obstacles = []
        for _ in range(num_obstacles):
            x = random.randint(2, max_x - 1)
            y = random.randint(2, max_y - 1)

            symbol = "#"

            color = random.choice([Colors.RED, Colors.YELLOW])
            obstacles.append((y, x, symbol, color))  
        return obstacles
    

    def generate_goal(max_x, max_y):
        x = max_x // 2  # U
        y = max_y // 10  
        return (y, x, "X", Colors.GREEN) 




    def check_collision(y, x, obstacles):
        return (y, x) in [(o[0], o[1]) for o in obstacles]

    clear_screen()
    print(f'{Colors.BLUE}{imie}, znajdujesz sie w Warszawie. Postaraj sie przedostać do {Colors.END}{Colors.GREEN}Gdanska(X na mapie){Colors.END}{Colors.BLUE}.{Colors.END}\n')
    time.sleep(5) 

    y, x = 10, 20 
    max_x, max_y = 300, 50  
    num_obstacles = 300  

   
    obstacles = generate_obstacles(max_x, max_y, num_obstacles)

    
    goal = generate_goal(max_x, max_y)

    while True:
        clear_screen()

        
        print(f"\033[{y};{x}H ", end='', flush=True)

        
        draw_car(y, x)

        
        draw_obstacles(obstacles, max_y)

       
        draw_obstacles([goal], max_y)

        
        print("\033[1;1HPoruszaj się strzałkami. Naciśnij 'q' aby wyjść.")

        
        key = get_input()

        
        prev_y, prev_x = y, x

        
        if key == 'w':
            y = max(2, y - 1)
        elif key == 's':
            y = min(max_y - 1, y + 1)
        elif key == 'a':
            x = max(2, x - 1)
        elif key == 'd':
            x = min(max_x - 1, x + 1)
        elif key == 'q':  
            break

        
        if check_collision(y, x, obstacles):
            clear_screen()
            print(f"{Colors.RED}PRZEGRANA{Colors.END}")
            break

          
        if (y, x) == (goal[0], goal[1]):
            clear_screen()
            print(f"{Colors.GREEN}Brawo, wygrałeś!")
            start()
            break

        
        if (y, x) == (goal[0], goal[1]):
            clear_screen()
            print(f"{Colors.GREEN}Brawo, wygrałeś!")
            start()
            break

if __name__ == "__main__":
    rozwiniecie1("Imię")
