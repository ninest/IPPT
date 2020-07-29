from static import Station, get_score

s_score, s_next = get_score(Station.situp, 41, 23)
p_score, p_next = get_score(Station.pushup, 41, 14)

print(f"Situps: {s_score}, Next: {s_next}")
print(f"Pushups: {p_score}, Next: {p_next}")