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
        self.health = 30
        self.attack = 10
        self.defense = 3

class Spider(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Giant Spider"
        self.health = 60
        self.attack = 8
        self.defense = 3

# Change to something else. Something Armored or Flying (Rogues keen eye allows them to see weak points)
class Bat(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Giant Bat"
        self.health = 40
        self.attack = 5
        self.defense = 10

class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "temp"
        self.health = 100
        self.attack = 12
        self.defense = 15