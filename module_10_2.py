from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        days = 0
        enemy = 100
        print(f"{self.name}, на нас напали!")
        while enemy > 0:
            sleep(1)
            enemy -= self.power
            days += 1
            print(f"{self.name} сражается {days}..., осталось {enemy} воинов.\n")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
