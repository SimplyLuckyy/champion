# Numbers are placeholders. Balance later

class Enemy:
    def __init__(self):
        self.health = 0
        self.attack = 0
        self.defense = 0

class Skeleton(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Skeleton"
        self.health = 40
        self.attack = 10
        self.defense = 5

class Spider(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Giant Spider"
        self.health = 50
        self.attack = 5
        self.defense = 3

# Change to something else. Something Armored or Flying (Rogues keen eye allows them to see weak points)
class Bat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Giant Bat"
        self.health = 40
        self.attack = 3
        self.defense = 8

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "temp"
        self.health = 200
        self.attack = 20
        self.defense = 20