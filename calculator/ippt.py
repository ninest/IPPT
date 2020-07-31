
from static import get_static_score, Station
from run import get_run_score
from data.awards import awards


def get_score(age, pushups, situps, run_secs):
  puhsups_score, pushups_next_score = get_static_score(Station.pushup, age, pushups)
  situps_score, situps_next_score = get_static_score(Station.situp, age, situps)
  run_score, run_next_score = get_run_score(age, run_secs)

  total = puhsups_score + situps_score + run_score

  # find awards

  for award in awards:
    if total >= award.min_score:
      result = award


  return {
      "pushups": {
          "score": puhsups_score,
          "next": pushups_next_score
      },
      "situps": {
          "score": situps_score,
          "next": situps_next_score
      },
      "run": {
          "score": run_score,
          "next": run_next_score
      },
      "age": age,
      "total": total,
      "result": result.to_dict()
  }


a =get_score(age=18, pushups=31, situps=37, run_secs=100)
