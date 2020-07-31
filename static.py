from enum import Enum, unique
from age import get_age_group

from data.pushup import pushup_score_table
from data.situp import situp_score_table


@unique
class Station(Enum):
  pushup = 0
  situp = 1


def get_score(station: Station, age: int, reps: int):
  age_group = get_age_group(age)
  score_table = pushup_score_table if station == Station.pushup else situp_score_table

  # get the score from age group
  score = score_table[age_group][reps-1]

  return score
