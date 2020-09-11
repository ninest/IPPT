# from calculator.ippt import get_score
from calculator.age import get_age_group
from calculator.static import Station, get_static_score

age = 40
pushups = 45
# situps = 54
# run_secs = 12 * 60 + 30

# score = get_score(age, pushups, situps, run_secs)
ag = get_age_group(age)
score = get_static_score(Station.pushup, ag, pushups)
print(score)
