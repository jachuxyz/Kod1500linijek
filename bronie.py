# bronie.py
import random

class Weapon:
    def __init__(self, name, base_damage, story_continuation):
        self.name = name
        self.base_damage = base_damage
        self.story_continuation = story_continuation

    def attack(self):
        return self.base_damage

class Dagger(Weapon):
    def __init__(self):
        base_damage = 10
        super().__init__("Sztylet", base_damage, "Sztylet, chociaż mała, ale zawsze pewna broń, która może być decydująca w walce.")

    def attack(self):
        base_damage = super().attack()
        damage_variation = random.randint(-1, 1) * round(base_damage * 0.1)  
        return base_damage + damage_variation

class Shovel(Weapon):
    def __init__(self):
        base_damage = 8
        super().__init__("Łopata", base_damage, "Łopata, przydatna nie tylko do kopania, ale także do zadawania obrażeń w walce.")

    def attack(self):
        base_damage = super().attack()
        damage_variation = random.randint(-1, 1) * round(base_damage * 0.1)  
        return base_damage + damage_variation

class Bow(Weapon):
    def __init__(self):
        base_damage = 12
        super().__init__("Łuk", base_damage, "Łuk, broń dystansowa, która umożliwia atakowanie wrogów z bezpiecznej odległości.")

    def attack(self):
        base_damage = super().attack()
        damage_variation = random.randint(-1, 1) * round(base_damage * 0.1)  
        return base_damage + damage_variation

class Club(Weapon):
    def __init__(self):
        base_damage = 7
        super().__init__("Pałka", base_damage, "Pałka, prosta, ale skuteczna broń, która zadaje solidne obrażenia w walce wręcz.")

    def attack(self):
        base_damage = super().attack()
        damage_variation = random.randint(-1, 1) * round(base_damage * 0.1)  
        return base_damage + damage_variation

class Rapier(Weapon):
    def __init__(self):
        base_damage = 14
        super().__init__("Rapier", base_damage, "Rapier, szybka i zwinna broń, idealna dla graczy preferujących szybkie ataki.")

    def attack(self):
        base_damage = super().attack()
        damage_variation = random.randint(-1, 1) * round(base_damage * 0.1)
