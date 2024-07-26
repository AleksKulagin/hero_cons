
import random




class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name} и нанёс {self.attack_power} урона.")

    def is_alive(self):
        return self.health > 0

from hero import Hero

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Игра началась!")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            self.display_status()

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def display_status(self):
        print(f"{self.player.name}: {self.player.health} здоровья.")
        print(f"{self.computer.name}: {self.computer.health} здоровья.")
        print("-" * 20)


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()
