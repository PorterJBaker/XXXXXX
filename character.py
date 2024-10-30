from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional, Union, List
from enum import Enum
from random import randint
from coord import Coord


class CharacterDeath(Exception):

    def __init__(self, msg, char: Character):
        self.message = msg
        char.temp_health = 0


class InvalidAttack(Exception):
    pass


class Player(Enum):
    VILLAIN = 0
    HERO = 1

