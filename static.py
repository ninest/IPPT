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

  age_group = get_age_group(age)

  # get the score set for the age group
  score_set = score_table[age_group]["score_set"]
  top_score_reps = score_table[age_group]["top_score_reps"]


  # add zeroes to padd the end
  zeroes = top_score_reps - len(score_set)
  score_set += [0] * zeroes

  # reverse score_set
  score_set = score_set[::-1]

    
    

  
  # get the score
  # remember that arrays start with 0 but reps start with 1
  score = score_set[reps - 1]

  # get reps needed until next point
  next_point_counter = 0
  for val in score_set[reps:]:
    next_point_counter += 1
    if val != score:
      break

  return score, next_point_counter

