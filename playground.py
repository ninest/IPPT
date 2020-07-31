from static import Station, get_score

pushups = get_score(
    Station.pushup,
    age=18,
    reps=20
)

situps = get_score(
    Station.situp,
    age=18,
    reps=40
)


print(pushups, situps)
