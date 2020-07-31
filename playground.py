# from static import Station, get_score
# from run import get_run_score

age = 18

pushups = get_score(
    Station.pushup,
    age=age,
    reps=20
)

situps = get_score(
    Station.situp,
    age=age,
    reps=40
)

run = get_run_score(
  age,
  12 * 60 + 30
)

print(pushups, situps, run)

total = pushups + situps + run

print(total)
