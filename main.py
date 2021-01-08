# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

import sys


class Player:
    def __init__(self, name, speed, endurance, accuracy):
        try:
            if ((0 <= endurance <= 1) and (0 <= accuracy <= 1)):
                self.name = name
                self.speed = speed
                self.endurance = endurance
                self.accuracy = accuracy
            else:
                raise ValueError(
                    "Endurance and accuracy should be more than naught and less or equal 1")
        except ValueError as error:
            print(error)
            sys.exit(1)


class introduce:
    def __init__(self):
        self.introduction = (f"Hello everyone my name is {player.name}. ")


class strength:
    def __new__(self):
        if (player.speed >= player.endurance and player.speed >= player.accuracy):
            return "speed", player.speed
        elif (player.endurance > player.speed and player.endurance >= player.accuracy):
            return "endurance", player.endurance
        else:
            return "accuracy", player.accuracy


player = Player("Peter", 10, 0.5, 0.5)
introduce_ = introduce()
print(introduce_.introduction)
strong = strength()
print(type(strong))
tp = (3, 4, 5)
print(type(tp))
