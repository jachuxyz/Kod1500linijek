import os
import random
import time
from opcjedalsze import start
from colors import Colors

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input():
    try:
        import termios, tty, sys
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    except ImportError:
        import msvcrt
        return msvcrt.getch().decode('utf-8')

def draw_car(y, x):
    print(f"\033[{y};{x}H⛟", end='', flush=True)

def draw_obstacles(obstacles):
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
    x = max_x // 2
    y = max_y // 10
    return (y, x, "X", Colors.GREEN)

def check_collision(y, x, obstacles):
    return (y, x) in [(o[0], o[1]) for o in obstacles]

def rozwiniecie1(imie):
    clear_screen()
    print(f'{Colors.BLUE}{imie}, znajdujesz się w Warszawie. Postaraj się przedostać do {Colors.END}{Colors.GREEN}Gdańska(X na mapie){Colors.END}{Colors.BLUE}.{Colors.END}\n')
    time.sleep(5)

    y, x = 10, 20
    max_x, max_y = 80, 24  # Zakładając domyślny rozmiar terminala 80x24
    num_obstacles = 30

    obstacles = generate_obstacles(max_x, max_y, num_obstacles)
    goal = generate_goal(max_x, max_y)

    while True:
        clear_screen()

        print(f"\033[{y};{x}H ", end='', flush=True)
        draw_car(y, x)
        draw_obstacles(obstacles)
        draw_obstacles([goal])
        print("\033[1;1HPoruszaj się strzałkami (w/s/a/d). Naciśnij 'q' aby wyjść.")

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

if __name__ == "__main__":
    rozwiniecie1("Imię")