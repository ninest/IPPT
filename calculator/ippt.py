from static import get_static_score, Station
from run import get_run_score

def get_score(age, pushups, situps, run_secs):
  puhsups_score = get_static_score(Station.pushup, age, pushups)
  situps_score = get_static_score(Station.situp, age, situps)
  run_score = get_run_score(age, run_secs)