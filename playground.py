from calculator.ippt import get_score

age = 18
pushups = 54
situps = 54
run_secs = 12 * 60 + 30

score = get_score(age, pushups, situps, run_secs)

print(score)
