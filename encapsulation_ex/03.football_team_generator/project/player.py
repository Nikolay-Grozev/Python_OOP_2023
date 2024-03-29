class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name
# """Player: {name}
# Sprint: {sprint}
# Dribble: {dribble}
# Passing: {passing}
# Shooting: {shooting}
# """

    def __str__(self):
        result = f'Player: {self.name}\n' + \
                 f'Sprint: {self.__sprint}\n' + \
                 f'Dribble: {self.__dribble}\n' + \
                 f'Passing: {self.__passing}\n' + \
                 f'Shooting: {self.__shooting}'
        return result

