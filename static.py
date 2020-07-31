from enum import Enum, unique
from age import get_age_group


@unique
class Station(Enum):
  situp = 0
  pushup = 1


def get_score(station: Station, age: int, reps: int):
  pass
