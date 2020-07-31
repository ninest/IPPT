from .age import get_age_group
from .data.run import run_times, running_score_table


def get_run_score(age, secs):
  age_group = get_age_group(age)

  # check for max or min run times
  if secs > run_times[0]:
    secs = run_times[0]
  elif secs < run_times[-1]:
    secs = run_times[-1]

  else:
    # round up to nearest 10
    secs = round(secs, -1)
  
  # get the position in the array of the timing
  pos = run_times.index(secs)
  
  # get score
  score = running_score_table[age_group][pos]
  return score

