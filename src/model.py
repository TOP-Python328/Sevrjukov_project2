from dataclasses import dataclass


class DictOfRanges(dict):
    def __init__(self, mappable: dict):
        for key in mappable:
            if (
                   not isinstance(key, tuple) 
                or len(key) != 2
                or not isinstance(key[0], int) 
                or not isinstance(key[1], int)
            ):
                raise ValueError('...')
        super().__init__(mappable)
    
    def __getitem__(self, key: int):
        if isinstance(key, int):
            for left, right in self:
                if left <= key <= right:
                    return super().__getitem__((left, right))
        else:
            return super().__getitem__(key)
    
    def get_range(self, key: int) -> tuple[int, int]:
        if isinstance(key, int):
            for left, right in self:
                if left <= key <= right:
                    return left, right
        else:
            raise TypeError

@dataclass 
class KindParameter:
    name: str
    val: float
    min: int
    max: int


class Action:
    def __init__(self, name, creature):
        self.name = name
        self.creature = creature
        #self.creature: Creature = creature

    def do(self):
        pass


class PlayerAction(Action):
    image: str


class CreatureAction(Action):
    image: str
    chance: float


class NoAction(Action):
    image: str


class MaturePhase:
    def __init__(self, days, params, player_actions, creature_actions):
        self.days = days
        self.params: set[KindParameter] = params
        self.player_actions: set[PlayerAction] = player_actions
        self.creature_actions: set[CreatureAction] = creature_actions


# class CreatureParameter:
#     def __init__(self, name, val, min, max, creature):
#         self.name = name
#         self.val: float = val
#         self.min: float = min
#         self.max: float = max
#         self.creature = creature
        
#     def get_value(self):
#         return self.val
    
#     def range(self):
#         return tuple(self.min, self.max)
    
#     def set_value(self, new_val):
#         self.val = new_val

#     def update(self):
#         pass