from enum import Enum, unique
from data.situp import situp_score_table
from data.pushup import pushup_score_table
from age import get_age_group


@unique
class Station(Enum):
  situp = 0
  pushup = 1


def get_score(station: Station, age: int, reps: int):
  if station == Station.situp:
    score_table = situp_score_table
  else:
    score_table = pushup_score_table

  age = 18
  reps = 35

  age_group = get_age_group(age)

  # get the score set for the age group
  score_set = score_table[age_group]["score_set"]
  top_score_reps = score_table[age_group]["top_score_reps"]

  # add zeroes to padd the end
  zeroes = top_score_reps - len(score_set)
  score_set += [0] * zeroes

  # get the score
  score = score_set[::-1][reps]
  print(score)
