from static import get_static_score, Station
from run import get_run_score


def get_score(age, pushups, situps, run_secs):
  puhsups_score, pushups_next_score = get_static_score(Station.pushup, age, pushups)
  situps_score, situps_next_score = get_static_score(Station.situp, age, situps)
  # run_score = get_run_score(age, run_secs)

  return {
      "pushups": {
          "score": puhsups_score,
          "next": pushups_next_score
      },
      "situps": {
          "score": situps_score,
          "next": situps_next_score
      }
  }


print(
    get_score(age=18, pushups=20, situps=40, run_secs=100)
)
